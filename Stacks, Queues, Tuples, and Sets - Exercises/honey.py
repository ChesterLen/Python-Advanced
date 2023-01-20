from collections import deque

bees = deque([int(x) for x in input().split()])
nectar_values = deque([int(x) for x in input().split()])
calculating_symbols = deque([x for x in input().split()])
total_honey = 0

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

while bees and nectar_values:
    bee = bees.popleft()
    nectar = nectar_values.pop()

    if nectar > bee:
        total_honey += abs(operations[calculating_symbols.popleft()](bee, nectar))
    elif nectar < bee:
        bees.appendleft(bee)

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar_values:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_values)}")
