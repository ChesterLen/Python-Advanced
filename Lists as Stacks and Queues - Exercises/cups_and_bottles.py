from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
wasted_water = 0

while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()
    if bottle >= cup:
        wasted_water += bottle - cup
    else:
        cups.appendleft(cup - bottle)

if not cups:
    print(f"Bottles: {' '.join(str(x) for x in bottles)}")
elif not bottles:
    print(f"Cups: {' '.join(str(x) for x in cups)}")

print(f"Wasted litters of water: {wasted_water}")
