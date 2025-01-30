class TicTacToeModel:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # 3x3 board
        self.current_player = "X"  # Human starts as "X"
        self.score = {"X": 0, "O": 0}  # Track scores

    def make_move(self, index):
        """Make a move on the board."""
        if self.board[index] == " ":
            self.board[index] = self.current_player
            return True
        return False

    def undo_move(self, index):
        """Undo a move on the board."""
        if self.board[index] != " ":
            self.board[index] = " "
            self.switch_player()  # Switch back to the previous player
            return True
        return False

    def check_winner(self):
        """Check if the current player has won."""
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],  # Rows
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],  # Columns
            [0, 4, 8],
            [2, 4, 6],  # Diagonals
        ]
        for combo in winning_combinations:
            if all(self.board[i] == self.current_player for i in combo):
                return True
        return False

    def is_board_full(self):
        """Check if the board is full."""
        return " " not in self.board

    def reset_board(self):
        """Reset the board for a new game."""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def switch_player(self):
        """Switch the current player."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def update_score(self, player):
        """Update the score for the winning player."""
        self.score[player] += 1

    def get_board(self):
        """Get the current board state."""
        return self.board
