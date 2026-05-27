import math

board = [' ' for _ in range(9)]


def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])


def check_winner(board, player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for win in wins:
        if all(board[i] == player for i in win):
            return True

    return False


def is_draw(board):
    return ' ' not in board


def minimax(board, depth, is_max):

    if check_winner(board, 'X'):
        return 1

    if check_winner(board, 'O'):
        return -1

    if is_draw(board):
        return 0

    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'

                score = minimax(board, depth + 1, False)

                board[i] = ' '

                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'

                score = minimax(board, depth + 1, True)

                board[i] = ' '

                best = min(best, score)

        return best


def best_move(board):

    best_score = -math.inf
    move = -1

    for i in range(9):

        if board[i] == ' ':

            board[i] = 'X'

            score = minimax(board, 0, False)

            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    return move


board[0] = 'X'
board[4] = 'O'

move = best_move(board)

print("Best Move:", move)