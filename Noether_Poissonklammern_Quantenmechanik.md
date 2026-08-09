# Erhaltungsgrößen, Noether-Theorem und der Übergang zur Quantenmechanik

 Vorausgesetzt werden Lagrange- und Hamilton-Formalismus (verallgemeinerte Koordinaten, Euler-Lagrange-Gleichungen, kanonisch konjugierter Impuls $p_i = \partial L/\partial \dot x_i$, Hamiltonfunktion $H=\sum_i p_i\dot x_i - L$).

**Quelle:** Dieses Arbeitsblatt folgt eng M. Bartelmann, *Theoretische Physik I: Mechanik* (im Folgenden **TP I**), Kap. 12, 13.2.3 und 13.3, sowie *Theoretische Physik II: Analytische Mechanik* (**TP II**), Kap. 5–6. Die Gleichungsnummern in eckigen Klammern verweisen auf die dortige Nummerierung. Schaut aber erst nach, wenn ihr selbst fertig seid oder wirklich feststeckt.

**Aufbau:** Teil 1 sammelt vier konkrete Erhaltungsgrößen aus der Galilei-Invarianz. Das allgemeine Rezept dafür wird euch zunächst nur gegeben, nicht bewiesen. Teil 2 liefert den Beweis dieses Rezepts (das eigentliche Noether-Theorem) über die Variation der Wirkung. Teil 3 übersetzt denselben Sachverhalt in die Sprache der Poisson-Klammern. Teil 4 ersetzt die Poisson-Klammer durch den Kommutator und landet bei der Quantenmechanik.

---

## Teil 1: Erhaltungsgrößen aus der Galilei-Invarianz

### 1.1 Ausgangssystem

Betrachtet $N$ Massenpunkte mit paarweisen Potentialkräften, sodass
$$L(\vec x,\dot{\vec x},t) = \sum_{i=1}^N \frac{m_i}{2}\dot{\vec x}_i^{2} - \sum_{i<j} V_{ji}(|\vec x_i-\vec x_j|)$$
gilt (vgl. die Lagrangefunktion $L=T-V$ vor TP I 12.1/TP II 5.1, aus der die dort angegebenen Bewegungsgleichungen folgen). Ein Beobachter sitzt in einem abgeschlossenen, kräftefrei bewegten Kasten und prüft, welche Bewegungen des Kastens er *nicht* nachweisen kann. Genau diese Bewegungen sind Symmetrien der Mechanik.

### 1.2 Warum $R$ konstant sein muss

Die allgemeinste denkbare Transformation zwischen dem Kasten (ungestrichen) und einem Fixsternsystem (gestrichen) lautet
$$t^{\prime} = t+\tau, \qquad \vec{x}^{\prime} = \vec a(t) + R(t)\vec x$$

