from sklearn import cluster
from gensim.models.word2vec import Word2Vec
import pickle
import pandas as pd
import numpy as np
from scipy.spatial import distance
import numpy as np
import matplotlib.pyplot as plt
import argparse
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from matplotlib import colors
import mplcursors
import plotly.offline as pyo
import plotly.graph_objects as go
import mpld3


# Diese Funktion sortiert ein Dictionary (Voraussetzung: Zahlen als Werte)
def sort_dict(dic, reverse=True):
    return dict(sorted(dic.items(), key=lambda item: item[1], reverse=reverse))


# Diese Funktion ermittelt zu den Korpusdateien Type-Frequenzen. Voraussetzung: Format ein Satz pro Zeile, jedes Token zwischen zwei Leerzeichen
def get_word_frequencies(path_to_txt):
    frequencies = {}

    with open(path_to_txt, "r") as f:
        for line in f.readlines():
            for word in line.split():
                if word in frequencies:
                    frequencies[word] += 1
                else:
                    frequencies[word] = 1

    return sort_dict(frequencies)


# Mit den folgenden zwei Funktionen können wir die Schritte bündeln (-> in lib.py enthalten)


# Diese Funktion berechnet das Modell.
# Wir übergeben den Pfad zum Word-Embedding-Modell, das geclustert werden soll,
# die Anzahl der Cluster k sowie optional einen Pfad zum Sichern des fertigen kmeans-Modells.
# Wird hier kein Pfad übergeben, wird das Modell im gleichen Ordner wie das WE-Modell gesichert.
# Außerdem können wir optional eine Mindestfrequenz für die Types des Korpus sowie ein entsprechendes Dictionary, in dem diese ausgezählt sind, übergeben.
# Ein Funktionsaufruf zum trainieren unseres obigen Modells  könnte so aussehen:
# kmeans = compute_kmeans("model/sentences_paris_min_count.model", k=93, min_count=100, freq_dict=freqs["paris"])


def compute_kmeans(
    path_to_we_model, k, path_to_save=None, min_count=None, freq_dict=None
):
    model = Word2Vec.load(path_to_we_model)
    words = model.wv.vocab.keys()
    word_vectors = model.wv[words]

    if min_count is not None and freq_dict is not None:
        words = []
        for word in model.wv.vocab.keys():
            if freq_dict[word] >= min_count:
                words.append(word)

        word_vectors = model.wv[words]

    kmeans = cluster.KMeans(n_clusters=k)
    kmeans.fit(word_vectors)

    if path_to_save is None:
        with open(path_to_we_model + ".kmeans.pkl", "wb") as f:
            pickle.dump(kmeans, f)
    else:
        with open(path_to_save, "wb") as f:
            pickle.dump(kmeans, f)

    return kmeans


# Dieser Funktion übergeben wir das kmeans- und das WE-Modell.
# Jeweils können wir entweder das Modell als Variable übergeben oder einen Pfad zum Speicherort
# Zurück bekommen wir die verschiedenen oben erstellten Dictionaries, die wir als Variablen speichern müssen
# Ein Funktionsaufruf könnte so aussehen:
# word_cluster, cluster_words, cluster_centroid, cluster_label = load_kmeans("model/sentences_paris_min_count.model.kmeans.pkl", "model/sentences_paris_min_count.model")
def load_kmeans(kmeans, we_model):
    if type(we_model) == str:
        we_model = Word2Vec.load(we_model)

    words = we_model.wv.vocab.keys()

    if type(kmeans) == str:
        with open(kmeans, "rb") as f:
            kmeans = pickle.load(f)

    word_cluster = dict(zip(words, kmeans.labels_))
    cluster_centroid = dict(
        zip(range(len(kmeans.cluster_centers_)), kmeans.cluster_centers_)
    )
    df = pd.DataFrame(word_cluster.items(), columns=["word", "cluster"])
    df["sim"] = [
        1 - distance.cosine(we_model[word], cluster_centroid[word_cluster[word]])
        for word in df["word"]
    ]
    df = df.sort_values(by=["cluster", "sim"], ascending=[True, False])

    cluster_words = {}

    for i, row in df.iterrows():
        if row["cluster"] in cluster_words:
            cluster_words[row["cluster"]].append(row["word"])
        else:
            cluster_words[row["cluster"]] = [row["word"]]

    cluster_label = {}

    for cluster, words in cluster_words.items():
        cluster_label[cluster] = "|".join(words[:3])

    return word_cluster, cluster_words, cluster_centroid, cluster_label


