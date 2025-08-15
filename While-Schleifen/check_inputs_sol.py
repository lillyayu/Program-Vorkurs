from random import randint
"""
Eine While Schleife ist eine Schleife, die den Inhalt des eingerückten Blocks
so lange ausführt, wie eine Bedinung erfüllt ist. "while True:" erzeugt
beispielsweise eine Endlosschleife, weil True ja immer wahr ist.

a) Eine normale Anwendung für while wäre eine Schleife, die die BenutzerIn
so lange nach einem Passwort fragt, bis sie es richtig eingibt.
Schreibe die Funktion "require_password", welche genau dies tut.

b) Ratespiel: Schreibe die Funktion "guess_number", bei der die BenutzerIn
eine zufällige Zahl von 1 bis n erraten muss und die zählt, wie viele
Versuche sie dafür braucht

Schwierigkeit
a) 2/5
b) 3/5

"""


def require_password(password: str) -> None:
    """
    Fragt so lange mit input nach dem Passwort, bis die BenutzerIn es eingibt.

    Die Ausgabe soll beispielsweise so aussehen: (ohne die ----)
    ------------
    Passwort? DiesesPasswort124
    Falsch. Passwort? DiesesPasswortIstSicher123
    Zugriff erlaubt!
    -----------
    """
    password_input: str = input("Passwort? ")
    while not password_input == password:
        password_input = input("Falsch. Passwort? ")
    print("Zugriff erlaubt!")


def guess_number(n: int) -> None:
    """
    Lässt die BenutzerIn so lange raten, bis die zufällige Zahl erreicht wurde.
    Dabei zählt die Funktion mit, wie viele Versuche gebraucht werden.

    Hinweis:
    random = randint(1, n) generiert eine zufällige Zahl von 1 bis n

    Die Augabe soll beispielsweise so aussehen: (ohne die ----)
    ----
    Errate die Zahl: 3
    Errate die Zahl: 4
    Errate die Zahl: 1
    Richtig! Die Zahl war: 1. Du hast 3 Versuche gebraucht!
    ----
    """
    random_number: int = randint(1, n)
    number_guesses: int = 0
    guess: int = int(input("Errate die Zahl: "))
    while not guess == random_number:
        number_guesses += 1
        guess = int(input("Nicht ganz. Errate die Zahl: "))
    print("Richtig! Die Zahl war: " + str(random_number) + ". Du hast " +
          str(number_guesses) + " Versuche gebraucht!")


if __name__ == "__main__":
    require_password("DiesesPasswortIstSicher123")
    guess_number(10)
