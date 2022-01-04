from State import State

class Terminal_State:

	def terminal_test(self, State):
		if(
			(State.board[0][0] == State.board[0][1] == State.board[0][2]) or
			(State.board[1][0] == State.board[1][1] == State.board[1][2]) or
			(State.board[2][0] == State.board[2][1] == State.board[2][2]) or
			(State.board[0][0] == State.board[1][0] == State.board[2][0]) or
			(State.board[0][1] == State.board[1][1] == State.board[2][1]) or
			(State.board[0][2] == State.board[1][2] == State.board[2][2]) or
			(State.board[0][0] == State.board[1][1] == State.board[2][2]) or
			(State.board[0][2] == State.board[1][1] == State.board[2][0]) ):
			return True

		else:
			return False














if __name__ == "__main__":

