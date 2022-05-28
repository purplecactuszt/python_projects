import sys
import json
import os
import time

SAVED_DATA = "notes.json"
opens = "opened.txt"

def saveItems(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def loadItems(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return{}
def save_to_notepad_and_open(filepath, key):
    try:
        with open(opens, "w") as n:
            n.write(data[key])
    except:
        return{}

command = input("Enter a command: ")
data = loadItems(SAVED_DATA)

if command == "save":
    key = input("Enter a key: ")
    data[key] = input("Enter a note: ")
    saveItems(SAVED_DATA, data)
    print("Data successfully saved!")
    time.sleep(2)

elif command == "list":
    print("\nKeys: ")
    for key, value in data.items():
        print(key)
    print('')
    time.sleep(4)


elif command == "load":
    key = input("Enter a key: ")
    if key in data:
        save_to_notepad_and_open(opens, key)
        os.startfile("opened.txt")
    else:
        print("Key does not exist.")
        time.sleep(2)

elif command == "delete":
    key = input("Enter a key: ")
    if key in data:
        del data[key]
        saveItems(SAVED_DATA, data)
        print("Data successfully deleted!")
        time.sleep(2)
    else:
        print("Key does not exist.")
        time.sleep(2)

else:
    print("Unknown command")
