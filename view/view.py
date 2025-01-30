import tkinter as tk
from tkinter import messagebox


class TicTacToeView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x500")  # Window size

        # Create GUI
        self.create_widgets()

    def create_widgets(self):
        # Score display
        self.score_label = tk.Label(
            self.root,
            text=f"Human (X): {self.controller.get_score('X')}  Bot (O): {self.controller.get_score('O')}",
            font=("Arial", 16),
        )
        self.score_label.pack(pady=10)

        # Game board (3x3 grid)
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    self.board_frame,
                    text=" ",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda i=i, j=j: self.controller.on_button_click(i, j),
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

        # Restart button
        self.restart_button = tk.Button(
            self.root,
            text="Restart",
            font=("Arial", 14),
            command=self.controller.reset_game,
        )
        self.restart_button.pack(pady=20)

    def update_button(self, row, col, player):
        """Update the button text with the current player's symbol."""
        self.buttons[row][col].config(text=player)

    def update_score(self, x_score, o_score):
        """Update the score display."""
        self.score_label.config(text=f"Human (X): {x_score}  Bot (O): {o_score}")

    def show_winner(self, winner):
        """Show a message box with the winner."""
        if winner == "X":
            messagebox.showinfo("Game Over", "Human wins!")
        elif winner == "O":
            messagebox.showinfo("Game Over", "Bot wins!")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")

    def reset_buttons(self):
        """Reset all buttons to empty."""
        for row in self.buttons:
            for button in row:
                button.config(text=" ")
