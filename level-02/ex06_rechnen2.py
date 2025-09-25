import time
"""
a) Was ist die Summe der ersten 10 Quadratzahlen?

Schreibe die Generelle Funktion sum_of_squares, welche die Summe der
Quadratzahlen von x bis y berechnet. (bsp von 5-7: 5^2 + 6^2 + 7^2 = 110)

b) Countdown:
In 10 Sekunden geht das Rennen los! Zähle von x runter und gib jede Sekunde
eine Zahl aus. Statt 0 gibst du "Los gehts!" aus.
Tipp: mit time.sleep(1) kannst du eine Sekunde warten.

c) Algorithmusdivision:
1: Gegeben seien zwei ganze Zahlen a und b.
2: Berechne das Produkt von a und b.
3: Prüfe, ob das Produkt durch 7 teilbar ist. Wenn ja, gib es aus und beende
das Programm.
4: Falls nicht, erhöhe a um 2 und verringere b um 1.
5: Wiederhole Schritt 2.

Schreibe die Funktion "division", welche diesen Algorithmus umsetzt.

"""


def sum_of_squares(x: int, y: int) -> int:
    """
    Berechnet die Summe der Quadratzahlen von x bis y
    >>> sum_of_squares(5, 7)
    110

    """
    summe: int = 0
    for zahl in range(x, y+1):
        summe += zahl**2
    return summe


def countdown(x: int) -> None:
    """
    Zählt von x runter.

    >>> countdown(2)
    2
    1
    Los gehts!
    """
    for zahl in range(x, 0, -1):
        print(zahl)
        time.sleep(1)
    print("Los gehts!")


def division(a: int, b: int) -> int:
    """
    Setzt den oben beschriebenen Algorithmus um

    >>> division(4, 2)
    """
    ...


if __name__ == "__main__":
    countdown(4)
