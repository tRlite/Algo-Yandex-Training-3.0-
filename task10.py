word = input()

dct = {}

l = len(word)
for i in range(l):
    if word[i] in dct:
        dct[word[i]] += (l - i) * (i + 1)
    else:
        dct[word[i]] = (l - i) * (i + 1)
        
for key in sorted(dct):
    print(f'{key}: {dct[key]}')
