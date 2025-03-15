from Board import Board
from play import Player, ComputerPlayer


class Game:
    def __init__(self):
        self.board = Board()
        self.human = Player("Human", "X")
        self.computer = ComputerPlayer("O")

    def switch_player(self, current_player):
        return self.computer if current_player == self.human else self.human

    def check_game_over(self, current_player):
        if self.board.check_winner(current_player.piece):
            self.board.display()
            print(f"{current_player.name} wins!")
            return True
        if self.board.is_full():
            self.board.display()
            print("It's a tie!")
            return True
        return False

    def reset(self):
        self.board = Board()