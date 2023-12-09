# README für Python-Skript

## Übersicht
Dieses Skript ist dazu gedacht, Metadaten aus einer CSV-Datei (`tp1p1_metadata.csv`) mit Textinhalten aus einer TXT-Datei (`sp1p1_1-export.txt`) zu kombinieren. Es extrahiert spezifische Daten aus beiden Dateien und erstellt daraus eine neue, kombinierte CSV-Datei.

## Voraussetzungen
- Python muss auf dem System installiert sein.
- Die Bibliothek `pandas` muss installiert sein. Sie kann mit `pip install pandas` installiert werden.
- Das Skript verwendet auch das `re` Modul für reguläre Ausdrücke, das in der Standardbibliothek von Python enthalten ist.
- .csv ist im koDi-Ordner auf Nextcloud
- .txt Datei kann man von CQP downloaden

## Dateien
- **Eingabedateien**:
  - `tp1p1_metadata.csv`: Eine CSV-Datei, die Metadaten enthält. Sie sollte die Spalten 'text_id', 'text_date', 'text_section', 'text_source', 'text_text_type' und 'text_title' haben.
  - `sp1p1_1-export.txt`: Eine TXT-Datei, die Textinhalte enthält. Die Texte sind in `<text>`-Tags eingeschlossen, mit jeweils einer `id`.
- **Ausgabedatei**:
  - `tp1_sub.csv`: Die neu erstellte CSV-Datei, die die kombinierten Daten enthält.

## Benutzung
1. Stellen Sie sicher, dass die Eingabedateien im selben Verzeichnis wie das Skript liegen oder passen Sie die Dateipfade im Skript entsprechend an.
2. Führen Sie das Skript aus. Es liest die Metadaten aus der CSV-Datei und den Textinhalt aus der TXT-Datei.
3. Das Skript extrahiert Textabschnitte, die den Metadaten in der CSV-Datei entsprechen, und kombiniert diese zu einer neuen DataFrame.
4. Datenformate, insbesondere das Datum, werden angepasst.
5. Das Ergebnis wird als .csv gespeichert

## Funktionen des Skripts
- **Einlesen der Metadaten**: Die Metadaten werden aus der CSV-Datei eingelesen.
- **Extraktion des Textes**: Das Skript verwendet reguläre Ausdrücke, um Textinhalte aus der TXT-Datei zu extrahieren.
- **Zusammenführung der Daten**: Die extrahierten Texte werden mit den entsprechenden Metadaten aus der CSV-Datei kombiniert.
- **Datumsumwandlung**: Das Datum wird in ein einheitliches Format umgewandelt.
- **Speichern der kombinierten Daten**: Die kombinierten Daten werden in eine neue CSV-Datei exportiert.

## Hinweise
- Die Effizienz und Genauigkeit des Skripts hängt von der Konsistenz der Formate in den Eingabedateien ab.
- Stellen Sie sicher, dass die Eingabedateien korrekt formatiert sind, um Fehler bei der Ausführung des Skripts zu vermeiden.
