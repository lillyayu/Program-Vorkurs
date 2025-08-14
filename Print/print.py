"""
In dieser Aufgabe beschäftigen wir uns intensiv mit der print()

a) Gebe alle Ziffern von 0-9, jeweils durch ein Leerzeichen getrennt, aus.
Verwende dafür nur eine Zeile.

b) Gebe alle Ziffern von 0-9, jeweils durch vier "@" getrennt, aus und füge
drei Leerzeilen am Ende ein. Verwende dafür nur eine Zeile.

c) Gebe alle Ziffern von 0-9, jeweils durch eine Zeile mit
50 mal "*" getrennt, aus. Verwende dafür nur eine Zeile.

d) Schreibe ein Programm, welches die in der Funktion print_x gezeigte Ausgabe
erzeugt, jedoch nureinmal den Buchstaben "X" verwendet.

"""


def eins_bis_zehn():
    """
    >>> a1()
    0 1 2 3 4 5 6 7 8 9
    """
    print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


def eins_bis_zehn_at():
    """
    >>> eins_bis_zehn_at()
    0@@@@1@@@@2@@@@3@@@@4@@@@5@@@@6@@@@7@@@@8@@@@9@@@@
    """
    print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, sep="@@@@", end="\n\n\n")


def print_x():
    """
    >>> print_x()
    XXXX
    XXXX
    XXXX
    """
    print(3 * (4 * "X" + "\n"))


if __name__ == "__main__":
    pass
