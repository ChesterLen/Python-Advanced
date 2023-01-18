range_ = int(input())

elements_set = set()

for _ in range(range_):
    for element in input().split():
        elements_set.add(element)

print(*elements_set, sep="\n")
