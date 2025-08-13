from random import randint
"""
Eine While Schleife ist eine Schleife, die den Inhalt des eingerückten Blocks
so lange ausführt, wie eine Bedinung erfüllt ist. "while True:" erzeugt
beispielsweise eine Endlosschleife, das True immer wahr ist.

a) Eine normale Anwendung für while wäre eine Schleife, die die BenutzerIn
so lange nach dem Passwort fragt, bis sie es eingibt.
Schreibe die Funktion "require_password", welche genau dies tut.

b) Ratespiel: Schreibe die Funktion "guess_number", bei der die BenutzerIn eine
zufällige Zahl von 1 bis n erraten muss und zähle die Versuche, die sie braucht

Schwierigkeit
a) 3/5
b) 4/5
"""


def require_password(password: str) -> None:
    """
    Fragt so lange mit input nach dem Passwort, bis die BenutzerIn es eingibt.
    """
    pass


def guess_number(n: int) -> None:
    """
    Lässt die BenutzerIn so lange raten, bis die zufällige Zahl erreicht wurde.
    Dabei zählt die Funktion mit, wie viele Versuche gebraucht werden.

    Hinweis:
    random = randint(1, n) generiert eine zufällige Zahl von 1 bis n
    """
    random: int = randint(1, n)
    pass


if __name__ == "__main__":
    require_password("DiesesPasswortIstSicher123")
    guess_number(10)
