class Agent:
    def __init__(self, game):
        self.game = game
        self.transposition_table = {}  # For memoization
        self.PLAYER_O = "O"
        self.PLAYER_X = "X"
        self.WIN_SCORE = 10
        self.LOSE_SCORE = -10
        self.DEPTH_LIMIT = 5  # Depth limit for Minimax

    def make_move(self):
        """Find the best move using minimax algorithm with alpha-beta pruning."""
        best_score = -float("inf")
        best_move = None
        alpha = -float("inf")
        beta = float("inf")

        # First check for winning move
        for i in range(9):
            if self.game.board[i] == " ":
                self.game.board[i] = self.PLAYER_O
                if self.evaluate_board() == self.WIN_SCORE:
                    self.game.board[i] = " "
                    return (i // 3, i % 3)
                self.game.board[i] = " "

        # Then check for blocking opponent's winning move
        for i in range(9):
            if self.game.board[i] == " ":
                self.game.board[i] = self.PLAYER_X
                if self.evaluate_board() == self.LOSE_SCORE:
                    self.game.board[i] = " "
                    return (i // 3, i % 3)
                self.game.board[i] = " "

        # If no immediate win/block, use minimax
        possible_moves = self.get_possible_moves()
        ordered_moves = self.order_moves(possible_moves)  # Move ordering

        for move in ordered_moves:
            self.game.board[move] = self.PLAYER_O
            score = self.minimax(0, False, alpha, beta)
            self.game.board[move] = " "

            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, score)

        if best_move is not None:
            return (best_move // 3, best_move % 3)
        return None

    def evaluate_board(self):
        """Evaluate the current board state."""
        # Check rows, columns, and diagonals for a winner
        lines = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],  # Rows
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],  # Columns
            [0, 4, 8],
            [2, 4, 6],  # Diagonals
        ]
        for line in lines:
            a, b, c = line
            if self.game.board[a] == self.game.board[b] == self.game.board[c]:
                if self.game.board[a] == self.PLAYER_O:
                    return self.WIN_SCORE
                elif self.game.board[a] == self.PLAYER_X:
                    return self.LOSE_SCORE

        # Check for potential winning moves
        for line in lines:
            cells = [self.game.board[i] for i in line]
            if cells.count(self.PLAYER_O) == 2 and cells.count(" ") == 1:
                return 5
            if cells.count(self.PLAYER_X) == 2 and cells.count(" ") == 1:
                return -5

        # Additional heuristics
        score = 0
        if self.game.board[4] == self.PLAYER_O:  # Center control
            score += 1
        elif self.game.board[4] == self.PLAYER_X:
            score -= 1

        corners = [0, 2, 6, 8]
        for corner in corners:
            if self.game.board[corner] == self.PLAYER_O:
                score += 0.5
            elif self.game.board[corner] == self.PLAYER_X:
                score -= 0.5

        return score

    def minimax(self, depth, is_maximizing, alpha, beta):
        """Implement minimax algorithm with alpha-beta pruning."""
        board_key = tuple(self.game.board)  # Use the board state as a key
        if board_key in self.transposition_table:
            return self.transposition_table[board_key]

        score = self.evaluate_board()

        # Base cases
        if score == self.WIN_SCORE:
            return score - depth
        if score == self.LOSE_SCORE:
            return score + depth
        if " " not in self.game.board or depth == self.DEPTH_LIMIT:
            return score  # Use heuristic evaluation for non-terminal states

        if is_maximizing:
            best_score = -float("inf")
            for move in self.get_possible_moves():
                self.game.board[move] = self.PLAYER_O
                score = self.minimax(depth + 1, False, alpha, beta)
                self.game.board[move] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            self.transposition_table[board_key] = best_score
            return best_score
        else:
            best_score = float("inf")
            for move in self.get_possible_moves():
                self.game.board[move] = self.PLAYER_X
                score = self.minimax(depth + 1, True, alpha, beta)
                self.game.board[move] = " "
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            self.transposition_table[board_key] = best_score
            return best_score

    def get_possible_moves(self):
        """Get all possible moves on the board."""
        return [i for i, cell in enumerate(self.game.board) if cell == " "]

    def order_moves(self, moves):
        """Order moves based on priority (center, corners, edges)."""
        move_priority = [4, 0, 2, 6, 8, 1, 3, 5, 7]
        return sorted(moves, key=lambda x: move_priority.index(x))
