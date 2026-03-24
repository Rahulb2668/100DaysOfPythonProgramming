
def print_board(current_board):
    for i in range(0, 9, 3):
        print(current_board[i], "|", current_board[i + 1], "|", current_board[i + 2])

def check_winner(current_board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]

    for conditions in win_conditions:
        if all([current_board[i] == player for i in conditions]):
            return True
    return False


def is_valid_move(current_board, index):
    if current_board[index] == " ":
        return True
    return False

def make_move(current_board, index, player):
    if is_valid_move(current_board, index):
        current_board[index] = player
        return True
    else:
        print(f"Invalid Move")
        return False

def is_draw(current_board):
    return " " not in current_board


def play_game():
    board = [" " for i in range(9)]
    current_player = "X"
    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, choose 0-8: "))

        if not make_move(board, move, current_player):
            print("Invalid Move Try again")
            continue

        if check_winner(board, player=current_player):
            print("Winner is {}".format(current_player))
            break

        if is_draw(board):
            print("Its draw")
            break

        current_player = 'O' if current_player == "X" else "X"


play_game()