import pandas as pd
import pickle
import os
# Read the CSV file
data = pd.read_csv('/Users/davideventre/Desktop/telegram_daten/data_prep/tp4p1_metadata.csv', sep='\t', low_memory=False, nrows= 100000)
tp = 'tp4'
# Adapt dates to a homogeneous format
data['text_date'] = data['text_date'].str.replace(r'^(\d{2})(\d{4})$', r'\2-\1-01', regex=True)
data['text_date'] = data['text_date'].str.replace(r'^(\d{4})(\d{2})(\d{2})$', r'\1-\2-\3', regex=True)
data['text_date'] = data['text_date'].str.replace('_', '-')

# Extract metadata columns
metadata = data[['text_id', 'text_date', 'text_page_title', 'text_section', 
                 'text_source', 'text_text_type', 'text_title', 'text_year']]

# Create output directories if they don't exist
txt_output_dir = f'{tp}_txt'
pkl_output_dir = f'{tp}_pkl'
os.makedirs(txt_output_dir, exist_ok=True)
os.makedirs(pkl_output_dir, exist_ok=True)

# Save each column as a separate file
for column in metadata.columns:
    column_data = metadata[column]
    txt_file_path = os.path.join(txt_output_dir, f'{column}_{tp}.txt')
    pkl_file_path = os.path.join(pkl_output_dir, f'{column}_{tp}.pkl')
    column_data.to_csv(txt_file_path, index=False, header=False)
    with open(pkl_file_path, 'wb') as file:
        pickle.dump(column_data, file)
