import os
from fuzzywuzzy import process

database = {}
with open('database.txt', 'r', encoding='utf-8') as f:
    for line in f:
        id, name = line.strip().split(' = ')
        database[id] = name

root_folder = input("Enter the directory path: ")

if not os.path.exists(root_folder):
    print("Directory not found!")
    exit()

for folder in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder)
    if os.path.isdir(folder_path):
        matches = process.extract(folder, database.values(), limit=1)
        if matches:
            best_match = matches[0]
            for id, name in database.items():
                if name == best_match[0]:
                    new_name = f"{name} [{id}]"
                    os.rename(folder_path, os.path.join(root_folder, new_name))
                    print(f"Renamed folder {folder} to {new_name}")
                    break
