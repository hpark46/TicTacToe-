from State import State
from Actions import Actions
from Transition_Model import Transition_Model
from Initial_State import Initial_State


def minimax(state):

	return 



def max_value(state):



def min_value(state):




def utility(state):
	
	status = terminal_test(state)

	if (status == 'd'):
		return 0

	elif (status == 'o'):       #have to add handling current player later
		return 1 or -1

	elif (status == 'x'):		#have to add handling current player later
		return 1 or -1





def terminal_test(state):  # 'd': draw  'o'/'x': winner  'n': not terminated

	#test winner conditions

	for row in state.board: #i
		if (row[0] == row[1] == row[2]): #j
			return row[0] #terminated with winner

	for column in state.board:
		if (state.board[0][column] == state.board[1][column] == state.board[2][column]):
			return state.board[0][column] #terminated with winner

	if(state.board[0][0] == state.board[1][1] == state.board[2][2] or
		state.board[0][2] == state.board[1][1] == state.board[2][0]):
		return state.board[1][1]  #terminated with winner


	#test for full board

	else:   
		flag = True

		for i in range(0,3):
			for j in range(0,3):
				if (state.board[i][j] == '.'):
					flag = False

		if (flag == True):     #if full board draw
			return 'd'

		else: 					#if not full board (game not over)
			return 'n'












	# flag = True
	# for i in range(0,3):
	# 	for j in range(0,3):
	# 		if (state.board[i][j] == '.'):
	# 			flag = False

	# if (flag == True):

	# 	return '.'    #Terminated, draw

	# else:

	# 	for row in state.board: #i
	# 		if (row[0] == row[1] == row[2]): #j
	# 			return row[0] #terminated with winner

	# 	for column in state.board:
	# 		if (state.board[0][column] == state.board[1][column] == state.board[2][column]):
	# 			return state.board[0][column] #terminated with winner


	# 	if(state.board[0][0] == state.board[1][1] == state.board[2][2] or
	# 		state.board[0][2] == state.board[1][1] == state.board[2][0]):
	# 		return state.board[1][1]  #terminated with winner


	# 	else:
	# 		return 'n'
















if __name__ == "__main__":
	initial = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]
	temp = State(initial, 'o')
	print(temp.board)
	print(temp.turn)

