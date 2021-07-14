# def board():
#     """Board used to play the game. Numbers correspond to the spaces"""
#     board = "    |     |    \n  1 |  2  |  3 \n----|-----|----\n  4 |  5  |  6 \n    |     |    \n" \
#                 "----|-----|----\n  7 |  8  |  9 \n    |     |    "
#     return board
# a = board()
# print(a)


def create_players():
    """Create two players for game"""
    player_selection = True
    player1 = ""
    player2 = ""
    while player_selection:
        first_player_choice = input("Player 1, Do you want to be 'X' or 'O'?\n").upper()
        if first_player_choice == "X":
            # print("That means Player 2 is O")
            player1 = first_player_choice
            player2 = 'O'
            player_selection = False
        elif first_player_choice == "O":
            # print("That means Player 2 is X")
            player1 = first_player_choice
            player2 = 'X'
            player_selection = False
        else:
            print("Choice is invalid, try again")
            print("===============================")
    return player1, player2


def play_game():
    """Board used to play the game. Numbers correspond to the spaces"""
    board = "    |     |    \n  1 |  2  |  3 \n----|-----|----\n  4 |  5  |  6 \n    |     |    \n" \
            "----|-----|----\n  7 |  8  |  9 \n    |     |    "
    print(board)

    # ========================CREATE PLAYERS====================================#
    # Call create_players() to assign players with 'X' or 'O'; use the returned values to create the list "characters"
    # Ask for names of players; print output

    players = create_players()
    player1 = players[0]
    player2 = players[1]

    characters = [player1, player2]

    first_player = input("Player 1, what's your name?\n")
    second_player = input("Player 2, what's your name?\n")

    print(f"{first_player}: {player1}")
    print(f"{second_player}: {player2}")

    # =========================GAMEPLAY=====================================================
    all_players = [first_player, second_player]
    occupied_spaces = []
    number_turns = 0

    while number_turns != 9:
        for player in all_players:
            choose_number = True
            valid_number = 0

            # Validate player choice
            while choose_number:
                try:
                    player_choice = int(input(f"{player}, make a choice:\n"))
                except ValueError:
                    print("Error!! Only numbers are allowed")
                else:
                    if player_choice not in range(1, 10):
                        print("Please choose a number between 1 and 9")
                    else:
                        valid_number = player_choice
                        choose_number = False

            # Validate that player choice has not been used
            if valid_number not in occupied_spaces:
                player_index = all_players.index(player)
                new_board = board.replace(str(valid_number), characters[player_index])
                board = new_board
                occupied_spaces.append(valid_number)
                print(board)
                number_turns += 1
                if number_turns == 9:
                    break
                print(f"Num turns: {number_turns}")
            else:
                print("That space is taken; try again")
                print(board)

    print("Game over!!")

    return


# TODO 2: Check player choice range logic; not working


play_game()
