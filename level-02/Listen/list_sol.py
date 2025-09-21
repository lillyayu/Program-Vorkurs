import doctest
from unittest.mock import patch


"""
a) Schreibe ein Funktion, die aus einer vom Benutzer eingegebenen Zeichenkette
eine Liste erstellt, in der jedes Zeichen der Zeichenkette einen Listeneintrag
darstellt.
b) Schreibe eine Funktion, die aus einer vom Benutzer eingegebenen
mehrstelligen Zahl eine Liste erstellt, in der jede Ziffer der Zahl einen
Eintrag darstellt.
c) Schreibe eine Funktion, welche vom Benutzer eine Zahl fordert, und
anschließend den im Alphabet der Zahl entsprechenden Buchstaben zurückgibt.
d) Schreibe eine Funktion, welche nacheinander drei Zahlen vom Benutzer
fordert, die entsprechenden Buchstaben in einer Liste "memory" speichert
und diese am Ende zurückgibt.
e) Schreibe eine Funktion, die die zwei Zahlen vom Benutzer fordert (wir gehen
davon aus, dass die zweite Zahl größer ist als die erste und alle Zahlen
kleiner 27 sind) und den entsprechenden Listenabschnitte aus der Liste
"alphabet" zurückgibt (die den vom Benutzer gegebenen Zahlen entprechenden
Buchstaben inklusive).

Hinweis: alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
    'p','q','r','s','t','u','v','w','x','y','z']



Schwierigkeiten:
a) 1/5
b) 2/5
c) 2/5
d) 3/5
e) 3/5
"""


def string_to_list():
    """
    Forde eine Zeichenkette vom Benutzer und formatiere diese als Liste.
    >>> with patch('builtins.input', return_value='a3gh?§ds!fs'):
    ...     string_to_list()
    ['a', '3', 'g', 'h', '?', '§', 'd', 's', '!', 'f', 's']
    """
    text = input("Geben Sie eine Zeichenkette ein: ")
    return list(text)


def int_to_list():
    """
    Forde eine mehrstellige Zahl vom Benutzer und formatiere diese als Liste.
    >>> with patch('builtins.input', return_value=314159265358979323846):
    ...     int_to_list()
    ['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', \
'9', '3', '2', '3', '8', '4', '6']
    """
    zahl = input("Geben Sie eine mehrstellige Zahl ein: ")
    return list(str(zahl))


def buchstabe_zur_zahl():
    """
    Fordere eine Zahl vom Nutzer und gebe die entsprechende Zahl aus dem
    Alphabet aus.
    >>> with patch('builtins.input', return_value='5'):
    ...     buchstabe_zur_zahl()
    'e'
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']
    zahl = input("Geben Sie eine Zahl ein: ")
    return alphabet[int(zahl) - 1]


def liste_als_speicher():
    """
    Forde drei Zahlen vom Benutzer, speicher die entsprechenden Zahlen in
    einer Liste und gebe diese zurück.
    >>> with patch('builtins.input', side_effect=['3', '2', '13']):
    ...     liste_als_speicher()
    ['c', 'b', 'm']
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']
    returnlist = []
    for _ in range(3):
        zahl = input("Geben Sie eine Zahl ein: ")
        returnlist += [alphabet[int(zahl) - 1]]
    return returnlist


def alphabetabschnitt():
    """
    Fordere zwei Zahlen vom Benutzer, und gebe den entsprechenden Abschnitt
    aus der Liste "alphabet" zurück.
    >>> with patch('builtins.input', side_effect=['3', '11']):
    ...     alphabetabschnitt()
    ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']
    zahl1 = int(input("Geben Sie eine Zahl ein: "))
    zahl2 = int(input("Geben Sie eine Zahl ein: "))
    return alphabet[zahl1 - 1: zahl2]
