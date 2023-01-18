first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, *data = input().split()
    command = first_command + " " + data.pop(0)
    if command == "Add First":
        [first_sequence.add(int(number)) for number in data]
    elif command == "Add Second":
        [second_sequence.add(int(number)) for number in data]
    elif command == "Remove First":
        [first_sequence.discard(int(number)) for number in data]
    elif command == "Remove Second":
        [second_sequence.discard(int(number)) for number in data]
    else:
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print(True)
        else:
            print(False)

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
