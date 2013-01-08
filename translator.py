mapping = {
    "0": ["S", "Z"],
    "1": ["T", "D"],
    "2": ["N"],
    "3": ["M"],
    "4": ["R", "ER"],
    "5": ["L"],
    "6": ["SH", "JH", "CH", "TH"],
    "7": ["G", "K"],
    "8": ["F", "V"],
    "9": ["B", "P"]
    }

# vowels = ["AH", "IH", "IY", "EH", "AA", "AE", "EY", "AO", "AY", "AW", "OY", "UH"]
dict_ = {}

def findIndices(root_number, dict_word):
    """ find starting and ending index of dict word phonemes in root number """
    pass
        
        

class WordNode(object):
    def __init__(self, word, start_index, end_index):
        self.word = word
        self.start_index = start_index
        self.end_index = end_index
    

with open("dict1.txt") as d_file:
    for line in iter(lambda: d_file.readline(), ""):
        line = line.split()
        dict_[line[0]] = line[1:]



while True:
    root_mapping = []
    words = []
    try:
        input_string = input("Number to translate: ")
        for number in input_string:
            root_mapping.append(mapping[number])
    except KeyError:
        print("That string contained a character that's not a number. Try again: ")

    for key in dict_:
        if len(dict_[key]) == len(root_mapping):            
            for index, t in enumerate(root_mapping):
                try:
                    if dict_[key][index] not in t:
                        break
                except IndexError:
                    break
            else:
                words.append(key)

    print(words)
        