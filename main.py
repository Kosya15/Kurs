from game import Game


def main():
    """Головна функція програми. Виконує основний цикл гри "Хрестики-нулики"."""
    game = Game()

    while True:
        game.board.display()

        row = input("Введіть рядок дошки (0-2): ")
        col = input("Введіть стовпець дошки (0-2): ")

        try:
            row = int(row)
            col = int(col)
        except ValueError:
            print("Помилка: Рядок та стовпець мають бути цілими числами.")
            continue

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


if __name__ == "__main__":
    main()