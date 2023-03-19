from collections import deque

deque = deque()

while True:
    command = input().split()
    if command[0] == 'push_front':
        deque.appendleft(int(command[1]))
        print('ok')
    elif command[0] == 'push_back':
        deque.append(int(command[1]))
        print('ok')
    elif command[0] == 'pop_front':
        if len(deque):
            print(deque.popleft())
        else:
            print('error')
    elif command[0] == 'pop_back':
        if len(deque):
            print(deque.pop())
        else:
            print('error')
    elif command[0] == 'front':
        if len(deque):
            x = deque.popleft()
            print(x)
            deque.appendleft(x)
        else:
            print('error')
    elif command[0] == 'back':
        if len(deque):
            x = deque.pop()
            print(x)
            deque.append(x)
        else:
            print('error')
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'clear':
        deque.clear()
        print('ok')
    elif command[0] == 'exit':
        print('bye')
        break
