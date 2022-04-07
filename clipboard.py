import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

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




if len(sys.argv) == 2:
    command = sys.argv[1]
    data = loadItems(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        saveItems(SAVED_DATA, data)
        print("Data successfully saved!")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard!")
        else:
            print("Key does not exist.")


    elif command == "list":
        print(data)

    elif command == "delete":
        key = input("Enter a key: ")
        if key in data:
            del data[key]
            saveItems(SAVED_DATA, data)
        else:
            print("Key does not exist.")

    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")



