# zusätzliche Skripte
Skripte zum Erstellen eines Telegram-Korpus und zur Analyse der Daten mit WordEmbeddings und BERTopic

Die Daten sind auf diesem Github nicht verfügbar, können aber angefordert werden.

Die folgende Auswahl an Skripten bietet Werkzeuge zur Analyse und zum Gewinnen von Erkenntnissen aus Telegram-Daten.

Die Skripte basieren auf anderen Projekten. Bevor die Skripte verwendet werden, muss das Installationsprotokoll der folgenden Seiten befolgt werden.
- Telegram-Download https://github.com/amiryousefi/telegram-analysis
- Wort-Embedding-Analyse https://gitlab.uzh.ch/noah.bubenhofer/kodup-germanistik/-/tree/master/4._Korpusanalyse/Word_Embeddings

Mit diesem Toolkit können Benutzer wertvolle Einblicke in verschiedene Aspekte von Telegram-Nachrichten und deren Konzept gewinnen, was Forschern hilft, den spezialisierten Wortschatz in Telegram-Daten zu verstehen.

# Übersicht der Skripte
## Telegram
Verschiedene Skripte können verwendet werden, um die Daten von Telegram-Kanälen zu analysieren
- json_download.py kann verwendet werden, um Daten von Telegram zu sammeln
- subcorpus.py wird verwendet, um Daten zu reduzieren und ein Subkorpus zu erstellen
- network_gephi.py erstellt Dateien für die Netzwerkanalyse in Gephi
- id_language.py überprüft die Sprache jedes Kanals
- creation_telegram.py gibt das Erstellungsdatum jedes Kanals an

## WordEmbeddings und Telegram
Benötigte Eingabedateien im .model-Format. Anweisungen finden Sie auf https://gitlab.uzh.ch/noah.bubenhofer/kodup-germanistik/-/tree/master/4._Korpusanalyse/Word_Embeddings
- next_neighbors.py
- cosine_similarity.py
