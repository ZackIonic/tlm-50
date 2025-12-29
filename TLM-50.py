# 50 line TLM Made by ZackIonic

import random
import urllib.request

reader = urllib.request.urlopen("https://raw.githubusercontent.com/ZackIonic/llm-50/refs/heads/main/tlm-context").read().decode('utf-8')

window = []
successor_map = {}

for line in reader.splitlines():
    line = line.strip('_')
    for word in line.split():
        word = word.strip('_')
        window.append(word)
        if len(window) == 4:
            key = (window[0], window[1], window[2])
            value = window[3]
            if key not in successor_map:
                successor_map[key] = [value]
            else:
                successor_map[key].append(value)
            window.pop(0)

while True:
    words = []
    sentences = 0
    while len(words) != 3:
        words = input("Context: ").split()
        if len(words) != 3:
            print('Please input 3 words of context.')
    word1 = str(words[0])
    word2 = str(words[1])
    word3 = str(words[2])
    length = int(input("Number of sentences: "))

    while True:
        if ((word1, word2, word3)) in successor_map:
            print(word1, end=' ')
            if '.' in word1 or '!' in word1 or '?' in word1:
                sentences += 1
                if sentences >= length:
                    break
            successors = successor_map[(word1, word2, word3)]
            word1, word2, word3 = word2, word3, random.choice(successors)
        else:
            print("\n ERROR: No matches found for \'" + word1 + " " + word2 + " " + word3 + "\'")
            break

    print('\n')

