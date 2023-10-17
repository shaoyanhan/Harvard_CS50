"""
Tic Tac Toe Player
"""

import sys
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        for item in row:
            if item:
                count += 1
    # The "X" player plays first and find the next player by counts
    if count == 0 or count % 2 == 0:
        return "X"
    return "O"
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # find empty places and return as a set
    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                result.add((i, j))
    return result

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
        raise ValueError("Invalid action: position out of range!")
    
    # player  = player(board) will cause ambiguity
    current_player = player(board)
    new_board = copy.deepcopy(board)
    new_board[i][j] = current_player
    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def checkThree(line):
        if line == ["X", "X", "X"] or line == ["O", "O", "O"]:
            return line[0]
        else:
            return None
    for row in board:
        checkResult = checkThree(row)
        if checkResult: return checkResult
    for colNum in range(len(board[0])):
        column = [row[colNum] for row in board]
        checkResult = checkThree(column)
        if checkResult: return checkResult
    main_diagonal = [board[i][i] for i in range(len(board))]
    sub_diagonal = [board[i][len(board) - i - 1] for i in range(len(board))]
    checkResult = checkThree(main_diagonal)
    if checkResult: return checkResult
    checkResult = checkThree(sub_diagonal)
    if checkResult: return checkResult

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # True: tie/won
    # False: no won && no tie
    if len(actions(board)) == 0 or winner(board) != None:
        return True
    return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Assuming utility will only be called on a board if terminal(board) is True.
    current_winner = winner(board)
    if current_winner == "X": return 1
    elif current_winner == "O" : return -1
    else: return 0

    raise NotImplementedError

# The "X" player want to find the max final value to act next turn
def max_value(board):
    if terminal(board): return utility(board)
    v = -sys.maxsize # Initializing v as negative infinite
    # The "X" have to stand in "O"'s shoes after this action and find a maximal value
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

# The "O" player want to find the min final value to act next turn
def min_value(board):
    if terminal(board): return utility(board)
    v = sys.maxsize # Initializing v as positive infinite
    # The "O" have to stand in "X"'s shoes after this action and find a minimal value
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # The board is a terminal board
    if terminal(board): return None

    current_player = player(board)
    current_actions = list(actions(board)) # The set object doesn't have index so turn it to list
    values = [] # saving the final score of current player's next possible actions 
    
    if current_player == "X": 
        # after "X" taken this action, it should stand in "O"'s shoes and to minmize the value
        for action in current_actions:
            values.append(min_value(result(board, action)))
        return current_actions[values.index(max(values))]
        
    else:
        for action in current_actions:
            values.append(max_value(result(board, action)))
        return current_actions[values.index(min(values))]

    raise NotImplementedError
