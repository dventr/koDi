import argparse
from gensim.models import Word2Vec

word = 'Querdenker'

def we_basics(infile):
    model = Word2Vec.load(infile)
    # In diesem Block kann man ähnliche Vektoren zu
    # einem gegebenen token ausgeben, hier z.B. die 10 nächsten zum
    # Vektor des Wortes 'schreiben'
    sims = model.wv.most_similar(word, topn=10)
    for idx, elem in enumerate(sims, 1):
        print(f"{idx}: {elem[0]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enthält Bausteine für einfache Operationen mit Word Embeddings")
    parser.add_argument("in_file", type=str, help="Input-Datei: Word Embeddings Modell im word_vectors Format")
    args = parser.parse_args()
    we_basics(args.in_file)
