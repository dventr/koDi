# Readme für TWEC

## Übersicht
Dieses Script bietet eine umfassende Pipeline zur Verarbeitung und Analyse von Textdaten, insbesondere für den Vergleich von Textquellen und Zeiträumen. Es basiert auf der Anwendung von TWEC (Temporal Word Embeddings with a Compass) und anderen textverarbeitenden Methoden. Das Script ist modular aufgebaut, wobei jeder Abschnitt spezifische Aufgaben in der Datenverarbeitung übernimmt.

## Abhängigkeiten
- Pandas: Für das Einlesen und Verarbeiten von CSV-Dateien.
- NLTK oder SpaCy: Für die Tokenisierung der Texte.
- TWEC und Gensim: Für das Training und die Verwendung von Word Embeddings.
- Multiprocessing: Zur Beschleunigung von Berechnungen durch parallele Prozesse.

### Installation
Bevor Sie das Script verwenden, installieren Sie die erforderlichen Bibliotheken über `pip`:
```
pip install -r requirements.txt
```

## Script-Komponenten
1. **Daten-Vorbereitung:** Importieren Sie Ihre CSV-Dateien und initialisieren Sie Strukturen zur Datenhaltung.
   
2. **Vergleich zwischen Quellen:** Ermöglicht das Einlesen und Kategorisieren von Textdaten nach Quellen.

3. **Vergleich zwischen Zeiträumen:** Funktionen zum Einlesen und Sortieren von Texten nach Datumsangaben, was Vergleiche über verschiedene Zeiträume hinweg ermöglicht.

4. **Tokenisierung:** Wandeln Sie Texte in Token um, entweder mit NLTK oder SpaCy, abhängig von Ihrer Präferenz.

5. **Erstellung von Frequenz-Dictionaries:** Erzeugen Sie Wörterbücher, die die Häufigkeiten der Wörter in den Texten abbilden.

6. **TWEC:** Initialisieren und Trainieren von TWEC für das Erstellen von temporalen Word Embeddings.

7. **Speichern der Modelle:** Speichern Sie die trainierten Modelle zur späteren Verwendung und Analyse.

## Anwendungshinweise
- **Daten-Import:** Passen Sie die Pfade zu Ihren CSV-Dateien entsprechend an.
- **Tokenisierung:** Achten Sie auf die korrekte Spracheinstellung bei der Tokenisierung.
- **TWEC-Training:** Beachten Sie, dass das Training von TWEC rechenintensiv sein kann. Stellen Sie sicher, dass Ihre Hardware den Anforderungen entspricht.

## Zusätzliche Informationen
Das Script bezieht sich auf Tim Feldmüllers Anwendung von TWEC, die unter [diesem GitLab-Link](https://gitlab.uzh.ch/zukoko/sommerschule-2023/-/tree/master/C5-Distributionelle-Semantik/TWEC_Clustering/scripts?ref_type=heads) einsehbar ist. Für detailliertere Erklärungen und Beispiele besuchen Sie die angegebene Seite.
