from collections import deque

def list_manipulator(numbers, *args):
    list_numbers = deque(numbers)
    commands = [args[0], args[1]]
    list_args = deque(list(args[2:]))

    if commands[0] == "add" and commands[1] == "beginning":
        list_args = deque(list(args[2:])[::-1])
        if list_args:
            for num in range(len(list_args)):
                list_numbers.appendleft(list_args[num])
    elif commands[0] == "add" and commands[1] == "end":
        if list_args:
            for num in range(len(list_args)):
                list_numbers.append(list_args[num])
    elif commands[0] == "remove" and commands[1] == "beginning":
        if list_args:
            for num in range(list_args[0]):
                list_numbers.popleft()
        else:
            list_numbers.popleft()
    elif commands[0] == "remove" and commands[1] == "end":
        if list_args:
            for num in range(list_args[0]):
                list_numbers.pop()
        else:
            list_numbers.pop()

    return list(list_numbers)