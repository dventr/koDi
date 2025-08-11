# README for TWEC

## Overview
This script provides a comprehensive pipeline for processing and analyzing text data, particularly for comparing text sources and time periods. It is based on the application of **TWEC** (Temporal Word Embeddings with a Compass) and other text processing methods. The script is modular, with each section responsible for specific tasks in the data processing workflow.

## Dependencies
- **Pandas**: For reading and processing CSV files.  
- **NLTK** or **SpaCy**: For tokenizing the texts.  
- **TWEC** and **Gensim**: For training and using word embeddings.  
- **Multiprocessing**: To speed up computations via parallel processing.  

### Installation
Before using the script, install the required libraries via `pip`:
```bash
pip install -r requirements.txt
```
## Script Components
1. **Data Preparation**: Import your CSV files and initialize data structures.  
2. **Source Comparison**: Load and categorize text data by source.  
3. **Time Period Comparison**: Load and sort texts by date to enable cross-period comparisons.  
4. **Tokenization**: Convert texts into tokens using either NLTK or SpaCy, depending on your preference.  
5. **Frequency Dictionaries**: Create dictionaries mapping word frequencies in the texts.  
6. **TWEC**: Initialize and train TWEC to create temporal word embeddings.  
7. **Model Saving**: Save trained models for later use and analysis.  

## Usage Notes
- **Data Import**: Adjust the paths to your CSV files as needed.  
- **Tokenization**: Ensure the correct language setting when tokenizing.  
- **TWEC Training**: Be aware that TWEC training can be computationally intensive. Make sure your hardware meets the requirements.  

## Additional Information
This script is based on Tim Feldmüller’s implementation of TWEC, which is available at the following [GitLab link](https://gitlab.uzh.ch/zukoko/sommerschule-2023/-/tree/master/C5-Distributionelle-Semantik/TWEC_Clustering/scripts?ref_type=heads). For more detailed explanations and examples, visit the linked page.
