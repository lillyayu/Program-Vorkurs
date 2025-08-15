"""
Das 3x+1 Problem ist ein Problem in der Mathematik, bei dem man von einer
beliebigen Zahl ausgeht. Wenn diese ungrade ist, ist die neue Zahl x = 3*x+1,
wenn sie grade ist x = x / 2.
Dieses Problem ist ein gutes Beispiel für eine Anwendung, bei der man wissen
will, ob eine Zahl grade oder ungerade ist.

a) schreibe die Funktion ist_grade_eins_bis_zehn, die für die Zahlen von eins
bis Zehn ausgibt, ob die Zahl grade ist. Benutze hierfür mehrere If-Anweisungen

Zum Beispiel wenn n==1, gebe False zurück, oder wenn n==2, gebe True zurück

b) Offensichtlich ist es sehr ineffizient, für jede Zahl eine einzelne If-
Anweisung zu schreiben. Stattdessen gibt es den Modulo-Operator "%", welcher
den Rest bei einer Division zurückgibt. z.B. 6%5=1.

Benutze den Modulo-Operator in der Funktion ist_grade, um für ein beliebiges n
herauszufinden, ob dieses n grade ist.

c) (nur Bonus - Extra schwer!) Implementiere die Funktion three_x_plus_one,
die solange den oben beschriebenen Algorithmus ausführt, bis die Zahl 1 ist
(1 -> 4 -> 2 -> 1 ist nämlich eine Endlosschleife.)

Zähle, wie oft die Zahl halbiert, bzw. verdreifacht+1 wird und gib den Zähler
am Ende aus. Benutze die ist_grade Funktion um in der Funktion zu entscheiden,
ob die Zahl grade ist.

Schwierigkeit
a) 1/5
b) 2/5
c) 5/5 🔥

"""


def ist_grade_eins_bis_zehn(n: int) -> bool | None:
    """
    Gibt für die n zwischen eins und zehn zurück, ob n grade sind
    Wenn nicht 1<=n<=10, gib None zurück

    >>> ist_grade_eins_bis_zehn(1)
    False
    >>> ist_grade_eins_bis_zehn(2)
    True
    """
    ...


def ist_grade(n: int) -> bool:
    """
    Gibt für ein beliebiges n zurück, ob dieses grade ist

     >>> ist_grade(1)
    False
    >>> ist_grade(2412)
    True
    """
    ...


def three_x_plus_one(n: int):
    """
    Führt den 3x+1 Algorithmus aus, bis eine Endlosschleife erreicht wird.
    Zählt, wie viele Schritte es bis dahin sind.

    >>> three_x_plus_one(1)
    0
    >>> three_x_plus_one(3)
    7
    >>> three_x_plus_one(31)
    106
    """
    ...


if __name__ == "__main__":
    ...
