input()
diego = sorted(list(set(map(int, input().split()))))
input()
for p_i in input().split():
    l, r = 0, len(diego) - 1
    while(l <= r):
        mid = (l + r) // 2
        if diego[mid] >= int(p_i):
            r = mid - 1
        else:
            l = mid + 1
    print(l)
