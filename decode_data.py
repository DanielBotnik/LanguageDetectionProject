import pandas as pd
import numpy as np

keymap = {
    'א':1,
    'ב':2,
    'ג':3,
    'ד':4,
    'ה':5,
    'ו':6,
    'ז':7,
    'ח':8,
    'ט':9,
    'י':10,
    'כ':11,
    'ל':12,
    'מ':13,
    'נ':14,
    'ס':15,
    'ע':16,
    'פ':17,
    'צ':18,
    'ק':19,
    'ר':20,
    'ש':21,
    'ת':22,
    'q':28,
    'w':29,
    'e':19,
    'r':20,
    't':1,
    'y':9,
    'u':6,
    'i':23,
    'ן':23,
    'o':24,
    'ם':24,
    'p':17,
    'a':21,
    's':4,
    'd':3,
    'f':11,
    'g':16,
    'h':10,
    'j':8,
    'k':12,
    'l':25,
    'ך':25,
    'ף':26,
    'z':7,
    'x':15,
    'c':2,
    'v':5,
    'b':14,
    'n':13,
    'm':18,
    'ץ':27,
}

reverse_keymap = {
    1: 't',
    2: 'c',
    3: 'd',
    4: 's',
    5: 'v',
    6: 'u',
    7: 'z',
    8: 'j',
    9: 'y',
    10: 'h',
    11: 'f',
    12: 'k',
    13: 'n',
    14: 'b',
    15: 'x',
    16: 'g',
    17: 'p',
    18: 'm',
    19: 'e',
    20: 'r',
    21: 'a',
    22: ',',
    23: 'i',
    24: 'o',
    25: 'l',
    26: ';',
    27: '.',
    28: 'q',
    29: 'w',
}

def decode_word(word):
    try:
        decoded_string = ''
        for char in word:
            decoded_string += reverse_keymap[keymap[char]]
    except:
        print(word)
        
    return decoded_string

def get_words_from_file(filename):
    with open(filename,encoding='utf8') as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    return content

if __name__ == '__main__':
    df = pd.DataFrame(columns=['word','decoded_word','language'])
    words = get_words_from_file('english_words.txt')
    for word in words:
        df = df.append({'word':word,'decoded_word':decode_word(word),'language':'english'},ignore_index=True)
    words = get_words_from_file('hebrew_words.txt')
    for word in words:
        df = df.append({'word':word,'decoded_word':decode_word(word),'language':'hebrew'},ignore_index=True)
    df.sample(frac=1).reset_index(drop=True).to_csv('dataset.csv',encoding='utf8',index=False)
    print(df)