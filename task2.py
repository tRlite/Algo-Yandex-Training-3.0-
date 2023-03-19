k = int(input())

s = input()

max_len = 1

left = 0
right = 1

dct = {s[0]: 1}

i = 1
while left < len(s):
    if s[left] in dct:
        i -= dct[s[left]]
    while i <= k and right < len(s):
        if s[right] == s[left]:
            if s[right] in dct:
                dct[s[right]] += 1
            else:
                dct[s[right]] = 1
            right += 1
        else:
            if i == k:
                break
            i += 1 
            if s[right] in dct:
                dct[s[right]] += 1
            else:
                dct[s[right]] = 1
            right += 1
    left_adding = min(left, max(k - i, 0))
    max_len = max(max_len, right - left + left_adding)

    x = s[left]
    while left < len(s) and s[left] == x:
        left += 1
        dct[x] -= 1
    i += dct[x]

print(max_len)
