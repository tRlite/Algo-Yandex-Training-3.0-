stack = []

while True:
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
        print('ok')
    elif command[0] == 'pop':
        if len(stack) == 0:
            print('error')
        else:
            print(stack[-1])
            stack.pop()
    elif command[0] == 'back':
        if len(stack) == 0:
            print('error')
        else:
            print(stack[-1])
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'clear':
        stack = []
        print('ok')
    elif command[0] == 'exit':
        print('bye')
        break
