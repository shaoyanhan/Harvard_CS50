import tictactoe
from tictactoe import *

board0 = [[EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY]]
board1 = [[O, O, O],
          [X, EMPTY, X],
          [EMPTY, X, EMPTY]]
board2 = [[X, O, EMPTY],
          [X, EMPTY, EMPTY],
          [X, O, O]]
board3 = [[O, EMPTY, X],
          [X, O, EMPTY],
          [X, EMPTY, O]]
board4 = [[O, X, O],
          [X, X, O],
          [X, O, X]]
board5 = [[EMPTY, O, O],
          [O, X, X],
          [X, EMPTY, X]]
board6 = [[EMPTY, O, O],
          [O, X, X],
          [X, X, EMPTY]]


board = board5
print(board)
print(tictactoe.player(board))
actions = tictactoe.actions(board)
print(actions)
for action in actions:
    print(tictactoe.result(board, action))
print(tictactoe.winner(board))
print(tictactoe.terminal(board))
print(tictactoe.utility(board))
print(tictactoe.min_value(board))
print(tictactoe.minimax(board))