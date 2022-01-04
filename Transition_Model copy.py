from State import State
from Actions import Actions
class Transition_Model:   #takes state, action, and create new states for branches



	def result(self, State, an_action): #apply an action to the self state and toggle player
		(i,j) = an_action
		State.board[i][j] = State.player


	def toggle_player(self, State):

		if (State.player == 'x'):
			State.player = 'o'

		else:
			State.player = 'x'








if __name__ == "__main__":


	board = [['.', '1', '.'],['.', '.', '.'],['.', '.', '.']]
	player = 'x'



	temp_state = State(board, player)
	temp_Action = Actions(temp_state)
	temp_Action.update_actions()
	temp_Transition_Model = Transition_Model(temp_Action)
	temp_Transition_Model.result()

		
	

