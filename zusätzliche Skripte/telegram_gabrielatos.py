import glob
import json
import os
import csv
import re
import math

path = os.path.join('json_files')
file_list = glob.glob(os.path.join(path, '*.json'))

# Data should be passed in the form of a list
messages_list = []
date_list = []
channel_dict = {}
channel_names = {}
channel_id = []
view_list = []
forwardscount_list = []
x = 0

# Compile the regex pattern for "solidar"
solidar_patterns = [
    "soziale", "Teilhabe",
    "solidari",  # "solidarisch", "Solidarität"
    "sozial",
    "arbeitsfähig", "arbeitsunfähig",
    "altersvorsorge",
    "Anteilnahme",
    "berufsunfähig",
    "Benachteiligung",
    "behindert", 
    "Behinderung",
    "Betreuungsangebot",
    "bevormundung",
    "Bildungszug",
    "chancengerechtigkeit",
    "diskrimin",
    "Ein-Euro-Job",
    "fairness",
    "mindestlohn",
    "Mitfinanzierung",
    "nutznie(ß|ss)er",
    "finanzkrise",
    "flüchtling", "Flüchtlingskrise",
    "geflüchtet",
    "Chancengleichheit", "ungleichheit",
    "gleichberechtigt",
    "gegenseitig", "unterstützen",
    "gemeinschaft",
    "gemeinsinn",
    "gesellschaftstragend",
    "Wertegesellschaft",
    "integrieren",
    "invalid", "invalide",
    "Zugang",
    "klassengesellschaft",
    "Kita",
    "krisenregion",
    "krisenzeiten",
    "kollektiverantwortung",
    "lebensqualität",
    "leiharbeit",
    "menschenfreundlich",
    "Riester-Rente",
    "Pflegeversicherung", "Bürgerversicherung", "Rentenversicherung", "Unfallversicherung", "Krankenversicherung",
    "Minderheiten",
    "Menschenrechte",
    "Partizipation",
    "privilegiert", "nicht privilegiert", "unterprivilegiert",
    "selbstbestimmung",
    "sozialarbeit",
    "soziale Arbeit",
    "Sozialwerk",
    "Tagesstätte",
    "Teilzeitarbeit",
    "Mitverantwortung", "Eigenverantwortung",
    "Wertschätzung",
    "Working Poor"
] # Add more keywords as needed
for file in file_list:
    with open(f'{file}', 'r') as f:
        try:
            data = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            pass
        for s in data:
            try:
                telegram_messages = s['message']
                if any(keyword in telegram_messages.lower() for keyword in solidar_patterns):
                        messages_list.append(telegram_messages)
                        date_list.append(s['date'])
                        view_list.append(math.floor(s['views'] / 10000) * 10000)
                        forwardscount_list.append(math.floor(s['forwards'] / 10) * 10)
                        channel_id.append(s['peer_id']['channel_id'])
                        if s['peer_id']['channel_id'] in channel_dict:
                            channel_dict[s['peer_id']['channel_id']] += 1
                        else:
                            channel_dict[s['peer_id']['channel_id']] = 1
                else:
                    pass
            except KeyError:
                pass

# Write the header
channel_name = {}
for file in file_list:
    with open(file, 'r') as f:
        try:
            files = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            pass
        for s in files:
            try:
                value = (s['action']['title'])
                key = (s['peer_id']['channel_id'])
                channel_name[key] = value
            except (KeyError, TypeError):
                pass
name_list = []
for i in channel_id:
    name_list.append(channel_name[i])

# Combine the lists into rows of data
combined_data = list(zip(messages_list, date_list, name_list, view_list, forwardscount_list))

# Define the CSV file path
csv_file_path = 'telegram_data.csv'

# Write the data to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header
    csv_writer.writerow(['message', 'date', 'channel_id', 'view_list', 'forwards'])
    # Write the data rows
    csv_writer.writerows(combined_data)

# Convert the dictionary to a list of dictionaries with the desired header names
formatted_data = [{"channel": key, "nr of texts": value} for key, value in channel_dict.items()]
# Specify the CSV file path
csv_file_path = "channel_counts.csv"
# Write the data to CSV
with open(csv_file_path, "w", newline="") as csv_file:
    fieldnames = ["channel", "nr of texts"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()  # Write the header
    writer.writerows(formatted_data)  # Write the data
    
print(len(messages_list))
print(len(date_list))
print(x)