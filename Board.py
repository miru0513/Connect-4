from texttable import Texttable


class Board:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.matrixboard = [[" " for _ in range(self.columns)] for _ in range(self.rows)]

    def display(self):
        table = Texttable()
        table.header([str(i) for i in range(1, self.columns + 1)])
        for row in self.matrixboard:
            table.add_row(row)
        print(table.draw())

    def is_valid_move(self, col):
        """
        :param col: coloana de verificat
        """
        return 0 <= col < self.columns and self.matrixboard[0][col] == " "

    def drop_piece(self, col, piece):
        """
        :param col:  Indexul coloanei în care se adaugă piesa
        :param piece: Simbolul piesei de adăuga
        """
        for row in reversed(self.matrixboard):
            if row[col] == " ":
                row[col] = piece
                return True
        return False

    def check_winner(self, piece):
        """
        :param piece:Simbolul piesei de verificat
        """

        # Check horizontal
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if all(self.matrixboard[row][col + i] == piece for i in range(4)):
                    return True

        # Check vertical
        for col in range(self.columns):
            for row in range(self.rows - 3):
                if all(self.matrixboard[row + i][col] == piece for i in range(4)):
                    return True

        # Check diagonal
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if all(self.matrixboard[row + i][col + i] == piece for i in range(4)):
                    return True

        # Check diagonal 2
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if all(self.matrixboard[row - i][col + i] == piece for i in range(4)):
                    return True

        return False

    def is_full(self):
        return all(self.matrixboard[0][col] != " " for col in range(self.columns))