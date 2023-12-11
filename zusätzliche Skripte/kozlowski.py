# implementation of Kozlowski Method
# input files can be found in the folder 'model' and has the format .model
# output will be a visualization of cosine similarity

import numpy as np
import matplotlib.pyplot as plt
import argparse
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec

antonym_list = [
    ('Solidarität', 'Egoismus'),
    ('Zusammenhalt', 'Eigenverantwortung'),
    ('Zusammenstehen', 'Isolierung'),
    ('Einheit', 'Ausschluß'),
    ('Gemeinschaftssinn', 'Individualismus'),
    ('Hilfsbereitschaft', 'Opportunismus'),
    ('Opferbereitschaft', 'Eigennutz'),
    ('Mitmenschlichkeit', 'Apathie'),
    ('Mitgefühl', 'Gleichgültigkeit'),
    ('Dankbarkeit', 'Undankbarkeit'),
    ('Gemeinsinn', 'Eigensinn'),
    ('Verantwortung', 'Verantwortungslosigkeit'),
    ('Anteilnahme', 'Gleichgültigkeit'),
    ('Verantwortung', 'Selbstverantwortung'),
    ('Gesellschaft', 'Selbstbestimmtheit'),
    ('Gemeinnützigkeit', 'Eigeninteresse'),
    ('Allgemeinwohl', 'Eigenliebe'),
    ('Zusammengehörigkeit', 'Selbstsucht'),
    ('Empathie', 'Indifferenz'),
    ('Selbstlosigkeit', 'Herzlosigkeit'),
    ('Verantwortungsgefühl', 'Empathielosigkeit'),
    ('Solidarität', 'Teilnahmslosigkeit'),
    ('Betroffenheit', 'Intoleranz'),
    ('Gemeinwohl', 'Egoismus'),
    ('gemeinnützig', 'eigennützig'),
    ('solidarisch', 'unsolidarisch'),
    ('sozial', 'asozial'),
    ('altruistisch', 'egoistisch'),
    ('hilfsbereit', 'selbstbestimmt'),
    ('uneigennützig', 'selbstsüchtig'),
    ('selbstlos', 'egozentrisch'),
    ('großherzig', 'herzlos'),
    ('wohltätig', 'opportunistisch'),
    ('empathisch', 'empathielos')]

# This block calculates the cosine similarity between a word vector and a semantic dimension.
# input: list of words to analyze
def we_basics(infile):
    model = Word2Vec.load(infile)
    # A word list can be entered as a string 'Maske' or as a tuple ('Maske', 'FFP2') for very similar words.
    # Note: For the Telegram model, the character 'ß' must be used (for the KD model, 'ß' can be retained).
    word_list = [
        'Coronaleugner', 'Massnahmenkritiker', 'Querdenker', 'Bürgerrechtler', 'Verschwörungstheoretiker'
    ]
    # Ideally, there should be up to 42 antonym pairs. However, it also works with fewer antonym pairs. The order of antonyms does not matter.
    # Note: For the Telegram model, the character 'ß' must be used (for the KD model, 'ß' can be retained).

    vis_list = []
    cultural_dim = 0
    synonyms = 0
    # semantic dimension is calculated. Tuple [0] - Tuple [1]
    for key, value in antonym_list:
        try:
            x = model.wv[key] - model.wv[value]
            cultural_dim += x
        except KeyError:
            print(key, value)
            key = key.replace('ß', 'ss')
            value = value.replace('ß', 'ss')
            x = model.wv[key] - model.wv[value]
            cultural_dim += x

    # divide by length of antonym for the average
    with_div = cultural_dim / len(antonym_list)
    # reshape, in order to calculate cosine similarity 1 | -1
    vector_cultural = with_div.reshape(1, -1)

    # compare each measure with the semantic dimension
    for word_input in word_list:
        try:
            # identify the data type
            if type(word_input) is tuple:
                synonyms = 0
                for word_syn in word_input:
                    synonym = (model.wv[word_syn])
                    synonyms += synonym
                vector_word = (synonyms / len(synonyms)).reshape(1, -1)
                similarity = cosine_similarity(vector_cultural, vector_word)
                thistuple = tuple((similarity[0][0], word_input[0]))
                vis_list.append(thistuple)
            else:
                word = (model.wv[word_input])
                try:
                    vector_word = word.reshape(1, -1)
                    similarity = cosine_similarity(vector_cultural, vector_word)
                    thistuple = tuple((similarity[0][0], word_input))
                    vis_list.append(thistuple)
                except KeyError:
                    print('word not found')
                    word_input = word_input.replace('ß', 'ss')
                    vector_word = word.reshape(1, -1)
                    similarity = cosine_similarity(vector_cultural, vector_word)
                    thistuple = tuple((similarity[0][0], word_input))
                    vis_list.append(thistuple)
        except KeyError:
            print('keyerror')
            pass
    vis_list
    print(sorted(vis_list))
    return sorted(vis_list)

# visualization of cosine similarity
def plot_cosine_similarity(cos_similarities_1):
    fig = plt.figure(figsize=(6, 3))

    # Create the first polar plot
    ax1 = fig.add_subplot(121, projection='polar')
    for cos_sim, word in cos_similarities_1:
        # Map cosine similarity to 180-degree scale
        mapped_value = ((cos_sim + 1) / 2) * 180
        # Plot the mapping on the 180-degree scale
        ax1.plot([0, mapped_value * np.pi / 180], [0, 1], label=word + ' ' + str(cos_sim))
    ax1.set_title(args.in_file)
    # Add labels to each side
    ax1.text(np.deg2rad(0), 1.5, antonym_list[0][1], fontsize=12, ha='center')
    ax1.text(np.deg2rad(180), 1.5, antonym_list[0][0], fontsize=12, ha='center')
    ax1.set_thetamin(0)
    ax1.set_thetamax(180)
    ax1.set_theta_direction(-1)
    ax1.set_theta_zero_location('W')
    ax1.legend(bbox_to_anchor=(1, 0.85), loc='center', borderaxespad=0)

    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="calculation with word embeddings")
    parser.add_argument("in_file", type=str, help="input data: word vector format file")
    args = parser.parse_args()

    words = we_basics(args.in_file)
    plot_cosine_similarity(words)