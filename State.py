class State:

	def __init__(self, board, player):
		self.board = board
		self.player = player













if __name__ == "__main__":
	initial = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]
	temp = State(initial, 'o')
	print(temp.board)
	print(temp.turn)

