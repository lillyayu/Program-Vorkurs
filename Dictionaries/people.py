"""
Eddy möchte ein Tool erstellen, welches es den Benutzern ermöglicht, die
Daten aus einer Datenbank, welche dort in Form von dictionaries gespeichert
sind, in einem kompakten Satz zusammenzufassen. Außerdem hat sein Kollege
neue Daten hinzugefügt, diese aber leider nicht in Form von dicionaries,
sondern in Form von Listen abgespeichert. D

a) Schreibe eine Funktion, welche aus einem dictionary der Person ihr
    Geburstdatum, Alter, Lieblingstier und Größe extrahiert, und einen Satz
    zurückgibt, welcher diese zusammenfasst.
b) Schreibe eine Funktion, welche aus einer Liste mit den Informationen der
    Person ein dictionary erstellt, in dem die Informationen einer
    Informationsklasse zugeordnet sind.  """


def a(person: dict[str, str]) -> str:
    """
    Aus dem dictionary "person" sollen die Informationen extrahiert werden,
    und als Satz formuliert ausgegeben werden.
    >>> a({"name": "Julia", "birthdate": "11.06.2004", "animal": "Hund",
    ... "height": 1.62})
    'Julia hat am 11.06.2004 Geburstag, ist 1.62m groß und hat das \
Lieblingstier Hund.'
    """
    pass


# def b(person: list[str]) -> dict[str, str]:
#    """
#    Aus der Liste "person" sollen die Informationen in ein dictionary
#    umgeformt werden, welches am Ende zurückgegeben wird.
#    >>> b(["Julia", "11.06.2004", "Hund", "1,62"])
#    {'name': 'Julia', 'birthdate': '11.06.2004',
#    ... 'animal': 'Hund', 'height': '1,62'}"""
#    pass


if __name__ == "__main__":
    person = {"name": "Julia", "birthdate": "11.06.2004", "animal": "Hund",
              "height": "1,62"}
    assert a(person) == "Julia hat am 11.06.2004 Geburstag, ist 1,62m groß und hat das Lieblingstier Hund."


""" Lösungen:
a) return person["name"] + " hat am " + person["birthdate"] + " Geburstag, ist " + str(person["height"]) + "m groß und hat das Lieblingstier " + person["animal"] + "."

b)  dic = dict()
    dic["name"], dic["birthdate"],dic["animal"], dic["height"] = person[0], person[1], person[2], person[3] 
    return dic"""
