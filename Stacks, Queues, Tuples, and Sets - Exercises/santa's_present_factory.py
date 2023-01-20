from collections import deque

materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

toys_dict = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

toys_list = []

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[0] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0

    if not magic_level:
        continue

    product = material * magic_level

    if toys_dict.get(product):
        toys_list.append(toys_dict[product])
    elif product < 0:
        materials.append(material + magic_level)
    elif product > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(toys_list) or {"Teddy bear", "Bicycle"}.issubset(toys_list):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

[print(f"{toy}: {toys_list.count(toy)}") for toy in sorted(set(toys_list))]
