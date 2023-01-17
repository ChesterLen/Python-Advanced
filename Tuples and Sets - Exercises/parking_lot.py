commands_count = int(input())
cars = set()

for _ in range(commands_count):
    direction, car = input().split(", ")
    if direction == "IN":
        cars.add(car)
    elif direction == "OUT":
        cars.remove(car)
if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
