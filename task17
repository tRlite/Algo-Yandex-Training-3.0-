queue1 = list(map(int, input().split()))
front1 = 0
end1 = len(queue1)
queue1 *= 4

queue2 = list(map(int, input().split()))
front2 = 0
end2 = len(queue2) 
queue2 *= 4

step = 0
while step < 10 ** 6 and front1 != end1 and front2 != end2:
    step += 1
    first = queue1[front1]
    front1 = (front1 + 1) % 20
    second = queue2[front2]
    front2 = (front2 + 1) % 20
    if (first == 0 and second == 9) or \
       first > second and not(first == 9 and second == 0):
        queue1[end1] = first
        end1 = (end1 + 1) % 20
        queue1[end1] = second
        end1 = (end1 + 1) % 20
    else:
        queue2[end2] = first
        end2 = (end2 + 1) % 20
        queue2[end2] = second
        end2 = (end2 + 1) % 20

if front1 == end1:
    print(f'second {step}')
elif front2 == end2:
    print(f'first {step}')
else:
    print('botva')
