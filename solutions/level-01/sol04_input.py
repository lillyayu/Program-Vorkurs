"""
Hinweis: Die Tests funktionieren bei dieser Datei wegen input nicht.
Sie sind trotzdem als Beispiele zu verstehen :)

a) Schreibe ein Programm, welches den Nutzer auffordert, eine Zahl einzugeben.
Verwende danach die Funktion "print()", um einen Antwortsatz auszugeben,
welcher die Eingabe bestätigt.

b) Schreibe dasselbe Programm wie bei a), verwende für die Antwort aber einen
f-string. Hinweis: (Kapitel 5.1) -> f"Text {Variable}"

d) Matthias verkauft Metallplatten, ein Quadratmeter kostet 2,78€. Seine
Kunden sollen angeben können, welche Abmessungen die Platten haben sollen
(Rechtecke). Leider hat er seine Messgeräte verlegt, und muss mit Schritten
die Meter abzählen. Deshalb dürfen nur ganze Zahlen von der BenutzerIn an-
gegeben werden. Erstelle ein Programm, welches mit dem Benutzer interagiert
und am Ende ausgibt, wie viel das entsprechende Stück Platte kosten würde.

e) Ein Getränkeautomat verkauft Wasserflaschen zu 1,25€ und Saftflaschen
zu 1,85€. Schreibe die Funktion "getränke", welche die BenuterIn fragt,
wie viele Wasserflaschen und wie viele Saftflaschen sie kaufen will.

Am Ende soll das Programm die Gesamtkosten berechnen und ausgeben.
Verwende dafür f-Strings, um die Ausgabe lesbar zu gestalten.
Bonus, wenn du auf 2 Nachkommastellen rundest (Kapitel 5.1 :))

Schwierigkeit:
a) 1/5
b) 2/5
c) 3/5
e) 3/5

"""


def enter_number() -> None:
    number = input("Bitte geben Sie eine Zahl ein: ")
    print(
        "Sie haben die Zahl \"" + number + "\" eingegeben.")


def enter_number_fstring() -> None:
    number = input("Bitte geben Sie eine Zahl ein: ")
    print(f"Sie haben die \
            Zahl \"{number}\" eingegeben.")


def kosten_metallplatte() -> None:
    preis = 2.78
    laenge = int(input("Geben Sie die Länge der Metallplatte an: "))
    breite = int(input("Geben Sie die Breite der Metallplatte an: "))
    print(f"Die Metallplatte mit den Maßen {laenge}x{breite}m \
kostet {laenge * breite * preis}€.")


def getränke() -> None:
    wasser: int = int(input("Anzahl Wasserflaschen: "))
    saft: int = int(input("Anzahl Saftflaschen: "))

    gesamt: float = wasser * 1.25 + saft * 1.85
    print(f"Du hast {wasser} Wasserflaschen und {saft} Saftflaschen gewählt.")
    print(f"Die Gesamtkosten betragen {gesamt:.2f}€.")


if __name__ == "__main__":
    enter_number()
    enter_number_fstring()
    kosten_metallplatte()
    getränke()
