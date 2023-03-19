n = int(input())

k = int(input())

row, column = int(input()), int(input())

place = (row - 1) * 2 + column - 1
if place + k >= n and place - k < 0:
    print(-1)
elif place < k or (place + k < n and not(place % 2 and k % 2)):
    our_place = place + k
    print(our_place // 2 + 1, our_place % 2 + 1)
else:
    our_place = place - k
    print(our_place // 2 + 1, our_place % 2 + 1)