**Aufgabe 1.** Begründet physikalisch (nicht rechnerisch), warum $R(t)$ **zeitlich konstant** sein muss, damit der Beobachter im Kasten keine Scheinkräfte feststellt. *(Zum Beispiel beim Foucault'sches Pendel. Was würde eine zeitabhängige Drehung $R(t)$ dort bewirken?)*

Ab jetzt gilt also $R=\text{const}$, und mit $\vec a(t)=\vec a_0+\vec v t$ (die allgemeinste Form, die ihr in Aufgabe 2 nachprüft) bleiben zehn freie Parameter: $\tau$, drei in $\vec a_0$, drei in $\vec v$, drei in $R$.

### 1.3 Die Lagrangefunktion ändert sich nur um eine totale Zeitableitung

**Aufgabe 2.** Setzt $t^{\prime}=t+\tau$, $\vec x_i^{\prime} = \vec a_0+\vec v t + R\vec x_i$ mit konstantem $R,\vec v,\vec a_0$ in die Lagrangefunktion des Fixsternsystems ein und zeigt
$$L(\vec x^{\prime},\dot{\vec x}^{\prime},t^{\prime}) = L(\vec x,\dot{\vec x},t) + \frac{\mathrm d f(\vec x,t)}{\mathrm dt}, \qquad f(\vec x,t) = \vec v^{\top}\sum_{i=1}^N m_iR\vec x_i + \frac{\vec v^{2}t}{2}\sum_{i=1}^N m_i$$
*(Hinweis: Die kinetische Energie ist unter der zeitunabhängigen Drehung $R$ ohnehin invariant; der einzige nichttriviale Teil kommt von der Geschwindigkeitsverschiebung $\dot{\vec x}^{\prime} = \vec v + R\dot{\vec x}$.)* [vgl. TP I 12.5–12.10 bzw. TP II 5.3–5.9]

### 1.4 Das Rezept (Beweis folgt in Teil 2)

> **Noether-Theorem, vorläufige Fassung.** Ändert eine infinitesimale Transformation $\delta t$, $\delta\vec x_i$ die Lagrangefunktion nur um eine totale Zeitableitung, $L\to L+\dot f$, dann ist
> $$\sum_{i=1}^N \vec p_i\cdot\delta\vec x_i \;-\; H\,\delta t \;-\; f(\delta\vec x,\delta t) \;=\;\text{const.}$$
> entlang jeder Bahn, wobei $f(\delta\vec x,\delta t):=\sum_i\frac{\partial f}{\partial \vec x_i}\cdot\delta\vec x_i + \frac{\partial f}{\partial t}\delta t$ das totale Differential von $f(\vec x,t)$ ist, ausgewertet mit den infinitesimalen Größen $\delta\vec x_i,\delta t$ der Transformation, **nicht** $f$ an einer verschobenen Stelle.

### 1.5 Vier Symmetrien, vier Erhaltungsgrößen

**Aufgabe 3.** Wendet das Rezept aus 1.4 auf jede der folgenden vier Ein-Parameter-Untergruppen der Galilei-Gruppe an (die übrigen neun Parameter jeweils auf null gesetzt) und bestimmt die zugehörige Erhaltungsgröße. Nutzt dabei euer $f$ aus Aufgabe 2.

  (a) **Zeittranslation:** $\delta t=\tau\neq0$, $\delta\vec x_i=0$. Zeigt $H=\text{const}$: *Energieerhaltung.*

  (b) **Ortstranslation:** $\delta t=0$, $\delta\vec x_i=\delta\vec a$ (für alle $i$ gleich). Zeigt $\sum_i \vec p_i = \text{const}$: *Impulserhaltung.*

  (c) **Boost:** $\delta t=0$, $\delta\vec x_i = \delta\vec v\, t$. Zeigt
  $$\delta\vec v^{\top}\Big(t\sum_i\vec p_i - \sum_i m_i\vec x_i\Big) = \text{const} \implies \vec X = \frac{1}{M}\sum_i m_i\vec x_i = \vec X_0 + \frac{t}{M}\sum_i \vec p_i$$
  also *geradlinig-gleichförmige Bewegung des Schwerpunkts.*

  (d) **Drehung:** $\delta t=0$, $\delta\vec x_i = \delta\vec\varphi\times\vec x_i$. Zeigt $\vec L=\sum_i \vec x_i\times\vec p_i = \text{const}$: *Drehimpulserhaltung.*

*(Alle vier Rechnungen lassen sich gegenprüfen in TP I 12.24–12.30 bzw. TP II 5.23–5.29 — die Energieerhaltung aus Fall (a) selbst bekommt dort keine eigene Gleichungsnummer, sondern folgt direkt und ohne Umweg aus der allgemeinen Formel am Anfang dieses Bereichs.)*

---

## Teil 2: Allgemeine Herleitung des Noether-Theorems anhand der Wirkung

Jetzt beweisen wir das Rezept aus 1.4 für eine *beliebige* infinitesimale Transformation $t\to t^{\prime}=t+\delta t$, $\vec x_i(t)\to\vec x_i^{\prime}(t^{\prime}) = \vec x_i(t)+\delta\vec x_i(t)$ mit $L(\vec x^{\prime},\dot{\vec x}^{\prime},t^{\prime}) = L(\vec x,\dot{\vec x},t)+\dot f(\vec x,t)$, $\delta t=\text{const}$.

**Aufgabe 4.** Zeigt, dass sich das Wirkungsintegral im gestrichenen System als
$$S^{\prime} = \int_{t_0^{\prime}}^{t_1^{\prime}} L^{\prime}\,\mathrm dt^{\prime} = S + f(\vec x,t)\Big|_{t_0}^{t_1}$$
schreiben lässt, indem ihr $L^{\prime}=L+\dot f$ direkt einsetzt und die Integrationsgrenzen $t_0^{\prime}=t_0+\delta t$, $t_1^{\prime}=t_1+\delta t$ beachtet. [TP I 12.15/TP II 5.13]

**Aufgabe 5.** Entwickelt andererseits $S^{\prime}$ ausgehend von der linken Seite direkt: Setzt $L^{\prime}=L(\vec x^{\prime}-\dot{\vec x}^{\prime}\delta t + \dots,\dots)$ in Taylorreihe an, integriert den Term mit $\partial L/\partial\dot x_i$ partiell und benutzt die Euler-Lagrange-Gleichungen, um alle Terme innerhalb des Integrals zum Verschwinden zu bringen. Ihr solltet auf
$$S^{\prime} = S + \left[\sum_{i=1}^N \frac{\partial L}{\partial \dot x_i}(\vec x_i^{\prime}-\vec x_i) + \delta t\, L\right]_{t_0}^{t_1}$$
kommen. [TP I 12.16–12.18/TP II 5.14–5.16]

**Aufgabe 6.** Nutzt die Taylor-Beziehung $\vec x_i^{\prime}(t) = \vec x_i(t) - \dot{\vec x}_i(t)\,\delta t + \delta\vec x_i$ (Vorsicht: das ist *nicht* dasselbe wie $\vec x_i^{\prime}(t^{\prime})-\vec x_i(t)=\delta\vec x_i$; macht euch den Unterschied klar!), um die eckige Klammer aus Aufgabe 5 mithilfe von $p_i=\partial L/\partial\dot x_i$ und $H=\sum_i p_i\dot x_i - L$ in die Form
$$S^{\prime} = S + \Big[\sum_i \vec p_i\cdot\delta\vec x_i - H\,\delta t\Big]_{t_0}^{t_1}$$
zu bringen. [TP I 12.19–12.22/TP II 5.17–5.21 — TP II schreibt dieses Zwischenergebnis explizit als eigene Gleichung (5.21) an, TP I fasst es direkt mit dem nächsten Schritt zusammen]

**Aufgabe 7.** Vergleicht die Ergebnisse aus Aufgabe 4 und Aufgabe 6, beide sind Ausdrücke für dasselbe $S^{\prime}$. Folgert, dass
$$\Big[\sum_i \vec p_i\cdot\delta\vec x_i - H\,\delta t - f(\delta\vec x,\delta t)\Big]_{t_0}^{t_1} = 0$$
gelten muss, und dass daraus wegen der Beliebigkeit von $t_0,t_1$ folgt, dass der Ausdruck in eckigen Klammern eine **Erhaltungsgröße** ist. Das ist exakt das Rezept aus 1.4, jetzt bewiesen. [TP I 12.23–12.24/TP II 5.22–5.23]

---

## Teil 3: Noether-Theorem mit Poisson-Klammern

Wir übersetzen dasselbe Resultat jetzt in den Hamilton-Formalismus. Erinnerung an die Poisson-Klammer, in der Konvention von TP I:
$$\{f,g\} := \sum_{i=1}^f\left(\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i} - \frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}\right)\,,\qquad \dot q_i=\{H,q_i\}\,,\quad \dot p_i=\{H,p_i\}\,.$$
[TP I 13.62 & 13.65]

