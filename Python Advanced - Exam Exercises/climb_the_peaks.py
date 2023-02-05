from collections import deque

daily_food = deque([int(x) for x in input().split(", ")])
daily_stamina = deque([int(x) for x in input().split(", ")])

conquered_peaks = []
days = 1

peaks_difficulty_level = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70),
])

while True:
    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break

    if days > 7 or not daily_food or not daily_stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    food = daily_food.pop()
    stamina = daily_stamina.popleft()
    peak = peaks_difficulty_level.popleft()

    if food + stamina >= peak[1]:
        days += 1
        conquered_peaks.append(peak[0])
    else:
        days += 1
        peaks_difficulty_level.appendleft(peak)

if conquered_peaks:
    print("Conquered peaks:")
    for peak in conquered_peaks:
        print(peak)