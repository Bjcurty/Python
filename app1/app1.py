# Brad Curtis
# 3/11/2020
# Program to input a word from a user and match it to a definition
# Inluenced by The Python Mega Course taught by Ardit Sulce
import json
from difflib import get_close_matches

# This loads our dictionary file for use
data = json.load(open("data.json"))

# Method to lookup a definition located in the given dictionary from the given key
def dict_lookup(data, key):
    matches = get_close_matches(key, data.keys())
    if key in data:
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif key.upper() in data:
        return data[key.upper()]
    elif matches != []:
        for m in matches:
            choice = input("Did you mean this word: %s (y/n) " % m)
            if choice.lower() == 'y':
                return data[m]
            elif choice.lower() != 'n':
                return "This is not a valid entry."
        return "This word does not exist. Please check for spelling mistakes."
    else:
        return "This word does not exist. Please check for spelling mistakes."

# Word input from the user to be a key for the dictionary
key = input("Input a word to search for: ").lower()

# Returns the definition
output = dict_lookup(data, key)
if type(output) == list:
    for o in output:
        print(o)
else:
    print(output)
