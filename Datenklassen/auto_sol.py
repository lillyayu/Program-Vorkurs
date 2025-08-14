from dataclasses import dataclass
"""
Datenklassen sind eine besondere Form der Klassen, die wir schon kennengelernt
haben. Sie übernehmen viele Aufgaben von Klassen, welche man normalerweise
selber definieren muss. Zum Beispiel kann man eine Datenklasse gut ausgeben.

Wir haben hier schon das Beispiel der Datenklasse FahrerIn vorgegeben.

a) Definiere nach dem gleichen Prinzip wie die Klasse FahrerIn die Datenklasse
"Auto" mit den folgenden Attributen:
Marke (Zeichenkette)
Modell (Zeichenkette)
Baujahr (Ganzzahl)
FahrerIn (FahrerIn)

Hinweis: Wenn du diese Aufgabe korrekt löst, sollte das Dokument keine Fehler
mehr anzeigen :)

b) Definiere in der Klasse Auto die Funktion hupe(), welche "Tuuuuut!" ausgibt.

c) Definiere in der Klasse Auto die Funktion fahrerin_grüßt(), welche die
"grüßt" Funktion der Klasse FahrerIn mit der FahrerIn des Autos aufruft
und dazu noch das Auto vorstellt.
In unserem Beispiel soll die Ausgabe so aussehen:
---------
Hallo, ich bin Lisa!!
Das hier ist mein Opel Astra von 2007
---------


Schwierigkeit:
a) 2/5
b) 1/5
c) 3/5

"""


@dataclass
class FahrerIn:
    vorname: str
    nachname: str
    alter: int
    gender: str
    größe: int
    gültiger_führerschein: bool

    def grüßt(self) -> None:
        """
        Die FahrerIn stellt sich vor.

        >>> lisa = FahrerIn("Lisa", "Krause", 27, "Frau", 177, True)
        >>> lisa.grüßt()
        Hallo! Ich bin Lisa!!
        """
        print("Hallo! Ich bin " + self.vorname + "!!")


@dataclass
class Auto:
    marke: str
    modell: str
    baujahr: int
    fahrerin: FahrerIn

    def fahrerin_grüßt(self):
        """
        Die Fahrerin stellt sich und ihr Auto vor.

        >>> a = Auto("Open", "Astra", 2007, FahrerIn("Lisa", "Krause", 27,\
            "Frau", 177, True))
        >>> a.fahrerin_grüßt()
        Hallo! Ich bin Lisa!!
        Das hier ist mein Open Astra von 2007
        """

        self.fahrerin.grüßt()
        print("Das hier ist mein", self.marke,
              self.modell, "von", self.baujahr)


if __name__ == "__main__":
    lisa: FahrerIn = FahrerIn("Lisa", "Krause", 27, "Frau", 177, True)
    lisa.grüßt()

    opel_astra: Auto = Auto("Open", "Astra", 2007, lisa)
    opel_astra.fahrerin_grüßt()
