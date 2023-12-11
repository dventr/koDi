import glob
import json
import os
import csv  

# Set the path to the directory containing the JSON files
path = os.path.join('json_files')

# Create a list of all JSON files in the specified directory
file_list = glob.glob(os.path.join(path, '*.json'))

# Initialize lists to store messages, dates, and a dictionary for channel data
messages_list = []
date_list = []
channel_dict = {}
channel_id = []

# Iterate over each file in the file list
for file in file_list:
    # Open and read the JSON file
    with open(f'{file}', 'r') as f:
        try:
            # Load the JSON data
            data = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            # Skip file if JSON is not properly formatted
            pass
        # Process each entry in the JSON data
        for s in data:
            try:
                # Check if message length is greater than or equal to 30 characters
                if len(s['message']) >= 30:
                    # Append message, date, and channel ID to respective lists
                    messages_list.append(s['message'])
                    date_list.append(s['date'])
                    channel_id.append(s['peer_id']['channel_id'])
                    # Update the count of messages per channel in the dictionary
                    if s['peer_id']['channel_id'] in channel_dict:
                        channel_dict[s['peer_id']['channel_id']] += 1
                    else:
                        channel_dict[s['peer_id']['channel_id']] = 1
                else:
                    # Skip if the message is shorter than 30 characters
                    pass
            except KeyError:
                # Skip if key is missing in the JSON data
                pass

# Combine the lists into rows of data
combined_data = list(zip(messages_list, date_list, channel_id))

# Define the path for the CSV file where the data will be saved
csv_file_path = 'extracted_data.csv'

# Write the data to the CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header to the CSV file
    csv_writer.writerow(['message', 'date', 'channel_id'])
    
    # Write each row of combined data to the CSV file
    csv_writer.writerows(combined_data)

# Print the length of the messages list, date list, and the channel dictionary
print(len(messages_list))
print(len(date_list))
print(channel_dict)
