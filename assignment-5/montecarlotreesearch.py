import random
import math


class Node:

    def __init__(self, state, parent=None):

        self.state = state
        self.parent = parent
        self.children = []

        self.wins = 0
        self.visits = 0


    def ucb1(self):

        if self.visits == 0:
            return math.inf

        return (
            self.wins / self.visits
            +
            math.sqrt(
                2 * math.log(self.parent.visits)
                / self.visits
            )
        )


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


def select(node):

    while node.children:
        node = max(node.children, key=lambda n: n.ucb1())

    return node


def expand(node):

    for i in range(9):

        if node.state[i] == ' ':

            new_state = node.state.copy()

            new_state[i] = 'X'

            child = Node(new_state, node)

            node.children.append(child)


def simulate(state):

    current = state.copy()

    player = 'O'

    while True:

        if check_winner(current, 'X'):
            return 1

        if check_winner(current, 'O'):
            return -1

        if is_draw(current):
            return 0

        moves = [
            i for i in range(9)
            if current[i] == ' '
        ]

        move = random.choice(moves)

        current[move] = player

        player = 'X' if player == 'O' else 'O'


def backpropagate(node, result):

    while node:

        node.visits += 1
        node.wins += result

        node = node.parent


root = Node([' ' for _ in range(9)])

for _ in range(100):

    leaf = select(root)

    expand(leaf)

    if leaf.children:

        child = random.choice(leaf.children)

        result = simulate(child.state)

        backpropagate(child, result)


for child in root.children:
    print(child.visits, child.wins)