def time_machine(model1, model2, word_or_vec):
    if type(word_or_vec) == str:
        embedding = model1[word_or_vec]
    else:
        embedding = word_or_vec
    return model2.most_similar([embedding])


def get_most_similar_clusters(vec, cluster_centroid, cluster_label, topn=10):
    cluster_cosim = {}
    for cluster, centroid in cluster_centroid.items():
        cluster_cosim[cluster] = 1 - distance.cosine(cluster_centroid[cluster], vec)
    cluster_cosim = sort_dict(cluster_cosim)
    n_printed = 0
    for cluster_id, cosim in cluster_cosim.items():
        print(cluster_label[cluster_id], round(cosim, 2))
        n_printed += 1
        if n_printed == topn:
            break
    return cluster_cosim


def get_most_distant_clusters(
    model1, cluster_words_model1, cluster_label_model1, model2
):
    cluster_distance = {}

    for cluster, words in cluster_words_model1.items():
        try:
            distances = [
                distance.cosine(model1[word], model2[word])
                for word in words
                if word in model2
            ]
            if len(distances) > 0:
                cluster_distance[cluster_label_model1[cluster]] = np.mean(distances)
        except KeyError:
            pass
    return sort_dict(cluster_distance)

import numpy as np
import matplotlib.pyplot as plt
import argparse
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from matplotlib import colors
import mplcursors
import plotly.offline as pyo
import plotly.graph_objects as go

