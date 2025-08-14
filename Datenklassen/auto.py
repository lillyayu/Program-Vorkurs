from dataclasses import dataclass
"""
Datenklassen sind eine besondere Form der Klassen, die wir schon kennengelernt
haben. Sie übernehmen viele Aufgaben von Klassen, welche man normalerweise
selber definieren muss. Zum Beispiel kann man eine Datenklasse gut ausgeben.


"""


@dataclass
class Reifen:
    durchmesser: int
