from State import State
class Actions:

	def __init__(self, temp):
		self.actions = temp

	def update_actions(State): #append possible actions at the current state to self actions
		for i in range(0,3):
			for j in range(0,3):
				if (State.board[i][j] == '.'):
					# actions.append(i*3 + j)
					self.actions.append((i,j))











if __name__ == "__main__":
	act = Actions(['x'])
	print(act.actions)

