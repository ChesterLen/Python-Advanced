from math import floor

odd_set = set()
even_set = set()
current_row = 0

for _ in range(int(input())):
    name = input()
    current_row += 1
    total = 0
    for letter in name:
        total += ord(letter)
    total = floor(total / current_row)
    if total % 2 == 0:
        even_set.add(total)
    else:
        odd_set.add(total)

if sum(odd_set) == sum(even_set):
    print(", ".join(str(x) for x in odd_set.union(even_set)))
elif sum(odd_set) > sum(even_set):
    print(", ".join(str(x) for x in odd_set.difference(even_set)))
else:
    print(", ".join(str(x) for x in odd_set.symmetric_difference(even_set)))
