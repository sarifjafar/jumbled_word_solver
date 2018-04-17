from itertools import permutations as npr
import json

data = json.load(open("wordsEn.json"))
print('Enter String->')
input_str = str(input()).lower().strip()
permute_list = []
for p in npr(input_str):
    temp = ''.join(p)
    if temp not in permute_list:
        permute_list.append(temp)
        
for word in permute_list:
    if word in data:
        print(word)
