# def board():
#     """Board used to play the game. Numbers correspond to the spaces"""
#     structure = "    |     |    \n  1 |  2  |  3 \n----|-----|----\n  4 |  5  |  6 \n    |     |    \n" \
#                 "----|-----|----\n  7 |  8  |  9 \n    |     |    "
#     return structure
# a = board()
# print(a)

def create_players():
    """Create two players for game"""
    player1 = input("Player 1,Do you want to be 'X' or 'O'?\n").upper()
    player2 = ""
    if player1 == "X":
        print("That means Player 2 is 'O")
        player2 = 'O'
    elif player1 == "O":
        print("That means Player 2 is 'X")
        player2 = 'X'
    else:
        print("Choice is invalid")
    return player1, player2


def play_game():
    """Board used to play the game. Numbers correspond to the spaces"""
    structure = "    |     |    \n  1 |  2  |  3 \n----|-----|----\n  4 |  5  |  6 \n    |     |    \n" \
                "----|-----|----\n  7 |  8  |  9 \n    |     |    "

    a = create_players()
    player1 = a[0]
    player2 = a[1]

    print(f"Player 1: {player1}")
    print(f"Player 2: {player2}")

    # player1_choice = 1
    # new_structure = structure.replace(str(player1_choice), player1)
    return


play_game()










