########################################################################
# Aufgabe 1: Schreibe alle Ziffern, jeweils durch ein Leerzeichen getrennt, auf. Verwende dafür nur eine Zeile.

def a1():
    """
    >>> a1()
    0 1 2 3 4 5 6 7 8 9
    """
    print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
########################################################################
# Aufgabe 2: Schreibe alle Ziffern, jeweils durch vier "@" getrennt, auf, und füge drei Leerzeilen am Ende ein. Verwende dafür nur eine Zeile.

########################################################################
# Aufgabe 3: Schreibe alle Ziffern, jeweils durch eine Zeile mit 50 mal "*" getrennt, auf. Verwende dafür nur eine Zeile.

########################################################################
# Aufgabe 3: Schreibe ein Programm, welches die selbe Ausgabe erzeugt, jedoch nur einmal den Buchstaben "X" verwendet


def a3():
    """
    >>> a3()
    XXXX
    XXXX
    XXXX
    """
    print()

########################################################################
if __name__ == "__main__":

    # Aufgabe 1
    print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    # Aufgabe 2
    print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, sep=4 * "@", end="\n\n\n")
    print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, sep="@@@@", end="\n\n\n")
    # Aufgabe 3
    print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, sep="\n" + 50 * "*" + "\n")
    # Aufgabe X"
    print(3 * (4 * "X" + "\n"))
