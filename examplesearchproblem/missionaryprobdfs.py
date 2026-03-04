from collections import deque

# initial and goal states
INITIAL_STATE = (3, 3, 0)   # (missionaries_left, cannibals_left, boat_side)
GOAL_STATE = (0, 0, 1)

# possible boat moves
moves = [
    (1, 0),  # 1 missionary
    (2, 0),  # 2 missionaries
    (0, 1),  # 1 cannibal
    (0, 2),  # 2 cannibals
    (1, 1)   # 1 missionary and 1 cannibal
]


def is_valid(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    # check limits
    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False

    # missionaries cannot be outnumbered
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False

    return True


def get_next_states(state):
    m_left, c_left, boat = state
    next_states = []

    for m, c in moves:

        if boat == 0:  # boat on left
            new_state = (m_left - m, c_left - c, 1)
        else:          # boat on right
            new_state = (m_left + m, c_left + c, 0)

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states


def dfs():
    stack = [(INITIAL_STATE, [INITIAL_STATE])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == GOAL_STATE:
            return path

        if state not in visited:
            visited.add(state)

            for next_state in get_next_states(state):
                stack.append((next_state, path + [next_state]))

    return None


solution = dfs()

print("Solution Path:")
for step in solution:
    print(step)