def calculate_and_visualize_cosine_similarity(input_file, input_special, antonym_list, antonym_list_2, word_list):
    # Load the Word2Vec model
    model = Word2Vec.load(input_file)
    model1 = Word2Vec.load(input_special)
    # Define a function to calculate cosine similarity
    def calculate_cosine_similarity(word_list, antonym_list, model):
        vis_list = []
        cultural_dim = 0

        # Calculate the semantic dimension based on antonym pairs
        for key, value in antonym_list:
            try:
                x = model.wv[key] - model.wv[value]
                cultural_dim += x
            except KeyError:                
                antonym_list = [word.replace('ß', 'ss') if isinstance(word, str) else (word[0].replace('ß', 'ss'), word[1].replace('ß', 'ss')) for word in antonym_list]
                try:
                    for key, value in antonym_list:
                        x = model.wv[key] - model.wv[value]
                        cultural_dim += x
                except KeyError:
                    print(f'KeyError: {input_file}: {key}, {value}')
                    pass
        # Calculate the average semantic dimension
        with_div = cultural_dim / len(antonym_list)
        vector_cultural = with_div.reshape(1, -1)

        # Compare each word in the word_list with the semantic dimension
        for word_input in word_list:
            try:
                if type(word_input) is tuple:
                    synonyms = 0
                    for word_syn in word_input:
                        try:
                            synonym = model1.wv[word_syn]
                            synonyms += synonym
                        except KeyError:
                            synonym = model1.wv[word_syn]
                            synonyms += synonym
                            pass
                    vector_word = (synonyms / len(word_input)).reshape(1, -1)
                    similarity = cosine_similarity(vector_cultural, vector_word)
                    thistuple = tuple((similarity[0][0], word_input[0]))
                    vis_list.append(thistuple)
                else:
                    try:
                        vector_word = model1.wv[word_input].reshape(1, -1)
                        similarity = cosine_similarity(vector_cultural, vector_word)
                        thistuple = tuple((similarity[0][0], word_input))
                        vis_list.append(thistuple)
                    except KeyError:
                        vector_word = model1.wv[word_input].reshape(1, -1)
                        similarity = cosine_similarity(vector_cultural, vector_word)
                        thistuple = tuple((similarity[0][0], word_input))
                        vis_list.append(thistuple)
                        pass   
            except KeyError:
                word_list = [word.replace('ß', 'ss') if isinstance(word, str) else (word[0].replace('ß', 'ss'), word[1].replace('ß', 'ss')) for word in word_list]
                for word_input in word_list:
                    if type(word_input) is tuple:
                        synonyms = 0
                        for word_syn in word_input:
                            try:
                                synonym = model1.wv[word_syn]
                                synonyms += synonym
                            except KeyError:
                                synonym = model1.wv[word_syn]
                                synonyms += synonym
                                pass
                        vector_word = (synonyms / len(word_input)).reshape(1, -1)
                        similarity = cosine_similarity(vector_cultural, vector_word)
                        thistuple = tuple((similarity[0][0], word_input[0]))
                        vis_list.append(thistuple)
                    else:
                        try:
                            vector_word = model1.wv[word_input].reshape(1, -1)
                            similarity = cosine_similarity(vector_cultural, vector_word)
                            thistuple = tuple((similarity[0][0], word_input))
                            vis_list.append(thistuple)
                        except KeyError:
                            vector_word = model1.wv[word_input].reshape(1, -1)
                            similarity = cosine_similarity(vector_cultural, vector_word)
                            thistuple = tuple((similarity[0][0], word_input))
                            vis_list.append(thistuple)
                            print(f'folgendes Wort nicht vorhanden: {word_input}, {input_file}')
                            pass
        return vis_list

    def plot_cosine_similarity(cos_similarities_y, cos_similarities_x):
        fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size as needed

        # Extract data
        y_values = [word_y for _, word_y in cos_similarities_y]
        y_scores = [((cos_sim_y + 1) / 2) * 180 for cos_sim_y, _ in cos_similarities_y]

        x_values = [word_x for _, word_x in cos_similarities_x]
        x_scores = [((cos_sim_x + 1) / 2) * 180 for cos_sim_x, _ in cos_similarities_x]

        cmap = plt.get_cmap('plasma')

        # Normalize the scores
        norm = colors.Normalize(vmin=min(y_scores + x_scores), vmax=max(y_scores + x_scores))
        scalar_map = plt.cm.ScalarMappable(norm=norm, cmap=cmap)

        # Create a scatter plot with improved aesthetics
        scatter = ax.scatter(y_scores, x_scores, c=y_scores, cmap=cmap, s=100, alpha=0.7, edgecolors='w', linewidth=0.5)

        # Annotate the points with the words as hover tooltips using mplcursors
        tooltips = mplcursors.cursor(scatter, hover=True)
        tooltips.connect("add", lambda sel: sel.annotation.set_text(f"{y_values[sel.target.index]} ({y_scores[sel.target.index]:.2f}, {x_values[sel.target.index]}, {x_scores[sel.target.index]:.2f})"))

        ax.set_xlim(-10, 190)
        ax.set_ylim(-10, 190)

        # Add labels and title
        ax.set_xlabel(antonym_list_2[0][0], loc="right")
        ax.set_ylabel(antonym_list[0][0], loc="top")
        ax.set_title(f'Cosine Similarity: {input_file}', fontsize=14)

        # Add colorbar
        cbar = plt.colorbar(scalar_map)
        cbar.set_label('Angle', fontsize=12)

        # Customize tick labels and legend as needed
        ax.tick_params(axis='both', which='both', labelsize=12)
        
        plt.tight_layout()
        plt.grid(True, linestyle='--', alpha=0.5)  # Add grid lines for reference

            # Create a table to display data
        table_data = [(word, y_score, x_score) for word, y_score, x_score in zip(y_values, y_scores, x_scores)]
        col_labels = ["Word", "Y Score", "X Score"]
        table = ax.table(cellText=table_data, colLabels=col_labels, loc="bottom", cellLoc='center')

        # Customize table appearance
        table.auto_set_font_size(False)
        table.set_fontsize(15)
        table.scale(1, 1.5)
        table.auto_set_column_width([0, 1, 2])
        
        # Hide the table initially
        table.set_visible(False)
        ax.add_table(table)
            
        # Create a zoom-in function
        def on_click(event):
            if event.button == 1 and event.inaxes == ax:
                table.set_visible(False)
                ax.set_xlim(-10, 190)
                ax.set_ylim(-10, 190)
                plt.draw()

        # Connect the zoom-in function to mouse button clicks
        fig.canvas.mpl_connect('button_press_event', on_click)

        # Create a Plotly figure
        plotly_fig = go.Figure()

        # Add scatter traces to the Plotly figure
        plotly_fig.add_trace(go.Scatter(
            x=x_scores,
            y=y_scores,
            mode='markers',  # Display data points
            marker=dict(
                size=10,
                color=y_scores,
                colorscale='plasma',
                opacity=0.7,
                line=dict(width=0.5, color='white')
            ),
            hovertext=table_data,  # Define hover text
            hoverinfo='text',  # Show hover text
            hovertemplate="%{hovertext}<extra></extra>",  # Custom hover template
        ))
        # Update the layout of the Plotly figure
        plotly_fig.update_layout(
            title=f'Cosine Similarity: {input_file}',
            xaxis=dict(range=[-10, 190]),
            yaxis=dict(range=[-10, 190]),
            xaxis_title=antonym_list_2[0][0],
            yaxis_title=antonym_list[0][0],
            coloraxis_colorbar=dict(title='Angle'),

        )
        # Connect the zoom-in function to mouse button clicks
        fig.canvas.mpl_connect('button_press_event', on_click)
        filename=f'{input_file}.html'
        # Writing the content to the file
        with open(filename, "w") as file:
            file.write(file_content)
        pyo.plot(plotly_fig, filename)
        pyo.iplot(plotly_fig)
        plt.show()

