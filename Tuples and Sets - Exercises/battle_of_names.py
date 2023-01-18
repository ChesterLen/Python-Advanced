odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    total_ascii_sum = sum(ord(letter) for letter in input()) // row

    if total_ascii_sum % 2 == 0:
        even_set.add(total_ascii_sum)
    else:
        odd_set.add(total_ascii_sum)

if sum(odd_set) == sum(even_set):
    print(", ".join(str(x) for x in odd_set.union(even_set)))
elif sum(odd_set) > sum(even_set):
    print(", ".join(str(x) for x in odd_set.difference(even_set)))
else:
    print(", ".join(str(x) for x in odd_set.symmetric_difference(even_set)))
