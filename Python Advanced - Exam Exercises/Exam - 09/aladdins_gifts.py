from collections import deque

materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

presents = ["Gemstone", "Porcelain Sculpture", "Gold", "Diamond Jewellery"]
crafted_presents = []

while materials and magic_levels:
    material = materials.pop()
    magic_level = magic_levels.popleft()
    total_sum = 0

    if material + magic_level < 100:
        if (material + magic_level) % 2 == 0:
            material *= 2
            magic_level *= 3
            total_sum = material + magic_level
        else:
            total_sum = (material + magic_level) * 2
    elif material + magic_level > 499:
        total_sum = (material + magic_level) / 2
    else:
        total_sum = material + magic_level

    if 100 <= total_sum <= 199:
        crafted_presents.append("Gemstone")
    elif 200 <= total_sum <= 299:
        crafted_presents.append("Porcelain Sculpture")
    elif 300 <= total_sum <= 399:
        crafted_presents.append("Gold")
    elif 400 <= total_sum <= 499:
        crafted_presents.append("Diamond Jewellery")

if "Gemstone" in crafted_presents and "Porcelain Sculpture" in crafted_presents or "Gold" in crafted_presents and "Diamond Jewellery" in crafted_presents:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for present in sorted(set(crafted_presents)):
    print(f"{present}: {crafted_presents.count(present)}")