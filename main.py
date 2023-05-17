from game import Game


def main():
    game = Game()

    while True:
        game.board.display()

        row = int(input("Введіть рядок (0-2): "))
        col = int(input("Введіть column стовпець (0-2): "))

        if game.player_move(row, col):
            if game.game_over():
                print("Гравець X переміг!")
                break
            elif game.board.is_board_full():
                print("Нічия...")
                break

            game.computer_move()
            if game.game_over():
                print("Гравець O переміг!")
                break
            elif game.board.is_board_full():
                print("Нічия")
                break

    print("Кінець гри.")