names_count = int(input())
names = set()

for _ in range(names_count):
    name = input()
    names.add(name)

for name in names:
    print(name)
