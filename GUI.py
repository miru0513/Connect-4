import tkinter as tk
from tkinter import messagebox
from Game import Game
from play import ComputerPlayer


class Connect4GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect 4")
        self.game = Game()
        self.current_player = self.game.human

        self.canvas = tk.Canvas(root, width=700, height=600, bg="blue")
        self.canvas.pack()

        self.board_ui = [[None for _ in range(7)] for _ in range(6)]
        self.create_board()
        self.root.bind("<Button-1>", self.handle_click)

    def create_board(self):
        for row in range(6):
            for col in range(7):
                x0, y0 = col * 100 + 10, row * 100 + 10
                x1, y1 = x0 + 80, y0 + 80
                self.board_ui[row][col] = self.canvas.create_oval(x0, y0, x1, y1, fill="white", outline="black")

    def handle_click(self, event):
        col = event.x // 100
        if self.game.board.is_valid_move(col):
            self.game.board.drop_piece(col, self.current_player.piece)
            self.update_board()
            if self.game.check_game_over(self.current_player):
                messagebox.showinfo("Game Over", f"{self.current_player.name} wins!")
                self.reset_game()
                return
            self.current_player = self.game.switch_player(self.current_player)
            if isinstance(self.current_player, ComputerPlayer):
                self.computer_move()

    def computer_move(self):
        self.root.after(500, self._computer_turn)

    def _computer_turn(self):
        col = self.current_player.get_move(self.game.board)
        self.game.board.drop_piece(col, self.current_player.piece)
        self.update_board()
        if self.game.check_game_over(self.current_player):
            messagebox.showinfo("Game Over", f"{self.current_player.name} wins!")
            self.reset_game()
            return
        self.current_player = self.game.switch_player(self.current_player)

    def update_board(self):
        for row in range(6):
            for col in range(7):
                color = "white"
                if self.game.board.matrixboard[row][col] == "X":
                    color = "red"
                elif self.game.board.matrixboard[row][col] == "O":
                    color = "yellow"
                self.canvas.itemconfig(self.board_ui[row][col], fill=color)

    def reset_game(self):
        self.game.reset()
        self.current_player = self.game.human
        self.update_board()


if __name__ == "__main__":
    root = tk.Tk()
    Connect4GUI(root)
    root.mainloop()
