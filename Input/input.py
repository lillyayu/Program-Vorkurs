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
    >>> with patch('builtins.input', return_value='5'):
    ...     enter_number()
    Sie haben die Zahl "5" eingegeben.
    """
    pass


def enter_number_fstring() -> None:
    """
    >>> with patch('builtins.input', return_value='5'):
    ...     enter_number_fstring()
    Sie haben die Zahl "5" eingegeben.
    """
    pass


def kosten_metallplatte() -> None:
    """
    >>> with patch('builtins.input', side_effect=['3', '2']):
    ...     kosten_metallplatte()
    Die Metallplatte mit den Maßen 3x2m kostet 16.68€.
    """
    pass


if __name__ == "__main__":
    enter_number()
    enter_number_fstring()
    kosten_metallplatte()