**Konventionsfalle:** TP II definiert dieselbe Klammer in Gl. 6.82 mit **vertauschten** Termen, $\{f,g\}_{TP\,II} := \sum(\partial f/\partial q_i\,\partial g/\partial p_i - \partial f/\partial p_i\,\partial g/\partial q_i)$ — das ist exakt das Negative der obigen Definition, und Bartelmann weist in TP II (Randbemerkung zu 6.82) selbst darauf hin. Auch die kanonischen Gleichungen stehen dort seitenverkehrt, $\dot q_i=\{q_i,H\}_{TP\,II}$. Wir folgen ab hier durchgehend der **TP-I-Konvention** oben. Behaltet das im Kopf, falls ihr in TP II nachschlagt.

**Aufgabe 8 (Aufwärmen).** Berechnet $\{q_i,p_j\}$ und $\{p_i,q_j\}$ direkt aus der Definition. *(Ergebnis nicht das, was ihr vielleicht aus den meisten QM-Lehrbüchern kennt, behaltet das im Hinterkopf für Teil 4!)*

**Aufgabe 9.** Sei $G(q,p,t)$ eine beliebige Phasenraumfunktion (nicht notwendig erhalten). Leitet mit der Kettenregel und den Hamilton'schen Gleichungen $\dot q_i=\partial H/\partial p_i$, $\dot p_i=-\partial H/\partial q_i$ her, dass entlang jeder Bahn
$$\frac{\mathrm dG}{\mathrm dt} = \frac{\partial G}{\partial t} + \{H,G\}$$
gilt. *(Das ist dieselbe Rechnung, mit der Bartelmann die Kontinuitätsgleichung für die Phasenraumdichte $\rho$ herleitet [TP I 13.61/TP II 6.81], nur jetzt für ein allgemeines $G$ statt $\rho$.)* Prüft: Für $G=q_i$ sollte genau $\dot q_i=\{H,q_i\}$ herauskommen.

