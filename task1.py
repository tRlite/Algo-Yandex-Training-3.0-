from collections import Counter

with open('input.txt', 'r') as file:
    text = file.read().replace(' ', '').replace('\n', '') 
main_dct = dict(sorted(Counter(text).items(), key=lambda x: x[0]))

dct_val = {}
for i, val in enumerate(main_dct.values()):
    if val in dct_val:
        dct_val[val].append(i)
    else:
        dct_val[val] = [i]

s = list(' ' * len(main_dct.values()))
m = max(dct_val.keys())

while m > 0:
    if m in dct_val:
        for i in dct_val[m]:
            s[i] = '#'
    print(*s, sep='')
    m -= 1
print(*main_dct.keys(), sep='')
