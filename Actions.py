from State import State
class Actions:

	def __init__(self):
		actions = []

	def update_actions(State): #append possible actions at the current state to self actions
		for i in range(0,3):
			for j in range(0,3):
				if (State.board[i][j] == '.'):
					# actions.append(i*3 + j)
					self.actions.append((i,j))











if __name__ == "__main__":
	initial = [['.', '1', '.'],['.', '.', '.'],['.', '.', '.']]
	temp = State(initial, 'o')
	temp_two = Actions(temp)
	# print(temp_two.states.board)
	# print(temp_two.states.turn)
	# print(temp_two.actions)
	temp_two.update_actions()
	print(temp_two.action)
