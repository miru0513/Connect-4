import pyfiglet
from colorama import Fore, init
import random

from Game import Game
from play import ComputerPlayer

init(autoreset=True)
ascii_art = pyfiglet.figlet_format("Connect 4")
foreground_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
colorful_text = ""
for line in ascii_art.splitlines():
    for char in line:
        if char.strip():
            colorful_text += random.choice(foreground_colors) + char
        else:
            colorful_text += " "
    colorful_text += "\n"

print(colorful_text)


class UI:
    @staticmethod
    def get_human_move():
        while True:
            try:
                col = int(input("Enter column (1-7): ")) - 1
                if col < 0 or col > 6:
                    raise ValueError("Column out of range.")
                return col
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    @staticmethod
    def display_board(board):
        board.display()

    @staticmethod
    def show_turn_message(player):
        print(f"{player.name}'s turn ({player.piece})")


def main():
    while True:
        game = Game()
        current_player = game.human

        while True:
            UI.display_board(game.board)
            UI.show_turn_message(current_player)

            if isinstance(current_player, ComputerPlayer):
                col = current_player.get_move(game.board)
            else:
                col = UI.get_human_move()

            if not game.board.is_valid_move(col):
                print("Invalid move. Try again.")
                continue

            game.board.drop_piece(col, current_player.piece)

            if game.check_game_over(current_player):
                break

            current_player = game.switch_player(current_player)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()

