import doctest
"""
Zeichenketten sind in Python sehr wichtig. Es gibt einige Funktionen speziell
für Zeichenketten. In dieser Aufgabe lernt ihr diese besser kennen.

a) In der Vorstellungsrunde soll jeder Ersti ein Tier finden, das den gleichen
Anfangsbuchstaben wie der Name hat. Da es aber ganz schön viele Erstis an der
Uni Freiburg gibt, brauchen wir eine Funktion, die für uns überprüft, ob ein
Name und ein Tier den gleichen Anfangsbuchstaben haben.

Schreibe die Funktion "check_first_letter", die den ersten Buchstaben vom
Namen und den ersten Buchstaben des Tiers vegleicht.
Hinweis: Groß- und Kleinschreibung beachten (teil der nächsten aufgabe)

b) Die Funktion aus a) funktioniert zwar schon, "Lenia" und "löwe" haben laut
ihr aber nicht den gleichen Anfangsbuchstaben. Logisch: "a" und "A" sind nicht
das selbe.

Schreibe also eine ähnliche Funktion "check_first_letter_ignore_case" welche
die Groß und Kleinschreibung ignoriert.

c) manchmal will man einfach nur schreien. Schreibe die Funktion "scream",
welche einen Text nimmt und ihn in GROSSBUCHSTABEN! umwandelt, sofern ein
Ausrufezeichen darin vorkommt. Sonst soll "scream" den Text so wie er ist
zurückgeben.

Schwierigkeit:
a) 1/5
b) 2/5
c) 2/5
d) 3/5

"""


def check_first_letter(name: str, tier: str) -> bool:
    """
    Überprüft, ob der Anfangsbuchstabe von "name" und "tier" der selbe ist.

    >>> check_first_letter("lenia", "löwe")
    True
    >>> check_first_letter("Lenia", "löwe")
    False
    >>> check_first_letter("jakob", "löwe")
    False
    """
    ...


def check_first_letter_ignore_case(name: str, tier: str) -> bool:
    """
    Überprüft, ob der Anfangsbuchstabe von "name" und "tier" übereinstimmen.
    Ignoriert Groß und Kleinschreibung

    >>> check_first_letter_ignore_case("Lenia", "löwe")
    True
    >>> check_first_letter_ignore_case("lenia", "löwe")
    True
    >>> check_first_letter_ignore_case("jakob", "löwe")
    False
    """
    ...


def scream(text: str) -> str:
    """
    Wandelt "text" in einen GESCHRIENEN Text um.

    >>> scream("Hallo dahinten!!!")
    'HALLO DAHINTEN!!!'
    >>> scream("Hallo dahinten.")
    'Hallo dahinten.'
    """
    ...


def snake_case(namen: list[str]) -> str:
    """
    Verwandelt eine Liste von Namen in einen langen snake_case namen.

    >>> snake_case(["das", "ist", "eine", "FUNKTION"])
    'das_ist_eine_funktion'
    """
    ...


if __name__ == "__main__":
    doctest.testmod()
    check_first_letter_ignore_case("Lenia", "löwe")
