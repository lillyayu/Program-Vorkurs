from dataclasses import dataclass
"""
In der letzten Aufgabe habt ihr hoffentlich schon das Prinzip
von Datenklassen verstanden. Wir kommen mit Datenklassen recht
häufig in die Situation, dass wir Datenklassen miteinander
vergleichen oder interagieren lassen wollen.

Dazu dienen uns sogenannte "Dunder"-Methoden. Bei Zahlen haben
wir schon vergleichsoperationen wie ==, <, etc.. kennengelernt.

Eine Bank will die Wichtigkeit ihrer Konten nach Kontostand einordnen.
Dazu muss die Bank schnell in der Lage sein, zwei Konten miteinander zu
vergleichen.

Die Bank hat schon eine Möglichkeit implementiert, um zu schauen, ob
zwei Konten die selbe Kontonr haben. Dazu wurde die __eq__ Dunder-Methode
verwendet. Durch diese können wir nun den Operator "==" verwenden, um
die Gleichheit zweier Konten zu vergleichen, selbst wenn sich die
InhaberIn und der Kontostand ändern.

a) Implementiere die Funktionen __lt__ (lower than / kleiner als) und
__le__ (lower equal / kleiner gleich), welche Überprüfen, ob der Kontostand
kleiner als / kleiner gleich einem anderen Konto ist.

b) Implementiere die Methode __add__, die es erlaubt, zwei Konten mit dem "+"
Operator zu addieren. Das Ergebnis soll ein neues Konto sein, welches denselben
Besitzer wie das erste Konto hat, die Kontonummer "9999" erhält und den
Kontostand als Summe der beiden ursprünglichen Kontostände speichert.


Schwierigkeit:
a) 2/5
b) 3/5

"""


@dataclass
class Konto:
    besitzerin: str
    kontronr: int
    kontostand: float

    def __eq__(self, other: "Konto"):
        """
        Gibt an, ob die Kontonummern gleich sind.

        >>> k1 = Konto("Max Mustermann", 1234, -12.02)
        >>> k2 = Konto("Alex Staub", 1234, 5954.02)
        >>> k1==k2
        True

        """
        return self.kontronr == other.kontronr

    def __lt__(self, other: "Konto") -> bool:
        """
        >>> k1 = Konto("Max Mustermann", 1234, -12.02)
        >>> k2 = Konto("Alex Staub", 1234, 5954.02)
        >>> k1<k2
        True
        >>> k1>k2
        False
        """
        ...

    def __le__(self, other: "Konto") -> bool:
        """
        >>> k1 = Konto("Max Mustermann", 1234, 5954.02)
        >>> k2 = Konto("Alex Staub", 1234, 5954.02)
        >>> k1<=k2
        True
        """
        ...

    def __add__(self, other: "Konto") -> "Konto":
        """
        >>> k1 = Konto("Max Mustermann", 1234, 100.00)
        >>> k2 = Konto("Alex Staub", 5678, 50.00)
        >>> k3 = k1 + k2
        >>> k3.besitzerin
        'Max Mustermann'
        >>> k3.kontostand
        150.0
        """
        ...


if __name__ == "__main__":
    k1 = Konto("Max Mustermann", 1234, 5954.02)
    k2 = Konto("Alex Staub", 1234, 5954.02)
    print(k1 <= k2)
