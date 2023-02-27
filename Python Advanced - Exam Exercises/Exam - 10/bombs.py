from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = deque([int(x) for x in input().split(", ")])

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0

bombs_pouch = []

full_pouch = False

while bomb_effects and bomb_casings:
    bomb_effect = bomb_effects.popleft()
    bomb_casing = bomb_casings.pop()

    if sum([bomb_effect, bomb_casing]) == 40:
        datura_bombs += 1
        if "Datura Bombs" not in bombs_pouch:
            bombs_pouch.append("Datura Bombs")
    elif sum([bomb_effect, bomb_casing]) == 60:
        cherry_bombs += 1
        if "Cherry Bombs" not in bombs_pouch:
            bombs_pouch.append("Cherry Bombs")
    elif sum([bomb_effect, bomb_casing]) == 120:
        smoke_decoy_bombs += 1
        if "Smoke Decoy Bombs" not in bombs_pouch:
            bombs_pouch.append("Smoke Decoy Bombs")
    else:
        bomb_effects.appendleft(bomb_effect)
        bomb_casings.append(bomb_casing - 5)

    if "Datura Bombs" in bombs_pouch and "Cherry Bombs" in bombs_pouch and "Smoke Decoy Bombs" in bombs_pouch:
        if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
            full_pouch = True
            break
    if full_pouch:
        break

if full_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")