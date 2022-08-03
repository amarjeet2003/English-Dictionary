import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        choice_y_n = input("Did u mean %s instead?, Enter Y for Yes or N for No :" % get_close_matches(w, data.keys())[0])
        if choice_y_n == "Y" or "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif choice_y_n == "N" or "n":
            return "The Word doesn't exist. Please double check it"
    else:
        return "We didin't understand your entry"

word = input("Enter Word:")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
