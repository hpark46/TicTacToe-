from State import State
class Initial_State:

	def __init__(self):
		board = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]
		player = 'x'



	def initialize(self):
		return State(self.board, self.player)












if __name__ == "__main__":
	temp = Initial_State()
	temp_two = temp.initialize()
	print(temp_two.board)
	print(temp_two.player)

