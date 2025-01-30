import tkinter as tk
from controller.controller import TicTacToeController

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeController(root)
    root.mainloop()
