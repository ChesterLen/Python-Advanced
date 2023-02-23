player_1, player_2 = input().split(", ")
dartboard = [input().split() for _ in range(7)]

player_1_score = 501
player_1_throws = 0

player_2_score = 501
player_2_throws = 0

while True:
    first_player = [int(x) for x in input().strip("()").split(", ")]

    r = first_player[0]
    c = first_player[1]

    if 0 <= r < 7 and 0 <= c < 7:
        if dartboard[r][c] == "D":
            doubled_score = (int(dartboard[0][c]) + int(dartboard[r][0]) + int(dartboard[-1][c]) + int(dartboard[r][-1])) * 2
            player_1_score -= doubled_score
            player_1_throws += 1
        elif dartboard[r][c] == "T":
            trippled_score = (int(dartboard[0][c]) + int(dartboard[r][0]) + int(dartboard[-1][c]) + int(dartboard[r][-1])) * 3
            player_1_score -= trippled_score
            player_1_throws += 1
        elif dartboard[r][c] == "B":
            player_1_throws += 1
            print(f"{player_1} won the game with {player_1_throws} throws!")
            break
        else:
            player_1_score -= int(dartboard[r][c])

        if player_1_score <= 0:
            print(f"{player_1} won the game with {player_1_throws} throws!")
            break

    second_player = [int(x) for x in input().strip("()").split(", ")]
    
    r = second_player[0]
    c = second_player[1]

    if 0 <= r < 6 and 0 <= c < 6:
        if dartboard[r][c] == "D":
            doubled_score = (int(dartboard[0][c]) + int(dartboard[r][0]) + int(dartboard[-1][c]) + int(dartboard[r][-1])) * 2
            player_2_score -= doubled_score
            player_2_throws += 1
        elif dartboard[r][c] == "T":
            trippled_score = (int(dartboard[0][c]) + int(dartboard[r][0]) + int(dartboard[-1][c]) + int(dartboard[r][-1])) * 3
            player_2_score -= trippled_score
            player_2_throws += 1
        elif dartboard[r][c] == "B":
            player_2_throws += 1
            print(f"{player_2} won the game with {player_2_throws} throws!")
            break
        else:
            player_2_score -= int(dartboard[r][c])

        if player_2_score <= 0:
            print(f"{player_2} won the game with {player_2_throws} throws!")
            break