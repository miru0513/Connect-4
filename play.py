import random


class Player:
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece


class ComputerPlayer(Player):
    def __init__(self, piece):
        super().__init__("Computer", piece)

    def get_move(self, board):
        # Check if computer can win
        for col in range(board.columns):
            if board.is_valid_move(col):
                copyboard = [row[:] for row in board.matrixboard]
                board.drop_piece(col, self.piece)
                if board.check_winner(self.piece):
                    board.matrixboard = copyboard  # Revert board
                    return col
                board.matrixboard = copyboard  # Revert board

        # Check if human can win, block it
        human_piece = "X" if self.piece == "O" else "O"
        for col in range(board.columns):
            if board.is_valid_move(col):
                copyboard = [row[:] for row in board.matrixboard]
                board.drop_piece(col, human_piece)
                if board.check_winner(human_piece):
                    board.matrixboard = copyboard  # Revert board
                    return col
                board.matrixboard = copyboard  # Revert board

        # Random valid move
        valid_moves = [col for col in range(board.columns) if board.is_valid_move(col)]
        return random.choice(valid_moves)




