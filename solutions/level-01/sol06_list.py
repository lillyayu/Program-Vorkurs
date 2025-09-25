"""
Achtung, wenn ihr doctests benutzt funktionieren diese hier wegen input nicht

a) Schreibe ein Funktion, die aus einer vom Benutzer eingegebenen Zeichenkette
eine Liste erstellt, in der jedes Zeichen der Zeichenkette einen Listeneintrag
darstellt.

b) Schreibe eine Funktion, welche vom Benutzer eine Zahl fordert, und
anschließend den im Alphabet der Zahl entsprechenden Buchstaben zurückgibt.

c) Schreibe eine Funktion, welche nacheinander drei Zahlen vom Benutzer
fordert, die entsprechenden Buchstaben in einer Liste "memory" speichert
und diese am Ende zurückgibt.

d) Schreibe eine Funktion, die die zwei Zahlen vom Benutzer fordert (wir gehen
davon aus, dass die zweite Zahl größer ist als die erste und alle Zahlen
kleiner 27 sind) und den entsprechenden Listenabschnitte aus der Liste
"alphabet" zurückgibt (die den vom Benutzer gegebenen Zahlen entprechenden
Buchstaben inklusive).

e) Umdrehen: Wir haben unser alphabet gegeben, wollen aber ein genau
umgedrehtes Alphabet als Liste (umgedreht = [z, y, x, usw...]). Da wir dieses
natürlich nicht per Hand aufschreiben wollen, schreibe die Funktion "umdrehen",
die eine Liste bekommt und die umgedrehte Version dieser Liste zurückgibt.

Hinweis: Benutzt hierfür bitte nicht die eingebaute .reverse()-Funktion von
Listen.


Schwierigkeiten:
a) 1/5
b) 2/5
c) 3/5
d) 3/5
e) 3/5


Tipp: ihr könnt die globale Variable "alphabet" in den Aufgaben benutzen :)
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']


def string_to_list() -> list[str]:
    """
    Forde eine Zeichenkette vom Benutzer und formatiere diese als Liste.
    >>> string_to_list()
    Gib etwas ein: a3gh?§ds!fs
    ['a', '3', 'g', 'h', '?', '§', 'd', 's', '!', 'f', 's']
    """
    text = input("Geben Sie eine Zeichenkette ein: ")
    return list(text)


def buchstabe_zur_zahl() -> str:
    """
    Fordere eine Zahl vom Nutzer und gebe die entsprechende Zahl aus dem
    Alphabet aus.
    >>> buchstabe_zur_zahl()
    Gib eine Zahl ein: 5
    'e'
    """
    zahl = input("Gib eine Zahl ein: ")
    return alphabet[int(zahl) - 1]


def liste_als_speicher() -> list[str]:
    """
    Forde drei Zahlen vom Benutzer, speicher die entsprechenden Buchstaben in
    einer Liste und gebe diese zurück.
    >>> liste_als_speicher()
    Gib eine Zahl ein: 3
    Gib eine Zahl ein: 2
    Gib eine Zahl ein: 13
    ['c', 'b', 'm']
    """
    returnlist: list[str] = []
    for _ in range(3):
        zahl = input("Gib eine Zahl ein: ")
        returnlist += [alphabet[int(zahl) - 1]]
    return returnlist


def alphabetabschnitt() -> list[str]:
    """
    Fordere zwei Zahlen vom Benutzer, und gebe den entsprechenden Abschnitt
    aus der Liste "alphabet" zurück.
    >>> alphabetabschnitt()
    Gib eine Zahl ein: 3
    Gib eine Zahl ein: 11
    ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    """
    zahl1 = int(input("Gib eine Zahl ein: "))
    zahl2 = int(input("Gib eine Zahl ein: "))
    return alphabet[zahl1 - 1: zahl2]


def umdrehen(liste: list) -> list:
    """
    Dreht eine gegebene Liste um.

    >>> umdrehen([1, 2, 3])
    [3, 2, 1]
    """
    # Wäre auch sehr schön mit einer for-schleife lösbar
    neue_liste: list = []
    index = len(liste) - 1
    while index >= 0:
        neue_liste.append(liste[index])
        index -= 1
    return neue_liste


if __name__ == "__main__":
    pass
