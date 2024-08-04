import os
from fuzzywuzzy import process

# Load the database from the txt file
database = {}
with open('database.txt', 'r', encoding='utf-8') as f:
    for line in f:
        id, name = line.strip().split(' = ')
        database[id] = name

# Ask the user for the directory
root_folder = input("Enter the directory path: ")

# Check if the directory exists
if not os.path.exists(root_folder):
    print("Directory not found!")
    exit()

# Iterate over all folders in the specified folder
for folder in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder)
    if os.path.isdir(folder_path):
        # Perform a fuzzy search on the folder name
        matches = process.extract(folder, database.values(), limit=1)
        if matches:
            best_match = matches[0]
            for id, name in database.items():
                if name == best_match[0]:
                    new_name = f"{name} [{id}]"
                    os.rename(folder_path, os.path.join(root_folder, new_name))
                    print(f"Renamed folder {folder} to {new_name}")
                    break
