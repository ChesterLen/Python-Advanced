from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_powers = deque([int(x) for x in input().split(", ")])

palm_firework = 0
willow_firework = 0
crossette_firework = 0

while firework_effects and explosive_powers:
    firework = firework_effects.popleft()
    explosive_power = explosive_powers.pop()
    if firework <= 0:
        explosive_powers.append(explosive_power)
        continue
    if explosive_power <= 0:
        firework_effects.appendleft(firework)
        continue
    firework_explosive_power_sum = firework + explosive_power

    if firework_explosive_power_sum % 3 == 0 and firework_explosive_power_sum % 5 != 0:
        palm_firework += 1
    elif firework_explosive_power_sum % 5 == 0 and firework_explosive_power_sum % 3 != 0:
        willow_firework += 1
    elif firework_explosive_power_sum % 3 == 0 and firework_explosive_power_sum % 5 == 0:
        crossette_firework += 1
    else:
        firework -= 1
        firework_effects.append(firework)
        explosive_powers.append(explosive_power)

if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")