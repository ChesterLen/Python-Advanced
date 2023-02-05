miligrams_coffeine_list = [int(x) for x in input().split(", ")]
energy_drinks_list = [int(x) for x in input().split(", ")]
total_coffeine = 0
for i in range(len(miligrams_coffeine_list)):
    if len(miligrams_coffeine_list) == 0 or len(energy_drinks_list) == 0:
        break
    if total_coffeine + (miligrams_coffeine_list[-1] * energy_drinks_list[0]) <= 300:
        total_coffeine += miligrams_coffeine_list[-1] * energy_drinks_list[0]
        miligrams_coffeine_list.pop(miligrams_coffeine_list.index(miligrams_coffeine_list[-1]))
        energy_drinks_list.pop(energy_drinks_list.index(energy_drinks_list[0]))
    else:
        miligrams_coffeine_list.pop(miligrams_coffeine_list.index(miligrams_coffeine_list[-1]))
        energy_drinks_list.append(energy_drinks_list[0])
        energy_drinks_list.pop(energy_drinks_list.index(energy_drinks_list[0]))
        total_coffeine -= 30
        if total_coffeine < 0:
            total_coffeine = 0
if len(energy_drinks_list) != 0:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks_list)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_coffeine} mg caffeine.")