# Programmier-Vorkurs

Hallo 👋  
hier findet ihr die Aufgaben zum Programmier-Vorkurs.

Die Aufgaben sind in **4 Ordner** eingeteilt:  

- **Level 1** – Grundlagenaufgaben, Logik  
- **Level 2** – Bedingungen, Schleifen und etwas kniffligere Aufgaben
- **Level 3** – Arbeiten mit Klassen und komplexeren Aufgaben

☁️ Auch die Aufgaben in Level 1 sind teilweise nicht einfach. Wir haben versucht, Bewertungen für die Aufgaben zu finden, diese sind allerdings sehr subjektiv und für uns schwer einschätzbar. Wir freuen uns deshalb über Feedback, welche Aufgaben ihr viel zu schwer oder zu leicht bewertet fandet. 

👉 Tipp: Fangt mit **Level 1** an und steigert euch. Ihr müsst nicht alle Aufgaben schaffen, der Kurs soll vor allem ein Gefühl für das Programmieren geben. Wenn Fragen aufkommen, oder ihr Fehler in der Aufgabe findet, sagt einfach eurer Tutor*in Bescheid 🫶

## Aufgaben herunterladen ♻️

Wenn ihr keine Lust auf Schnickschnack habt, könnt ihr den Ordner mit allen Aufgaben einfach oben rechts bei "Code" als Zip-Datei herunterladen.

Falls ihr Lust habt, könnt ihr aber auch versuchen, den Ordner über Git herunterzuladen, bzw. zu "klonen".

Das hat den Vorteil, dass ihr dann Änderungen / Korrekturen in den Aufgaben viel einfacher bekommen könnt, und die Lösungen am Ende auch mit nur einem Befehl in der Konsole in euren Ordner bekommen könnt.
<details>
<summary>
💡 Hier ausklappen, wenn ihr es mit git versuchen wollt :)
</summary>
<h3> 📥 Anleitung: den Ordner (<strong>das Git-Repository</strong>) klonen: </h3>
Damit ihr die Aufgaben bearbeiten könnt, müsst ihr das Repository auf euren eigenen Rechner holen.
Das nennt man klonen.

#### 1. Git installieren 👩‍🔧

- Windows: Git herunterladen und installieren (bei allen Fragen einfach „weiter“ klicken).

- macOS: Meist ist Git schon installiert.
Sonst:``brew install git` im Terminal.


- Linux (Ubuntu/Debian):
  ```
  sudo apt update
  sudo apt install git
  ```
#### 2. Ordner wählen  🗂 ️
Überlegt euch, in welchem Ordner ihr die Dateien speichern wollt. Zum Beispiel Dokumente.
Öffnet dort ein Terminal (oder Git Bash auf Windows).
#### 3. Repo klonen ♻
Gebe folgenden Befehl ein:
```
git clone https://github.com/lillyayu/Program-Vorkurs.git
```
Das lädt das komplette Repo herunter.
Es entsteht ein neuer Ordner Program-Vorkurs.
#### 4. In den Ordner wechseln ➡️
```
cd Program-Vorkurs
```
Jetzt seid ihr im Ordner mit den Aufgaben und könnt die Dateien sehen.

Wenn Änderungen kommen, oder um am Ende die Lösungen direkt in den Ordner zu bekommen, könnt ihr im Ordner "Program-Vorkurs" `git pull`
machen.

Um eine Datei direkt mit VSCode zu öffnen, könnt ihr im Terminal übrigens `code <datei.py>` schreiben :)

Bei Fragen hierzu kann oft ChatGPT weiterhelfen, ansonsten ist es nicht wichtig, dass ihr das über git macht, aber ein nice-to-have. ☀️
</details>

## Struktur der Aufgaben ⚙️

Ganz oben in der Datei steht immer die **Beschreibung der Aufgabe** und darunter ein **Funktionsgerüst**, in das ihr euren Code schreiben könnt. 

Das sieht vielleicht erstmal etwas kompliziert aus, ist aber viel einfacher als es aussieht.

Ihr sollt einfach den fehlenden Teil (die drei Punkte `...`) durch euren Code ersetzen.  
Wenn ihr das richtig macht, passiert genau das, was oben in der Beschreibung, bzw. in den Beispielen steht.

Ein Beispiel:

```py3
"""
a) Schreibe die Funktion "hallo", welche 'hallo' ausgibt
"""

def hallo() -> None:
    """
    Gibt hallo aus.
    >>> hallo()
    hallo
    """
    ...


# Hier müsstet ihr ... mit `print("hallo")` ersetzen.
```


💡 Bonustipp: Python kann diese Tests in der Beschreibung (den **docstring**) automatisch ausführen, schaut dazu mal im Skript unter Kapitel 3.2 :)

## Lösungen ✅

Die Lösungen werden wir im Anschluss an die Aufgaben auch in dieses Repository stellen. Beachtet bitte, dass es Musterlösungen sind. Man kann auf viele verschiedene Arten programmieren und oft sind Lösungen gleich gut! 🌱

Und jetzt viel Spaß mit den Aufgaben, \
Eure Fachschaft TF ☀️