# Refactoring the provided code into a function

def we_basics(infile, antonym_list, word_list):
    model = Word2Vec.load(infile)
    # A word list can be entered as a string 'Maske' or as a tuple ('Maske', 'FFP2') for very similar words.
    # Note: For the Telegram model, the character 'ß' must be used (for the KD model, 'ß' can be retained).
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
def plot_cosine_similarity(cos_similarities_1, antonym_list, word_list):
    fig = plt.figure(figsize=(6, 3))

    # Create the first polar plot
    ax1 = fig.add_subplot(121, projection='polar')
    for cos_sim, word in cos_similarities_1:
        # Map cosine similarity to 180-degree scale
        mapped_value = ((cos_sim + 1) / 2) * 180
        # Plot the mapping on the 180-degree scale
        ax1.plot([0, mapped_value * np.pi / 180], [0, 1], label=word + ' ' + str(cos_sim))
    ax1.set_title('Cosine similarity')
    # Add labels to each side
    ax1.text(np.deg2rad(0), 1.3, antonym_list[0][1], fontsize=12, ha='center')
    ax1.text(np.deg2rad(180), 1.3, antonym_list[0][0], fontsize=12, ha='center')
    ax1.set_thetamin(0)
    ax1.set_thetamax(180)
    ax1.set_theta_direction(-1)
    ax1.set_theta_zero_location('W')
    ax1.legend(bbox_to_anchor=(2, 0), loc='center', borderaxespad=0)
    plt.show()

