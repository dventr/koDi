import pandas as pd
import re
import os

# Assuming the script is run from the directory containing the 'data_prep' folder
cwd = os.getcwd()
data_prep_path = os.path.join(cwd, 'data_prep') # dein ordnername



# Path to the CSV file
# Path to the CSV file
csv_file_path = os.path.join(data_prep_path, 'tp1p1_metadata.csv')
columns = ['text_id', 'text_date', 'text_section', 'text_source', 'text_text_type', 'text_title']

# Check if the CSV file exists
if not os.path.exists(csv_file_path):
    # If the file doesn't exist, create it
    # For example, create an empty DataFrame with the necessary columns
    empty_df = pd.DataFrame(columns=columns)
    empty_df.to_csv(csv_file_path, sep='\t', index=False)
    print(f"Created new file at {csv_file_path}")
else:
    # If the file exists, read it
    metadata_df = pd.read_csv(csv_file_path, sep='\t', low_memory=False, usecols=columns)

# Continue with the rest of your script...
csv_file_path = os.path.join(data_prep_path, 'tp1p1_metadata.csv')
metadata_df = pd.read_csv(csv_file_path, sep='\t', low_memory=False, usecols=['text_id', 'text_date', 'text_section', 'text_source', 'text_text_type', 'text_title'])

# Create a new DataFrame to hold the combined data
combined_data = []
 
# Relative path to the TXT file
txt_file_path = os.path.join(data_prep_path, 'sp1p1_1-export.txt')
with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
    text = txt_file.read()

# Pattern to extract text content between <text> tags
pattern = r'<text id="([^"]+)">([^<]+)</text>'
# Extract all text sections
results = re.findall(pattern, text)
result_dict = dict(results)

# Loop through each row in the CSV and extract the corresponding text from the .txt file
for index, row in metadata_df.iterrows():
    text_id = row['text_id']

    # Check if the text_id exists as a key in result_dict
    if text_id in result_dict:
        text = result_dict[text_id].strip()
        
        # Create a dictionary with the required values
        combined_row = {
            'text_id': text_id,
            'text_date': row['text_date'],
            'text_section': row['text_section'],
            'text_source': row['text_source'],
            'text_text_type': row['text_text_type'],
            'text_title': row['text_title'],
            'text_content': text
        }
        # Append the dictionary to the combined_data list
        combined_data.append(combined_row)
    else:
        pass

# Create a new DataFrame with the combined data
combined_df = pd.DataFrame(combined_data)
print(len(combined_data))

# Step 3: Adapt dates to a homogeneous format
combined_df['text_date'] = combined_df['text_date'].str.replace(r'^(\d{2})(\d{4})$', r'\2-\1', regex=True)
combined_df['text_date'] = combined_df['text_date'].str.replace(r'^(\d{4})(\d{2})(\d{2})$', r'\1-\2-\3', regex=True)
combined_df['text_date'] = combined_df['text_date'].str.replace('_', '-')
combined_df['text_date'] = combined_df['text_date'].str.replace('no-entry', '1989-01-01')

# Step 4: Save the new DataFrame to a new .csv file in the cwd
new_csv_file_path = os.path.join(cwd, 'subcorpus_tp1.csv')
combined_df.to_csv(new_csv_file_path, sep='\t', index=False)