**Aufgabe 10 (Korollar).** Folgert: Eine zeitunabhängige Größe $G(q,p)$ ist genau dann erhalten, wenn $\{H,G\}=0$ gilt (äquivalent $\{G,H\}=0$, wegen Antisymmetrie $\{f,g\}=-\{g,f\}$).

### Erzeugende Funktionen

Zu jeder Phasenraumfunktion $G$ gehört eine infinitesimale Transformation
$$\delta q_i := \varepsilon\{G,q_i\}\,,\qquad \delta p_i := \varepsilon\{G,p_i\}\,.$$
(Das ist dieselbe Struktur wie $\dot q_i=\{H,q_i\}$, nur mit $G$ statt $H$ und $\varepsilon$ statt $\mathrm dt$: $H$ erzeugt die Zeitentwicklung, $G$ erzeugt eine andere Transformation.)

**Aufgabe 11.**
  (a) Zeigt, dass für jede Phasenraumfunktion $F(q,p)$ gilt: $\delta F = \varepsilon\{G,F\}$ (Kettenregel + Definition oben).
  (b) Sei $G=p_x$ (eine kartesische Impulskomponente). Zeigt, dass die erzeugte Transformation genau eine Verschiebung in $x$-Richtung um $\varepsilon$ ist, und dass dabei kein Impuls sich ändert.
  (c) Sei $G=L_z := x p_y - y p_x$. Zeigt, dass die erzeugte Transformation genau eine infinitesimale Drehung um die $z$-Achse mit Winkel $\varepsilon$ ist ($\delta x=-\varepsilon y$, $\delta y=\varepsilon x$).

**Aufgabe 12.** Nutzt Teil (a) aus Aufgabe 11 mit $F=H$, um $\delta H = \varepsilon\{G,H\}$ zu zeigen. Folgert: $H$ ist genau dann invariant unter der von $G$ erzeugten Transformation, wenn $\{G,H\}=0$. Vergleicht das mit Aufgabe 10: welche Beobachtung macht ihr? *(Erwartet: dieselbe Bedingung $\{G,H\}=0$ entscheidet sowohl über Symmetrie als auch über Erhaltung. Symmetrie-Erzeuger und Erhaltungsgröße sind ein und dasselbe Objekt.)*

**Aufgabe 13.** Ordnet den vier Erhaltungsgrößen aus Teil 1 jeweils zu, welche Transformation sie im Sinne von Aufgabe 11/12 erzeugen ($H$, $\vec p$, $\vec L$; was ist mit der Schwerpunktsgröße aus 1.5(c)? Warum ist deren Fall subtiler als die anderen drei?).

---

## Teil 4: Quantenmechanik als neue Poisson-Klammer

Bartelmann merkt in TP I (13.3.2, letzter Satz) knapp an, dass die Poisson-Klammer-Form der Hamilton'schen Gleichungen *"grundlegend für die Heisenbergsche Formulierung der Quantenmechanik"* wurde. In TP II (6.4.2, letzter Absatz) führt er das genauer aus: dort *"werden sie grundlegend für die Heisenberg'sche Formulierung der Quantenmechanik, wo die Poisson-Klammer durch den Kommutator der entsprechenden quantenmechanischen Operatoren ersetzt wird"*. Das arbeiten wir jetzt aus.

### 4.1 Diracs Korrespondenzregel

**Postulat (Dirac, 1925):** Observablen werden zu hermiteschen Operatoren, und es gibt eine Konstante $c$, sodass für alle $f,g$
$$[\hat f,\hat g] = c\cdot\{f,g\}\cdot\mathbb 1$$
gilt (die Poisson-Klammer wird zum Kommutator, bis auf einen festen Faktor).