def plot_cosine_similarity2(cos_similarities_y, cos_similarities_x, antonym_list, antonym_list2, word_list):
    fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size as needed

    # Extract data
    y_values = [word_y for _, word_y in cos_similarities_y]
    y_scores = [((cos_sim_y + 1) / 2) * 180 for cos_sim_y, _ in cos_similarities_y]

    x_values = [word_x for _, word_x in cos_similarities_x]
    x_scores = [((cos_sim_x + 1) / 2) * 180 for cos_sim_x, _ in cos_similarities_x]

    cmap = plt.get_cmap('plasma')

    # Normalize the scores
    norm = colors.Normalize(vmin=min(y_scores + x_scores), vmax=max(y_scores + x_scores))
    scalar_map = plt.cm.ScalarMappable(norm=norm, cmap=cmap)

    # Create a scatter plot with improved aesthetics
    scatter = ax.scatter(y_scores, x_scores, c=y_scores, cmap=cmap, s=100, alpha=0.7, edgecolors='w', linewidth=0.5)

    # Annotate the points with the words as hover tooltips using mplcursors
    tooltips = mplcursors.cursor(scatter, hover=True)
    tooltips.connect("add", lambda sel: sel.annotation.set_text(f"{y_values[sel.target.index]} ({y_scores[sel.target.index]:.2f}, {x_scores[sel.target.index]:.2f})"))

    ax.set_xlim(-10, 190)
    ax.set_ylim(-10, 190)

    # Add labels and title
    ax.set_xlabel(antonym_list2[0][0], loc="right")
    ax.set_ylabel(antonym_list[0][0], loc="top")
    ax.set_title(f'Cosine Similarity', fontsize=14)

    # Add colorbar
    cbar = plt.colorbar(scalar_map)
    cbar.set_label('Angle', fontsize=12)

    # Customize tick labels and legend as needed
    ax.tick_params(axis='both', which='both', labelsize=12)
    
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.5)  # Add grid lines for reference

    # Create a table to display data
    table_data = [(word, y_score, x_score) for word, y_score, x_score in zip(y_values, y_scores, x_scores)]
    col_labels = ["Word", "Y Score", "X Score"]
    table = ax.table(cellText=table_data, colLabels=col_labels, loc="bottom")
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    # Hide the table initially
    table.set_visible(True)

    
     # Create a zoom-in function
    def on_click(event):
        if event.button == 1 and event.inaxes == ax:
            table.set_visible(False)
            ax.set_xlim(-10, 190)
            ax.set_ylim(-10, 190)
            plt.draw()

    # Connect the zoom-in function to mouse button clicks
    fig.canvas.mpl_connect('button_press_event', on_click)

    # Create a Plotly figure
    plotly_fig = go.Figure()

     # Add scatter traces to the Plotly figure
    plotly_fig.add_trace(go.Scatter(
        x=y_scores,
        y=x_scores,
        mode='markers',  # Display data points
        marker=dict(
            size=10,
            color=y_scores,
            colorscale='plasma',
            opacity=0.7,
            line=dict(width=0.5, color='white')
        ),
        hovertext=word_list,  # Define hover text
        hoverinfo='text',  # Show hover text
        hovertemplate="%{hovertext}<extra></extra>",  # Custom hover template
    ))
    # Update the layout of the Plotly figure
    plotly_fig.update_layout(
        title=f'Cosine Similarity',
        xaxis=dict(range=[-10, 190]),
        yaxis=dict(range=[-10, 190]),
        xaxis_title=antonym_list2[0][0],
        yaxis_title=antonym_list[0][0],
        coloraxis_colorbar=dict(title='Angle'),
    )
    # Connect the zoom-in function to mouse button clicks
    fig.canvas.mpl_connect('button_press_event', on_click)
    pyo.plot(plotly_fig, filename='cosine_similarity_plot.html')
    pyo.iplot(plotly_fig)

    plt.show()
