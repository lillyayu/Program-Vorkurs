"""
In dieser Aufgabe beschäftigen wir uns mit der ursprünglichen Aufgabe von
Computern: Dem Rechnen.

Dafür könnt ihr die Rechnenaufgaben einfach ausgeben (wie 2+2 unten).

a) Was ist 9382 mal 23?

b) Was ist der Rest bei 9382 durch 23?

c) Berechne den Durchschnitt von 12, 7 und 23.

Wie sieht die Aufgabe generell aus? Schreibe die Funktion "durchschnitt",
welche den Durchschnitt von 3 beliebigen Ganzzahlen als Kommazahl zurückgibt.

d) Abgerundeter Durchschnitt: Nun wollen wir eine Ganzzahl, keine Kommazahl,
als Durchschnitt. Schreibe abgerundeter Durchschnitt, welche den Durch-
schnitt von 3 Zahlen abgerundet zurückgibt.

e) Satz den Pythagoras:
a quadrat + b quadrat = c quadrat
a und b sind als Argumente gegeben. Schreibe die Funktion "pythagoras",
die mit "return" "c" (nicht c^2) zurückgibt.

Tipp: Die Wurzel ist das selbe wie hoch 0.5

Schwierigkeit
a) 1/5
b) 1/5
c) 1/5
d) 2/5 💡
e) 2/5

"""


def durchschnitt(a: int, b: int, c: int) -> float:
    """
    Gibt den Durchschnitt von drei beliebigen Zahlen zurück

    >>> durchschnitt(3, 4, 5)
    4.0
    """
    ...


def abgerundeter_durchschnitt(a: int, b: int, c: int) -> int:
    """
    Gibt den abgerundeten Durchschnitt von drei beliebigen Zahlen zurück

    >>> abgerundeter_durchschnitt(3, 4, 5)
    4
    """
    ...


def pythagoras(a: int, b: int) -> float:
    """
    Gibt mit dem Satz des Pythagoras c zurück

    >>> pythagoras(3, 4)
    5.0
    """
    ...


if __name__ == "__main__":
    print(2+2)
    print(pythagoras(3, 4))
