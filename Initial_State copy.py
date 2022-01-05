from State import State
class Initial_State:

	def __init__(self, xo):
		self.board = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]
		self.player = 'x'
		self.xo = xo




	def initialize(self):
		return State(self.board, self.player, self.xo)












if __name__ == "__main__":
	temp = Initial_State()
	temp_two = temp.initialize()
	print(temp_two.board)
	print(temp_two.player)

