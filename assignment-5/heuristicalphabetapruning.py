import math


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


def alphabeta(board, depth, alpha, beta, is_max):

    if check_winner(board, 'X'):
        return 1

    if check_winner(board, 'O'):
        return -1

    if is_draw(board):
        return 0

    if is_max:

        value = -math.inf

        for i in range(9):

            if board[i] == ' ':

                board[i] = 'X'

                value = max(
                    value,
                    alphabeta(board, depth+1, alpha, beta, False)
                )

                board[i] = ' '

                alpha = max(alpha, value)

                if alpha >= beta:
                    break

        return value

    else:

        value = math.inf

        for i in range(9):

            if board[i] == ' ':

                board[i] = 'O'

                value = min(
                    value,
                    alphabeta(board, depth+1, alpha, beta, True)
                )

                board[i] = ' '

                beta = min(beta, value)

                if alpha >= beta:
                    break

        return value


board = [
    'X', ' ', ' ',
    ' ', 'O', ' ',
    ' ', ' ', ' '
]

result = alphabeta(board, 0, -math.inf, math.inf, True)

print("Result:", result)