import doctest
"""
a) Schreibe ein Programm, welches den Nutzer auffordert, eine Zahl einzugeben.
Verwende danach die Funktion "print()", um einen Antwortsatz auszugeben,
welcher die Eingabe bestätigt.

b) Schreibe das selbe Programm wie bei a), verwende für die Antwort aber einen
f-string.

c) Matthias verkauft Metallplatten, ein Quadratmeter kostet 2,78€. Seine
Kunden sollen angeben können, welche Abmessungen die Platten haben sollen
(Rechtecke). Leider hat er seine Messgeräte verlegt, und muss mit Schritten
die Meter abzählen. Deshalb dürfen nur ganze Zahlen vom benutzer angegeben
werden. Erstelle ein Programm, welches mit dem Benutzer interagiert und am
Ende ausgibt, wie viel das entsprechende Stück Platte kosten würde.

Schwierigkeit:
a) 2/5
b) 2/5
c) 3/5

"""


def enter_number() -> None:
    """
    """
    number = input("Bitte geben Sie eine Zahl ein: ")
    print(
        "Sie haben die Zahl \"" + number + "\" eingegeben.")


def enter_number_fstring() -> None:
    """
    """
    number = input("Bitte geben Sie eine Zahl ein: ")
    print(f"Sie haben die \
Zahl \"{number}\" eingegeben.")


def kosten_metallplatte() -> None:
    """
    """
    preis = 2.78
    laenge = int(input("Geben Sie die Länge der Metallplatte an: "))
    breite = int(input("Geben Sie die Breite der Metallplatte an: "))
    print(f"Die Metallplatte mit den Maßen {laenge}x{breite}m \
kostet {laenge * breite * preis}€.")


if __name__ == "__main__":
    doctest.testmod()
    enter_number()
    enter_number_fstring()
    kosten_metallplatte()
