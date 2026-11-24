
# Tic-Tac-Toe Game

board = [" " for i in range(9)]

def display_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):

    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if all(board[i] == player for i in position):
            return True

    return False


def play_game():

    current_player = "X"

    print("WELCOME TO TIC-TAC-TOE!")

    while True:

        display_board()

        try:
            move = int(input("Player " + current_player +
                             ", enter position (1-9): "))

            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue

            if board[move - 1] != " ":
                print("Position already occupied! Try again.")
                continue

        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        board[move - 1] = current_player

        # Check winner
        if check_winner(current_player):
            display_board()
            print("Congratulations! Player", current_player, "wins!")
            break

        # Check draw
        if " " not in board:
            display_board()
            print("Game Draw!")
            break

        # Change player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


play_game()
