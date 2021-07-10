# def board():
#     """Board used to play the game. Numbers correspond to the spaces"""
#     structure = "    |     |    \n  1 |  2  |  3 \n----|-----|----\n  4 |  5  |  6 \n    |     |    \n" \
#                 "----|-----|----\n  7 |  8  |  9 \n    |     |    "
#     return structure
# a = board()
# print(a)


def create_players():
    """Create two players for game"""
    player_selection = True
    player1 = ""
    player2 = ""
    while player_selection:
        first_player_choice = input("Player 1,Do you want to be 'X' or 'O'?\n").upper()
        if first_player_choice == "X":
            print("That means Player 2 is O")
            player1 = first_player_choice
            player2 = 'O'
            player_selection = False
        elif first_player_choice == "O":
            print("That means Player 2 is X")
            player1 = first_player_choice
            player2 = 'X'
            player_selection = False
        else:
            print("Choice is invalid, try again")
            print("===============================")
    return player1, player2


def play_game():
    """Board used to play the game. Numbers correspond to the spaces"""
    structure = "    |     |    \n  1 |  2  |  3 \n----|-----|----\n  4 |  5  |  6 \n    |     |    \n" \
                "----|-----|----\n  7 |  8  |  9 \n    |     |    "

    players = create_players()
    player1 = players[0]
    player2 = players[1]

    print(f"Player 1: {player1}")
    print(f"Player 2: {player2}")

    # player1_choice = 1
    # new_structure = structure.replace(str(player1_choice), player1)
    return


play_game()

# def p_word():
#     looping = True
#     password = ""
#
#     while looping:
#
#         ans1 = input("\n\nTest a new password? ")
#
#         if ans1.upper() in ("NO", "N"):
#             looping = False
#
# p_word()