from collections import deque

clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())
racks_count = 1
current_rack = rack_capacity

while clothes:
    cloth = clothes.pop()

    if current_rack - cloth >= 0:
        current_rack -= cloth
    else:
        racks_count += 1
        current_rack = rack_capacity - cloth

print(racks_count)