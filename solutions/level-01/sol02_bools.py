"""
Wir werden sehr oft Wahrheitswerte benutzen. Dafür ist es gut, ein Gefühl
für diese zu bekommen.

Versucht, die Aufgaben zuerst im Kopf zu lösen und dann mit Python
zu überprüfen.

a) Ist 5 kleiner als 3 oder 1 kleiner gleich 1 und 8 größer gleich 12
oder 2 kleiner 9 wahr?
Ändere ein Wort, um den Wert umzudrehen.

b) Ist (10 größer 7 und 4 kleiner 2) oder (3 gleich 3) wahr?
Ändere ein Wort, um den Wert umzudrehen.

c) Ist nicht (5 gleich 5 und 2 größer 3) und (7 kleiner 6) wahr?
Ändere ein Wort, um den Wert umzudrehen.

d) Ist (8 kleiner 10 oder 2 größer 5) und (3 gleich 3 und nicht 4 kleiner 2)
wahr? Ändere eine Zahl, um den Wert umzudrehen.

Schwierigkeit
a) 1/5
b) 1/5
c) 1/5
d) 2/5
"""

if __name__ == "__main__":
    # a)
    print(5 < 3 or 1 <= 1 and 8 >= 12 or 2 < 9)  # True
    print(5 < 3 or 1 <= 1 and 8 >= 12 and 2 < 9)  # False

    # b)
    print((10 > 7 and 4 < 2) or (3 == 3))  # True
    print((10 > 7 and 4 < 2) and (3 == 3))  # False

    # c)
    print(not (5 == 5 and 2 > 3) and (7 < 6))  # False
    print(not (5 == 5 and 2 > 3) or (7 < 6))  # True

    # d)
    print((8 < 10 or 2 > 5) and (3 == 3 and not 4 < 2))  # True
    print((8 < 10 or 2 > 5) and (3 == 4 and not 4 < 2))  # False
