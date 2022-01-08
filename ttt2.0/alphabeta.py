import math
from state_space import *


def alpha_beta(board, turn, player):


	moves = actions(board) #generate actions for current board state
	best_util = -math.inf
	flag_index = 0
	action_index = -1

	alpha = -math.inf
	beta = math.inf


	for move in moves:


		temp_util = min_value(result(board, move, turn), toggle_turn(turn), player, (alpha, beta))


		if (temp_util > best_util):
			best_util = temp_util
			action_index = flag_index  # if changed save best action's index

		# undo result() and toggle_turn() 
		(i,j) = move
		board[i][j] = '.'
		toggle_turn(turn)


		alpha = max(alpha, best_util)


		flag_index = flag_index + 1


	return moves[action_index]




def max_value(board, turn, player, alphabeta):
	alpha = alphabeta[0]
	beta = alphabeta[1]

	status = terminal_test(board)   #'d'/'o'/'x'/'n'

	if (status != 'n'):               #if terminated 
		return utility(status, player)


	else:     #if not terminated

		moves = actions(board) #generate actions for current board state
		best_util = -math.inf   

		for move in moves:


			best_util = max(best_util, min_value(result(board, move, turn), toggle_turn(turn), player, (alpha, beta)))


			# undo result() and toggle_turn() 
			(i,j) = move
			board[i][j] = '.'
			toggle_turn(turn)



			if (best_util >= beta):
				return best_util

			else:
				alpha = max(alpha, best_util)

		return best_util



def min_value(board, turn, player, alphabeta):

	alpha = alphabeta[0]
	beta = alphabeta[1]


	status = terminal_test(board)   #'d'/'o'/'x'/'n'


	if (status != 'n'):
		return utility(status, player)


	else:

		moves = actions(board) #generate actions for current board state
		worst_util = math.inf

		for move in moves:

			worst_util = min(worst_util, max_value(result(board, move, turn), toggle_turn(turn) , player, (alpha, beta)))

			# undo result() and toggle_turn() 
			(i,j) = move
			board[i][j] = '.'
			toggle_turn(turn)

			if (worst_util <= alpha):
				return worst_util

			else:
				beta = min(beta, worst_util)

		return worst_util




def utility(status, player):

	if (status == 'd'):
		return 0

	elif (status == 'o'):       
		
		if (player == 'o'):
			return 1
		else:
			return -1


	elif (status == 'x'):

		if (player == 'o'):
			return -1

		else:
			return 1	












