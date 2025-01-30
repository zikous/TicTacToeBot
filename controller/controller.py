from model.model import TicTacToeModel
from view.view import TicTacToeView
from agent.agent import Agent  # Import your Agent class


class TicTacToeController:
    def __init__(self, root):
        self.model = TicTacToeModel()
        self.view = TicTacToeView(root, self)
        self.agent = Agent(self.model)  # Initialize the Agent

    def on_button_click(self, row, col):
        """Handle button clicks."""
        index = 3 * row + col
        if self.model.make_move(index):
            self.view.update_button(row, col, self.model.current_player)
            if self.model.check_winner():  # No argument needed
                self.model.update_score(self.model.current_player)
                self.view.update_score(self.model.score["X"], self.model.score["O"])
                self.view.show_winner(self.model.current_player)
                self.model.reset_board()
                self.view.reset_buttons()
            elif self.model.is_board_full():
                self.view.show_winner(None)
                self.model.reset_board()
                self.view.reset_buttons()
            else:
                self.model.switch_player()
                if self.model.current_player == "O":
                    self.bot_move()

    def bot_move(self):
        """Use the Agent to make a move."""
        move = self.agent.make_move()  # Get the best move from the Agent
        if move:
            row, col = move
            index = 3 * row + col
            if self.model.make_move(index):
                self.view.update_button(row, col, self.model.current_player)
                if self.model.check_winner():  # No argument needed
                    self.model.update_score(self.model.current_player)
                    self.view.update_score(self.model.score["X"], self.model.score["O"])
                    self.view.show_winner(self.model.current_player)
                    self.model.reset_board()
                    self.view.reset_buttons()
                elif self.model.is_board_full():
                    self.view.show_winner(None)
                    self.model.reset_board()
                    self.view.reset_buttons()
                else:
                    self.model.switch_player()

    def reset_game(self):
        """Reset the game."""
        self.model.reset_board()
        self.view.reset_buttons()

    def get_score(self, player):
        """Get the score for a player."""
        return self.model.score[player]
