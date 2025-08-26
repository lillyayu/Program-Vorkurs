import doctest
"""
1784 wurde Carl Friedrich Gauß von seinem Lehrer gefragt, die ersten 100
natürlichen Zahlen zu addieren. Gauß hat sich einen intelligenten Algorithmus
ausgedacht, statt die Zahlen stumpf zu Addieren.
Zum Glück haben wir heute Rechenleistung und wir können die Zahlen wieder
stumpf addieren.

Gauß hat damals die Formel 1+2+...+100 = (100*101)/2 herausgefunden.

a) Schribe die Funktion "gauss_formel", welche die Formel von Gauss benutzt,
um die Summe der ersten "n" Zahlen zurückzugeben.

b) Schribe die Funktion "gauss_formel", welche eine For-Schleife benutzt,
um die Summe der ersten "n" Zahlen zurückzugeben.

c) Bonus (schwierig): Schreibe die Funktion "gauss_list", die eine Liste von
ganzen Zahlen bekommt und die Summe von der gauss-formel von jeder Zahl in der
Liste zurückgibt (Beispiel: [1, 3, 4] = 1 + 6 + 10 = 17)

Schwierigkeit:
a) 1/5
b) 2/5
c) 4/5 🌶️
"""


def gauss_formel(n: int) -> int:
    """
    Berechnet durch die Gauss-Formel die Summe der ersten "n" Zahlen.

    >>> gauss_formel(100)
    5050
    >>> gauss_formel(1000)
    500500
    >>> gauss_formel(456)
    104196
    """
    ...


def add_n_numbers(n: int) -> int:
    """
    Addiert mit einer For-Schleife die Summe der ersten "n"-Zahlen.

    >>> add_n_numbers(100)
    5050
    >>> add_n_numbers(100)
    500500
    >>> add_n_numbers(456)
    104196
    """
    ...


def gauss_list(liste: list[int]) -> int:
    """
    >>> gauss_list([1, 3, 4])
    17
    >>> gauss_list([100, 1000])
    505550
    """
    ...


if __name__ == "__main__":
    doctest.testmod()
    print(gauss_formel(456))
