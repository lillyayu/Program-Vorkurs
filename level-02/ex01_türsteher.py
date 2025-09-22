"""
Im Freiburger Club "Elpi" soll an der Tür entschieden werden, ob eine Person
in den Club kommt. Um in den Club zu kommen, muss man volljährig sein.

a) Schreibe die Funktion "check_age", die das Alter übergeben bekommt und einen
Wahrheitswert zurückgibt, der aussagt ob diese Person ins Elpi kommt oder nicht

b) Schreibe außerdem die Funktion "print_message" die einen Wahrheitswert über-
geben bekommt und der Person sagt, ob sie in den Club kommt.

c) Nun kombiniere die beiden Ersten Funktionen in der Funktion "türsteher", die
die BenutzerIn nach dem Alter fragt und eine Nachricht zurückgibt.

Schwierigkeit:
a) 1/5
b) 1/5
c) 2/5

"""


def check_age(alter: int) -> bool:
    """
    Guckt, ob das alter über 18 ist.

    >>> check_age(19)
    True
    >>> check_age(18)
    True
    >>> check_age(17)
    False
    """
    ...


def print_message(alt_genug: bool) -> None:
    """
    Außerdem will der Türsteher nicht die ganze Zeit das gleiche sagen müssen.
    Um ihm die Arbeit zu erleichtern. Gib je nach Fall entweder:
    "Du bist zu jung!" oder "Herzlich Willkommen!" aus.

    >>> print_message(False)
    "Du bist zu jung!"
    >>> print_message(True)
    "Herzlich Willkommen!"
    """
    ...


def türsteher() -> None:
    """
    Fragt die BenuterIn nach dem Alter und gibt je nach Alter durch die beiden
    anderen Funktionen zurück, ob die Benutzerin in den Club kommt.

    >>> türsteher()
    Wie alt bist du? 19
    Herzlich Willkommen!
    """
    ...


if __name__ == "__main__":
    ...