**Aufgabe 14.** Aus der Quantenmechanik ist die Heisenbergsche Vertauschungsrelation $[\hat q_i,\hat p_j]=\mathrm i\hbar\,\delta_{ij}$ bekannt. Bestimmt damit und eurem Ergebnis $\{q_i,p_j\}$ aus Aufgabe 8 die Konstante $c$ in obigem Postulat. *(Achtung: wegen Bartelmanns Vorzeichenkonvention der Poisson-Klammer kommt hier nicht einfach $c=1/(\mathrm i\hbar)$ heraus; findet das richtige Vorzeichen selbst!)*

### 4.2 Die Heisenberg'sche Bewegungsgleichung

**Aufgabe 15.** Wendet euer Ergebnis aus Aufgabe 14 auf die klassische Identität aus Aufgabe 9, $\mathrm dG/\mathrm dt = \partial G/\partial t + \{H,G\}$, an (ersetzt $G\to\hat A$, $H\to\hat H$, und die Poisson-Klammer gemäß eurer Korrespondenzregel durch den passenden Kommutator). Zeigt, dass sich die **Heisenberg'sche Bewegungsgleichung**
$$\frac{\mathrm d\hat A}{\mathrm dt} = \frac{\partial \hat A}{\partial t} + \frac{\mathrm i}{\hbar}[\hat H,\hat A]$$
ergibt: die Bewegungsgleichung, die eventuell aus einer QM-Vorlesung bekannt ist, jetzt aber direkt aus Teil 3 hergeleitet statt postuliert.

### 4.3 Erhaltung in der Quantenmechanik

**Aufgabe 16.** Folgert aus 4.2 das quantenmechanische Analogon zu Aufgabe 10: Eine zeitunabhängige Observable $\hat A$ ist genau dann eine Erhaltungsgröße (im Heisenberg-Bild), wenn $[\hat H,\hat A]=0$ gilt.

### 4.4 Reflexionsfragen

1. In Aufgabe 11 habt ihr gezeigt, dass $p_x$ klassisch Translationen und $L_z$ Drehungen *erzeugt*. In der Quantenmechanik erzeugt der Operator $\hat p_x$ Translationen über den unitären Operator $\exp(\mathrm i\hat p_x a/\hbar)$. Vergleicht diese Struktur mit der klassischen $\delta q_i=\varepsilon\{G,q_i\}$ aus Teil 3: was ist die Rolle von $\varepsilon$ vs. $a/\hbar$, was die Rolle von $\{G,\cdot\}$ vs. $\frac{\mathrm i}{\hbar}[\hat G,\cdot]$?
2. $[\hat q,\hat p]=\mathrm i\hbar\neq0$ bedeutet, dass Ort und Impuls nicht gleichzeitig scharf messbar sind (Heisenbergsche Unschärferelation). Was wäre anders, wenn in Teil 1–3 gezeigt hättet, dass $\{q,p\}=0$ gilt statt $\{q,p\}=\pm1$? Wieso *musste* die Korrespondenzregel in Aufgabe 14 zwangsläufig einen von null verschiedenen Kommutator liefern?
3. Stellt die klassische Aussage "$G$ erhalten $\Leftrightarrow\{G,H\}=0$" (Aufgabe 10/12) und die quantenmechanische Aussage "$\hat A$ erhalten $\Leftrightarrow[\hat A,\hat H]=0$" (Aufgabe 16) nebeneinander. Was ist strukturell identisch, was ist rein formal verschieden?

---

## Ausblick (optional)

Bartelmann leitet die Schrödingergleichung an einer ganz anderen Stelle noch einmal her, nicht über Poisson-Klammern, sondern über die **Hamilton-Jacobi-Theorie** und eine Analogie zur geometrischen Optik (Eikonalfunktion $\Phi$, Ansatz $\psi=\exp(\mathrm i\Phi/\hbar)$) [TP I 13.2.3, Gl. 13.49–13.50]. Lest euch diesen Abschnitt durch und vergleicht: Was haben die beiden Zugänge zur Quantisierung (Poisson-Klammer $\to$ Kommutator hier in Teil 4, versus Hamilton-Jacobi $\to$ Wellenfunktion dort) gemeinsam, und was ist grundverschieden an der Vorgehensweise?
