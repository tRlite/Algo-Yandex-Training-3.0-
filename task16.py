queue = []
front = 0

while True:
    command = input().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
        print('ok')
    elif command[0] == 'pop':
        if front != len(queue):
            print(queue[front])
            front += 1
        else:
            print('error')
    elif command[0] == 'front':
        if front != len(queue):
            print(queue[front])
        else:
            print('error')
    elif command[0] == 'size':
        print(len(queue) - front)
    elif command[0] == 'clear':
        queue = []
        front = 0
        print('ok')
    elif command[0] == 'exit':
        print('bye')
        break
