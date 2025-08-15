"""
In dieser Aufgabe beschäftigen wir uns intensiv mit der print()

a) Gebe alle Ziffern von 1-9, jeweils durch ein Leerzeichen getrennt, aus.
Verwende dafür nur eine Zeile.

b) Gebe alle Ziffern von 1-9, jeweils durch vier "@" getrennt, aus und füge
drei Leerzeilen am Ende ein. Verwende dafür nur eine Zeile.

c) Gebe alle Ziffern von 1-5, jeweils durch eine Zeile mit
10 mal "*" getrennt, aus. Verwende dafür nur eine Zeile.

d) Schreibe ein Programm, welches die in der Funktion print_x gezeigte Ausgabe
erzeugt, jedoch nureinmal den Buchstaben "X" verwendet.

Schwierigkeit:
a) 1/5
b) 2/5
c) 2/5
d) 3/5

"""


def eins_bis_neun():
    """
    >>> eins_bis_neun()
    1 2 3 4 5 6 7 8 9
    """
    ...


def eins_bis_neun_at():
    """
    >>> eins_bis_neun_at()
    1@@@@2@@@@3@@@@4@@@@5@@@@6@@@@7@@@@8@@@@9
    <BLANKLINE>
    <BLANKLINE>
    """
    ...


def eins_bis_fünf_stern():
    """
     >>> eins_bis_fünf_stern()
     1
     **********
     2
     **********
     3
     **********
     4
     **********
     5
    """
    ...


def print_x():
    """
    >>> print_x()
    XXXX
    XXXX
    XXXX
    <BLANKLINE>
    """
    ...


if __name__ == "__main__":
    eins_bis_neun()
    eins_bis_neun_at()
    eins_bis_fünf_stern()
    print_x()
