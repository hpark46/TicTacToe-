import math
from state_space import *


def minimax(board, turn, player):

	moves = actions(board) #possible moves on board
	best_util = -math.inf
	index = 0

	for num in range(0,len(moves)):   #index of the action in moves

		# result(s,a).   tm
		# toggle_turn.   tm
		# unchanging player 'x/o'

		num_util = min_value(transition_model(board, moves[num], turn), player)


		if (num_util > best_util):
			best_util = num_util
			index = num


	return moves[index]




def max_value(board, turn, player):

	status = terminal_test(board)   #'d'/'o'/'x'/'n'

	if (status != 'n'):
		return utility(status, player)


	else:

		moves = actions(board) #generate actions for current board state
		best_util = -math.inf

		for move in moves:

			best_util = max(best_util, min_value(transition_model(board, move, turn), player))

		return best_util



def min_value(board, turn, player):

	status = terminal_test(board)   #'d'/'o'/'x'/'n'


	if (status != 'n'):
		return utility(status, player)


	else:

		moves = actions(board) #generate actions for current board state
		worst_util = math.inf

		for move in moves:

			worst_util = min(worst_util, min_value(transition_model(board, move, turn), player))

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










