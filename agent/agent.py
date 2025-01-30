class Agent:
    def __init__(self, game):
        self.game = game

    def make_move(self):
        """Find the best move using minimax algorithm with alpha-beta pruning."""
        best_score = -float("inf")
        best_move = None
        alpha = -float("inf")
        beta = float("inf")

        # First check for winning move
        for i in range(9):
            if self.game.board[i] == " ":
                self.game.board[i] = "O"
                if self.evaluate_board() == 10:
                    self.game.board[i] = " "
                    return (i // 3, i % 3)
                self.game.board[i] = " "

        # Then check for blocking opponent's winning move
        for i in range(9):
            if self.game.board[i] == " ":
                self.game.board[i] = "X"
                if self.evaluate_board() == -10:
                    self.game.board[i] = " "
                    return (i // 3, i % 3)
                self.game.board[i] = " "

        # If no immediate win/block, use minimax
        for i in range(9):
            if self.game.board[i] == " ":
                self.game.board[i] = "O"
                score = self.minimax(0, False, alpha, beta)
                self.game.board[i] = " "

                if score > best_score:
                    best_score = score
                    best_move = i
                alpha = max(alpha, score)

        if best_move is not None:
            return (best_move // 3, best_move % 3)
        return None

    def evaluate_board(self):
        """Evaluate the current board state."""
        # Check rows
        for i in range(0, 9, 3):
            if self.game.board[i] == self.game.board[i + 1] == self.game.board[i + 2]:
                if self.game.board[i] == "O":
                    return 10
                elif self.game.board[i] == "X":
                    return -10

        # Check columns
        for i in range(3):
            if self.game.board[i] == self.game.board[i + 3] == self.game.board[i + 6]:
                if self.game.board[i] == "O":
                    return 10
                elif self.game.board[i] == "X":
                    return -10

        # Check diagonals
        if self.game.board[0] == self.game.board[4] == self.game.board[8]:
            if self.game.board[0] == "O":
                return 10
            elif self.game.board[0] == "X":
                return -10

        if self.game.board[2] == self.game.board[4] == self.game.board[6]:
            if self.game.board[2] == "O":
                return 10
            elif self.game.board[2] == "X":
                return -10

        # Check for potential winning moves
        for i in range(0, 9, 3):
            row = self.game.board[i : i + 3]
            if row.count("O") == 2 and row.count(" ") == 1:
                return 5
            if row.count("X") == 2 and row.count(" ") == 1:
                return -5

        # If no winner, return 0
        return 0

    def minimax(self, depth, is_maximizing, alpha, beta):
        """Implement minimax algorithm with alpha-beta pruning."""
        score = self.evaluate_board()

        # Base cases
        if score == 10:
            return score - depth
        if score == -10:
            return score + depth
        if " " not in self.game.board:
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for i in range(9):
                if self.game.board[i] == " ":
                    self.game.board[i] = "O"
                    score = self.minimax(depth + 1, False, alpha, beta)
                    self.game.board[i] = " "
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if self.game.board[i] == " ":
                    self.game.board[i] = "X"
                    score = self.minimax(depth + 1, True, alpha, beta)
                    self.game.board[i] = " "
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
            return best_score
