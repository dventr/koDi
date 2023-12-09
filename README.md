# koDi
Quantitative Methoden für diskurslinguistische Perspektiven

# Readme für die Ordnerstruktur: preprocessing, topic_modeling, twec

## Überblick
Diese Dokumentation gibt einen Überblick über die drei Hauptordner `preprocessing`, `topic_modeling` und `twec`, die jeweils unterschiedliche Aspekte der Datenverarbeitung und -analyse abdecken. Jeder Ordner enthält spezifische Skripte und Ressourcen, die für die jeweiligen Prozesse erforderlich sind.

## Ordnerstruktur

### 1. preprocessing
Dieser Ordner enthält Skripte und Ressourcen, die für die Vorverarbeitung von Textdaten verwendet werden. Die Vorverarbeitung ist ein kritischer Schritt, um Daten für die weitere Analyse vorzubereiten.

#### Inhalt:
- Kombiniert die .csv-Datei auf NextCloud mit einer .txt-Datei von CQP-Web

### 2. topic_modeling
In diesem Ordner finden Sie Skripte und Modelle für das Topic Modeling. Topic Modeling ist eine Methode zur Identifizierung von Themen in großen Textmengen.

#### Inhalt:
- BERTopic-Skript, das für diskurslinguistische Fragestellungen optimiert wurde.
- Man kann alles auf Marten Grotendorsts [GitHub-Seite](https://maartengr.github.io/BERTopic/api/bertopic.html) nachlesen


### 3. twec
Der `twec`-Ordner befasst sich mit der Anwendung von Temporal Word Embeddings with a Compass (TWEC), einer Methode zur Analyse von Wortbedeutungen über die Zeit. [TWEC-Paper](https://arxiv.org/pdf/2308.02142.pdf)

#### Inhalt:
- **TWEC-Skripte:** Skripte zum Trainieren von TWEC-Modellen. Das Skript basiert in grossen Teilen auf folgendes Skript: [TWEC](https://gitlab.uzh.ch/zukoko/sommerschule-2023/-/tree/master/C5-Distributionelle-Semantik/TWEC_Clustering?ref_type=heads)
- **Datenhandling:** Werkzeuge zum Importieren und Vorbereiten von Datensätzen für TWEC.
- **Modell-Analyse:** Skripte zur Untersuchung und Interpretation der generierten Word Embeddings.
- **Visualisierung:** Tools zur graphischen Darstellung der Ergebnisse, z.B. durch Vektorraum-Diagramme.

## Nutzungshinweise
- **Installation der Abhängigkeiten:** Stellen Sie sicher, dass alle benötigten Bibliotheken installiert sind. Die erforderlichen Bibliotheken finden Sie in den jeweiligen Unterordnern.
- **Anpassung der Skripte:** Passen Sie die Skripte an Ihre spezifischen Daten und Anforderungen an.
- **Dokumentation:** Jeder Ordner enthält eine spezifische README-Datei mit detaillierteren Anweisungen und Informationen.

## Zusätzliche Ressourcen
Zusätzliche Ressourcen und Beispiele finden Sie in den jeweiligen Unterordnern. Für eine umfassendere Anleitung und Best Practices verweisen wir auf die beigefügten Dokumentationen und externe Quellen. 
