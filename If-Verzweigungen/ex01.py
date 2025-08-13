"""
Im Freiburger Club "Elpi" soll an der Tür entschieden werden, ob eine Person
in den Club kommt. Um in den Club zu kommen, muss man volljährig sein.

Schreibe die Funktion "check_age" zuende, die das Alter übergeben bekommt und
 einen Wahrheitswert zurückgibt, der aussagt ob diese Person ins Elpi kommt.
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
    pass


if __name__ == "__main__":
    check_age(5)
