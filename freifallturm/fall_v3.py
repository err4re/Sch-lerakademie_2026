#!/home/freifallturm/freifall_experiment/bin/python
"""
Drop tower capture, unified clock version.

Uses picamera2 so every video frame carries a SensorTimestamp taken from the
same system clock as time.monotonic().  Video and IMU therefore land on one
time axis with no LED needed.  The LED still fires on freefall detection as an
independent backup marker.

Outputs (in /dev/shm, RAM - copy off after the run):
    <name>.h264        video
    <name>_frames.csv  frame index, sensor timestamp, monotonic time
    <name>_imu.csv     t, accel, gyro, led state

Usage:  ./drop.py [run_name]
"""

import sys, time, csv
from pathlib import Path

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
from libcamera import Transform, controls

import board, adafruit_icm20x
from gpiozero import LED

# ---------------- config ----------------
DURATION      = 10.0        # seconds
FREEFALL_G    = 0.25        # |a| below this => freefall
CONFIRM_N     = 3           # consecutive samples to debounce
LED_PIN       = 21          # GPIO21 = physical pin 40
FLASH_S       = 0.30

WIDTH, HEIGHT = 1280, 720
FPS           = 60
SHUTTER_US    = 2000
GAIN          = 8.0
LENS_POS      = 7.0         # dioptres -> 1/6.67 m = 15 cm
FLIP          = True        # camera mounted upside down

OUTDIR = Path("/dev/shm")
# ----------------------------------------

G = 9.80665
name = sys.argv[1] if len(sys.argv) > 1 else time.strftime("%Y%m%d_%H%M%S")

led = LED(LED_PIN)
led.off()

# ---------- IMU ----------
i2c = board.I2C()
try:
    icm = adafruit_icm20x.ICM20948(i2c, address=0x69)
except ValueError:
    icm = adafruit_icm20x.ICM20948(i2c, address=0x68)

icm.accelerometer_range = adafruit_icm20x.AccelRange.RANGE_16G
icm.gyro_range = adafruit_icm20x.GyroRange.RANGE_500_DPS
icm.accelerometer_data_rate_divisor = 0
icm.gyro_data_rate_divisor = 0

ax, ay, az = icm.acceleration
g0 = (ax*ax + ay*ay + az*az) ** 0.5 / G
print(f"IMU ok, resting |a| = {g0:.3f} g   (want ~1.000)")
if not 0.9 < g0 < 1.1:
    print("  WARNING: not ~1 g - check config before trusting drop data.")

# ---------- camera ----------
picam2 = Picamera2()
frame_dur = int(1_000_000 / FPS)

#cfg = picam2.create_video_configuration(
#    main={"size": (WIDTH, HEIGHT), "format": "YUV420"},
#    transform=Transform(hflip=FLIP, vflip=FLIP),
#    controls={
#        "FrameDurationLimits": (frame_dur, frame_dur),
#        "ExposureTime": SHUTTER_US,
#        "AnalogueGain": GAIN,
#        "AeEnable": False,
#        "AwbEnable": False,
#        "AfMode": controls.AfModeEnum.Manual,
#        "LensPosition": LENS_POS,
#    },
#)

cfg = picam2.create_video_configuration(
    main={"size": (WIDTH, HEIGHT), "format": "YUV420"},
    transform=Transform(hflip=FLIP, vflip=FLIP),
    controls={
        "FrameDurationLimits": (frame_dur, frame_dur),
        "AfMode": controls.AfModeEnum.Manual,
        "LensPosition": LENS_POS,
    },
)


picam2.configure(cfg)

# Per-frame timestamps, collected in the camera thread so the IMU loop
# is never blocked waiting for a frame.
frames = []          # (frame_index, sensor_timestamp_s, monotonic_at_callback)

def on_frame(request):
    md = request.get_metadata()
    ts = md.get("SensorTimestamp")
    if ts is not None:
        frames.append((len(frames), ts / 1e9, time.monotonic()))

picam2.pre_callback = on_frame

vid = OUTDIR / f"{name}.h264"
encoder = H264Encoder(bitrate=10_000_000)

print("starting camera ...")
picam2.start_recording(encoder, FileOutput(str(vid)))
time.sleep(1.5)                      # let exposure/pipeline settle

# ---------- log loop ----------
t0 = time.monotonic()
samples = []
low_count = 0
t_release = None
led_off_at = None

print("logging - release the capsule")
while time.monotonic() - t0 < DURATION:
    t = time.monotonic()
    ax, ay, az = icm.acceleration
    gx, gy, gz = icm.gyro
    a = (ax*ax + ay*ay + az*az) ** 0.5 / G

    if t_release is None:
        low_count = low_count + 1 if a < FREEFALL_G else 0
        if low_count >= CONFIRM_N:
            t_release = t
            led.on()
            led_off_at = t + FLASH_S
            print(f"  FREEFALL at t = {t - t0:.4f} s")

    if led_off_at is not None and t > led_off_at:
        led.off()
        led_off_at = None

    samples.append((t, ax, ay, az, gx, gy, gz, 1 if led.is_lit else 0))

led.off()
picam2.stop_recording()

# ---------- clock check ----------
# SensorTimestamp should already be on the same monotonic clock.  Measure the
# residual offset so we can verify rather than assume.
if frames:
    offs = [mono - ts for _, ts, mono in frames]
    offs.sort()
    median_off = offs[len(offs) // 2]
    spread = offs[-1] - offs[0]
else:
    median_off = spread = float("nan")

# ---------- write ----------
with open(OUTDIR / f"{name}_frames.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["frame", "sensor_ts_s", "t_s"])
    for i, ts, _ in frames:
        w.writerow([i, f"{ts:.6f}", f"{ts + median_off - t0:.6f}"])

with open(OUTDIR / f"{name}_imu.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["t_s", "ax", "ay", "az", "gx", "gy", "gz", "led"])
    for t, ax, ay, az, gx, gy, gz, l in samples:
        w.writerow([f"{t - t0:.6f}", f"{ax:.4f}", f"{ay:.4f}", f"{az:.4f}",
                    f"{gx:.4f}", f"{gy:.4f}", f"{gz:.4f}", l])

# ---------- report ----------
n = len(frames)
print(f"\nIMU:   {len(samples)} samples @ {len(samples)/DURATION:.0f} Hz")

if n > 1:
    span = frames[-1][1] - frames[0][1]          # sensor timestamps
    fps_actual = (n - 1) / span
    nominal = 1.0 / FPS
    ivals = [frames[i][1] - frames[i-1][1] for i in range(1, n)]
    dropped = sum(round(iv / nominal) - 1 for iv in ivals if iv > 1.5 * nominal)
    worst = max(ivals)
    print(f"Video: {n} frames over {span:.2f} s @ {fps_actual:.2f} fps "
          f"(target {FPS})")
    print(f"       dropped {dropped}, worst interval {worst*1000:.1f} ms "
          f"(nominal {nominal*1000:.1f} ms)")
    if dropped:
        print("  WARNING: frames were dropped - check velocities against frames CSV.")
else:
    print("Video: too few frames")

print(f"clock offset  median {median_off*1e3:.2f} ms, spread {spread*1e3:.2f} ms")
if abs(median_off) < 0.05:
    print("  -> sensor timestamps share the monotonic clock: t_s columns align directly.")
else:
    print("  -> offset applied to frames CSV; check the LED frame to confirm.")
if t_release is not None:
    print(f"release at t = {t_release - t0:.4f} s")
else:
    print("no freefall detected - check FREEFALL_G")
