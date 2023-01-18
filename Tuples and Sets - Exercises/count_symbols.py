letters = {}

for letter in input():
    if letter not in letters.keys():
        letters[letter] = 0
    letters[letter] += 1

for item, value in sorted(letters.items()):
    print(f"{item}: {value} time/s")
