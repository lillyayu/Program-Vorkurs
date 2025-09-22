"""
Zeichenketten sind in Python sehr wichtig. Es gibt einige Funktionen speziell
für Zeichenketten. In dieser Aufgabe lernt ihr diese besser kennen.

a) Welcher Buchstabe steht an Stelle 777 wenn wir 134 mal das Wort
"Programmiervorkurs" wiederholen?

Und wie sieht diese Funktion allgemein aus? Welcher Buchstabe steht an der
x-ten Stelle, wenn ich das Wort y z-mal wiederhole?

b) In der Vorstellungsrunde soll jeder Ersti ein Tier finden, das den gleichen
Anfangsbuchstaben wie der Name hat. Da es aber ganz schön viele Erstis an der
Uni Freiburg gibt, brauchen wir eine Funktion, die für uns überprüft, ob ein
Name und ein Tier den gleichen Anfangsbuchstaben haben.

Schreibe die Funktion "check_first_letter", die den ersten Buchstaben vom
Namen und den ersten Buchstaben des Tiers vegleicht.
Hinweis: Groß- und Kleinschreibung beachten (teil der nächsten aufgabe)

c) Die Funktion aus b) funktioniert zwar schon, "Lenia" und "löwe" haben laut
ihr aber nicht den gleichen Anfangsbuchstaben. Logisch: "a" und "A" sind nicht
das selbe.

Schreibe also eine ähnliche Funktion "check_first_letter_ignore_case" welche
die Groß und Kleinschreibung ignoriert.

d) manchmal will man einfach nur schreien. Schreibe die Funktion "scream",
welche einen Text nimmt und ihn in GROSSBUCHSTABEN! umwandelt, sofern ein
Ausrufezeichen darin vorkommt. Sonst soll "scream" den Text so wie er ist
zurückgeben.

e) Funktionen werden in Python nach der snake_case notation benannt, bei der
die Worte mit Unterstrichen verbunden werden. Schreibe die Funktion connect,
welche eine Liste von Worten mit Unterstrichen verbindet.

f) schreibe die Funktion snake_case, welche zusätzlich wie beim Snake-Case alle
Worte in nur Kleinbuchstaben verwandelt. Spicy!

Schwierigkeit:
a) 1/5
b) 1/5
c) 2/5
d) 2/5
e) 3/5
f) 4/5 🌶️

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
    return name[0] == tier[0]


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
    return name.lower()[0] == tier.lower()[0]


def scream(text: str) -> str:
    """
    Wandelt "text" in einen GESCHRIENEN Text um.

    >>> scream("Hallo dahinten!!!")
    'HALLO DAHINTEN!!!'
    >>> scream("Hallo dahinten.")
    'Hallo dahinten.'
    """
    if text.__contains__("!"):
        return text.upper()
    return text


def connect(namen: list[str]) -> str:
    """
    Verwandelt eine Liste von Namen in einen langen snake_case namen.

    >>> snake_case(["das", "ist", "eine", "funktion"])
    'das_ist_eine_funktion'
    """
    return "_".join(namen)


def snake_case(namen: list[str]) -> str:
    """
    Verwandelt eine Liste von Namen in einen langen snake_case namen.

    >>> snake_case(["DaS", "iSt", "eine", "FUNKTION"])
    'das_ist_eine_funktion'
    """
    namen_lower: list[str] = []
    for name in namen:
        namen_lower.append(name.lower())
    return "_".join(namen_lower)


def verschlüssele(text: str, key: int) -> str:
    """
    Verschiebt jeden Buchstaben des Textes um "key" im Alphabet.

    >>> verschlüssele("abc", 3)
    'def'
    >>> verschlüssele("Hello There!", 7)
    'Nkrru&Znkxk''
    """
    verschlüsselt: str = ""
    for char in text:
        verschlüsselt += chr(ord(char) + key)
    return verschlüsselt


def entschlüssele(text: str, key: int) -> str:
    """
    Verschiebt jeden Buchstaben des Textes um "key" im Alphabet.

    >>> verschlüssele("def", 3)
    'abc'
    >>> entschlüssele("Nkrru&Znkxk'", 7)
    'Hello There!'
    """
    entschlüsselt: str = ""
    for char in text:
        entschlüsselt += chr(ord(char) - key)
    return entschlüsselt


if __name__ == "__main__":
    check_first_letter_ignore_case("Lenia", "löwe")
