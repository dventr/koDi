# README for BERTopic

Further information on BERTopic: https://maartengr.github.io/BERTopic/api/bertopic.html
## Overview

This Jupyter Notebook is used for the analysis and visualization of text data using advanced NLP techniques, including BERTopic. The notebook covers several steps: data import, data processing, model building with BERTopic, and visualization of the results.

With korpus, topic modeling is performed for a corpus that can, depending on the research question, be divided into smaller text sets (time period or source).

### Requirements
	•	Installation of Python and Jupyter Notebook.
	•	Required Python libraries: plotly, matplotlib, pandas, numpy, sklearn, sentence_transformers, bertopic, hdbscan, umap-learn.
	•	The relevant data should be available in CSV format.

### Main Functions of the Notebook
	1.	Data import and preparation: Importing libraries and preparing the working environment.
	2.	Setting up the BERTopic model: Using transformer models to create topic models based on vectors.
	3.	Dimensionality reduction and clustering: Applying UMAP for dimensionality reduction and HDBSCAN for clustering.
	4.	Vectorization and text processing: Using CountVectorizer and ClassTfidfTransformer for text processing.
	5.	Analysis of specific corpora and time periods: Optional splitting of data into different corpora and time periods for targeted analysis.
	6.	Visualization of results: Creating various visualizations such as heatmaps, hierarchical representations, and dynamic graphs to display topics and their distribution.

### Usage
	1.	Prepare the data: Ensure that your data is in CSV format (see preprocessing) and stored in the same directory as the notebook.
	2.	Install libraries: Install the required libraries if they are not already installed.
	3.	Run the notebook: Execute the notebook cells in sequence to perform the analysis.
	4.	Check the results: Review the various visualizations and outputs to gain insights into your data.

### Notes
	•	The performance and accuracy of the analysis depend heavily on the quality and consistency of the input data.
	•	Code adjustments may be necessary to adapt it to specific data formats or analytical goals.
	•	Basic knowledge of Python and data analysis is recommended for effective use.
