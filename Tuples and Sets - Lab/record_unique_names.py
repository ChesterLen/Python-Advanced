names_count = int(input())
names = {input() for _ in range(names_count)}

for name in names:
    print(name)
