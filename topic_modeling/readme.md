# README für BERTopic

## Überblick
Dieses Jupyter-Notebook dient zur Analyse und Visualisierung von Textdaten mithilfe fortschrittlicher NLP-Techniken, einschließlich BERTopic. Das Notebook umfasst mehrere Schritte: Datenimport, Datenverarbeitung, Modellbildung mit BERTopic, und Visualisierung der Ergebnisse.

Mit *compare* können zwei unterschiedliche Korpora miteinander verglichen werden. Mögliche Inputformate sind:
- zwei verschiedene .csv Dateien
- .csv Datei, die basierend auf Metadaten (Zeitraum oder Quelle) unterteilt werden

Mit *korpus* wird ein Topic Modeling für ein Korpus erstellt, das je nach Fragestellung in kleinere Textmengen (Zeitraum oder Quelle) unterteilt werden kann.

## Voraussetzungen
- Installation von Python und Jupyter Notebook.
- Notwendige Python-Bibliotheken: `plotly`, `matplotlib`, `pandas`, `numpy`, `sklearn`, `sentence_transformers`, `bertopic`, `hdbscan`, `umap-learn`.
- Die relevanten Daten sollten im CSV-Format vorliegen.

## Hauptfunktionen des Notebooks
1. **Datenimport und -vorbereitung**: Importieren von Bibliotheken und Vorbereiten der Arbeitsumgebung.
2. **Einrichtung des BERTopic-Modells**: Verwendung von Transformermodllen zur Erstellung von Topic Modellen basierend auf Vektoren.
3. **Dimensionalitätsreduktion und Clustering**: Anwendung von UMAP für die Dimensionalitätsreduktion und HDBSCAN für das Clustering.
4. **Vektorisierung und Textverarbeitung**: Einsatz von CountVectorizer und ClassTfidfTransformer zur Textverarbeitung.
5. **Analyse spezifischer Korpora und Zeiträume**: mögliche Aufteilung der Daten in unterschiedliche Korpora und Zeiträume zur gezielten Analyse.
6. **Visualisierung der Ergebnisse**: Erstellung verschiedener Visualisierungen wie Heatmaps, hierarchische Darstellungen und dynamische Graphen zur Darstellung der Topics und ihrer Verteilung.

## Benutzung
1. **Daten vorbereiten**: Stellen Sie sicher, dass Ihre Daten im CSV-Format (siehe Preprocessing) vorliegen und im gleichen Verzeichnis wie das Notebook gespeichert sind.
2. **Bibliotheken installieren**: Installieren Sie die erforderlichen Bibliotheken, falls noch nicht geschehen.
3. **Notebook ausführen**: Führen Sie die Zellen des Notebooks der Reihe nach aus, um die Analyse durchzuführen.
4. **Ergebnisse überprüfen**: Überprüfen Sie die verschiedenen Visualisierungen und Ausgaben, um Einblicke in Ihre Daten zu gewinnen.

## Hinweise
- Die Performance und Genauigkeit der Analyse hängt stark von der Qualität und Konsistenz der Eingabedaten ab.
- Anpassungen am Code können erforderlich sein, um ihn an spezifische Datenformate oder Analyseziele anzupassen.
- Für eine effektive Nutzung sind Grundkenntnisse in Python und Datenanalyse empfehlenswert.
