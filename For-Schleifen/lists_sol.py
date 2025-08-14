"""
Eine der häufigsten Anwendungen von For-Schleifen ist das durchlaufen von
Listen, zum Beispiel zum sortieren, zum herausfinden der größten Zahl, zum
Überprüfen der Werte in der Liste und viel weiterem.

Diese Aufgabe beschäftigt sich mit allen möglichen Listenoperationen.

Hinweis: in Python gibt es viele dieser Operatoren schon (max() gibt das max-
imum einer Liste zurück). Diese dürft ihr hier natürlich nicht verwenden.

a) Wir haben eine Liste mit Wahrheitswerten (z.B. [True, True, False, True]).
Nun wollen wir überprüfen, ob jeder dieser Werte wahr ist. Falls auch nur einer
der Werte Falsch sein sollte, soll die Funktion False zurückgeben, sonst True
Schreibe die Funktion "alle_wahr", welche genau dies tut.

b) Bei b haben wir eine Liste mit Noten von Studierenden. Wir wollen gerne
wissen, was die Bestnote ist, die in der Klausur erreicht wurde.
Schreibe die Funktion "bestnote", welche die Liste durchgeht und die Bestnote
ausgibt.
Wenn die Liste leer ist, gib None zurück.

c) Es gibt Professor:innen, welche zwar in ihrem Fach brilliant sind, deren
Vorlesungsfolien allerdings wirklich mittelmäßig sind. Des öfteren sieht man
dort Wortneuschöpfungen mit zusammengesetzten Nomen, welche immer länger und
länger Werden. Wir haben also eine Liste an Worten (strings), und wollen uns
das längste dieser Worte anschauen, um zu sehen was für kreative Erzeugnisse
es so gibt.
Schreibe die Funktion "längstes_wort" welche das längste Wort aus einer Liste
an Strings zurückgibt.

d) (Schwierig) Vielleicht habt ihr ja schon die Aufgabe "türsteher" aus dem
Ordner "If-Verzweigungen" gemacht. Wenn nicht, dürft ihr hier noch einmal
Türsteher:in spielen.
Ihr kriegt eine Liste von Gästen im Format tuple[str, int]: ("name", alter) und
sollt in einer neuen Liste alle Namen aufschreiben, welche unter 18 sind.
Schreibe die Funktion "überprüfe_gäste", welche genau dies tut.

Schwierigkeit
a) 2/5
b) 3/5
c) 3/5
d) 4/5
"""


def alle_wahr(liste: list[bool]) -> bool:
    """
    Überprüft, ob alle Wahrheitswerte in der Liste wahr sind.

    >>> alle_wahr([True, True])
    True
    >>> alle_wahr([True, True, False, True])
    False
    """
    for value in liste:
        if not value:
            return False
    return True


def bestnote(noten: list[float]) -> float | None:
    """
    Gibt die Beste Note der Liste von Kommazahlen zurück.

    >>> bestnote([1.0, 3.3, 1.0, 5.0, 4.0, 2.3])
    1.0
    >>> bestnote([5.0])
    5.0
    >>> bestnote([])
    """
    if len(noten) == 0:
        return None
    kleinste_note: float = noten[0]
    for note in noten:
        if note < kleinste_note:
            kleinste_note = note
    return kleinste_note


def längstes_wort(wörter: list[str]) -> str:
    """
    Gibt das längste Wort aus einer Liste von Strings zurück.
    Wenn es zwei gleichlange gibt, nimm das erste.

    >>> längstes_wort([])
    ''
    >>> längstes_wort(["die", "tasse", "kaffee", "tassen"])
    'kaffee'
    """
    längstes: str = ""
    for wort in wörter:
        if len(wort) > len(längstes):
            längstes = wort
    return längstes


def überprüfe_gäste(gästeliste: list[tuple[str, int]]) -> list[str]:
    """
    Gibt eine Liste mit den Namen der Menschen zurück, die unter 18 sind.

    >>> überprüfe_gäste([])
    []
    >>> überprüfe_gäste([("Jakob", 19)])
    []
    >>> überprüfe_gäste([("Jakob", 19),("Sophia", 17), ("Anna", 18)])
    ['Sophia']
    >>> überprüfe_gäste([("Jakob", 12),("Sophia", 17), ("Anna", 17)])
    ['Jakob', 'Sophia', 'Anna']
    """
    returnlist: list[str] = []
    for name, alter in gästeliste:
        if alter < 18:
            returnlist.append(name)
    return returnlist
