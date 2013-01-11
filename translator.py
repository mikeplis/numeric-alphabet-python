mapping = {
    'S': '0',
    'Z': '0',
    'ZH': '0',
    'T': '1',
    'D': '1',
    'N': '2',
    'M': '3',
    'R': '4',
    'ER': '4',
    'L': '5',
    'SH': '6',
    'JH': '6',
    'CH': '6',
    'TH': '6',
    'DH': '6',
    'G': '7',
    'K': '7',
    'F': '8',
    'V': '8',
    'B': '9',
    'P': '9'
    }

# vowels = ["AH", "IH", "IY", "EH", "AA", "AE", "EY", "AO", "AY", "AW", "OY", "UH", "Y"]
# unused = ["W", "HH", "NG"]
dict_ = {} # stores dictionary word with number translation

def phonemes_to_numstring(phoneme_array):
    numstring = ''
    for phoneme in phoneme_array:
        numstring += mapping[phoneme]
    return numstring

with open('dict1.txt') as d_file:
    for line in iter(lambda: d_file.readline(), ''):
        line = line.split()
        try:
            dict_[line[0]] = phonemes_to_numstring(line[1:])
        except KeyError:
            continue

with open('freq_list.txt') as freq_list, open('dict2.txt', 'w+') as new_dict:
    freq_list.readline()
    for line in iter(lambda: freq_list.readline(), ''):
        line = line.split()
        try:
            new_dict.write(line[1].upper() + ' ' + dict_[line[1].upper()] + '\n')
        except KeyError:
            continue



"""while True:
    root_mapping = []
    words = [[] for _ in range(10)]
    try:
        input_string = input("Number to translate: ")
        if len(input_string) == 0:
            print("You didn't enter anything, try again.")
            continue
    except KeyError:
        print("That string contained a character that's not a number. Try again: ")
    for key in dict_:
        try:
            words[input_string.index(dict_[key])].append(key)
        except ValueError:
            continue
        except KeyError:
            continue
        
    for init_word in words[0]:
    init_word = words[0][0]
    index = len(dict_[init_word])
    output = init_word + ' '
    while index < len(input_string):
        output += words[index][0] + ' '
        index += len(dict_[words[index][0]])
    print(output)"""
        
        
