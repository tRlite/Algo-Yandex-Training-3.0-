t1 = list(map(int, input().split(':')))
t2 = list(map(int, input().split(':')))
t3 = list(map(int, input().split(':')))

if t1[0] > t3[0]:
    t3[0] += 24
    
diff = int(((t3[0] - t1[0]) * 3600 + (t3[1] - t1[1]) * 60 + t3[2] - t1[2]) / 2 + 0.5)

t2_sec = 3600 * t2[0] + 60 * t2[1] + t2[2] + diff
t2[0] = t2_sec // 3600
t2_sec %= 3600

if t2[0] >= 24:
    t2[0] -= 24
    
t2[1] = t2_sec // 60

t2[2] = t2_sec % 60
print(f'{t2[0]:02}:{t2[1]:02}:{t2[2]:02}')
