from collections import deque

seats = input().split(", ")
sequence_1 = deque([int(x) for x in input().split(", ")])
sequence_2 = deque([int(x) for x in input().split(", ")])

matched_seats = []

rotations = 0

while sequence_1:
    if len(matched_seats) == 3:
        break
    if rotations == 10:
        break
    left_number = sequence_1.popleft()
    right_number = sequence_2.pop()
    character_sum_ascii = chr(left_number + right_number)
    first_try_seat = str(left_number) + character_sum_ascii
    second_try_seat = str(right_number) + character_sum_ascii

    for seat in [first_try_seat, second_try_seat]:
        if seat in matched_seats:
            break
        if seat in seats:
            seats.remove(seat)
            matched_seats.append(seat)
            break
    else:
        sequence_1.append(left_number)
        sequence_2.appendleft(right_number)
    
    rotations += 1

    

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")