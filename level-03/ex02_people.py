import doctest
"""
Eddy möchte ein Tool erstellen, welches es den Benutzern ermöglicht, die
Daten aus einer Datenbank, welche dort in Form von dictionaries gespeichert
sind, in einem kompakten und für den Nutzer gut verständlichen Satz
zusammenzufassen.
Außerdem hat sein Kollege neue Daten hinzugefügt, diese aber
leider nicht in Form von dicionaries, sondern in Form von Listen abgespeichert.
Um diese Inkonsistenz zu korrigieren, mussen die Listen in dictionaries
umformatiert werden.

a) Schreibe eine Funktion, welche aus einem dictionary der Person ihr
    Geburstdatum, Alter, Lieblingstier und Größe extrahiert, und einen Satz
    zurückgibt, welcher diese zusammenfasst.

b) Schreibe eine Funktion, welche aus einer Liste mit den Informationen der
    Person ein dictionary erstellt, in dem die Informationen einer
    Informationsklasse zugeordnet sind.

Schwierigkeit:
a) 3/5
b) 4/5

"""


def a(person: dict[str, str]) -> str:
    """
    Aus dem dictionary "person" sollen die Informationen extrahiert werden,
    und als Satz formuliert ausgegeben werden.

    >>> a({"name": "Julia", "birthdate": "11.06.2004", "animal": "Hund",
    ... "height": 1.62})
    'Julia hat am 11.06.2004 Geburstag, ist 1.62m groß und hat das \
Lieblingstier Hund.'
    """
    ...


def b(person: list[str]) -> dict[str, str]:
    """
    Aus der Liste "person" sollen die Informationen in ein dictionary
    umgeformt werden, welches am Ende zurückgegeben wird.

    >>> b(["Julia", "11.06.2004", "Hund", "1,62"])
    {'name': 'Julia', 'birthdate': '11.06.2004',
    ... 'animal': 'Hund', 'height': '1,62'}
    """
    ...


if __name__ == "__main__":
    doctest.testmod()
    person = {"name": "Julia", "birthdate": "11.06.2004", "animal": "Hund",
              "height": "1,62"}
    assert a(person) == (
        "Julia hat am 11.06.2004 Geburstag, ist 1,62m groß"
        " und hat das Lieblingstier Hund.")
    assert b(["Julia", "11.06.2004", "Hund", "1,62"]) == (
        {"name": "Julia", "birthdate": "11.06.2004", "animal": "Hund",
         "height": "1,62"}
    )
