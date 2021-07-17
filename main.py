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


def win_game(player_list, player):
    """Evaluates player choices against winning combinations"""
    winning_combos = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9]]
    sorted_player_list = sorted(player_list)
    if len(sorted_player_list) >= 3:
        check_combo = sorted_player_list[:3]
        if check_combo in winning_combos:
            print(f"{player} wins")
    return




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
    x_choices = []
    o_choices = []
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
                if characters[player_index] == "X":
                    x_choices.append(valid_number)
                    win_game(x_choices, player)
                    print(f"X choices: {x_choices}")
                if characters[player_index] == "O":
                    o_choices.append(valid_number)
                    print(f"O choices: {o_choices}")
                    win_game(o_choices, player)
                if number_turns == 9:
                    break
            else:
                raise ValueError("Error!!! That space is taken. Ending game")

    print("Game over!!")

    return


# TODO: Fix duplicate selection issue


play_game()
