class View:
    def welcome_to_game(self):
        print("Начнем игру. Удачи!")

    def print_table(self, board):
        """
        Вывод игровой доски в консоль
        :return:
        """
        print(*board[:3])
        print(*board[3:6])
        print(*board[6:])

    def welcome_to_move(self, player):
        print(f"{player} выбери ячейку, чтобы сделать ход. Нажми цифру свободной ячейки (1 - 9): ")

    def message_to_winner(self, player):
        print(f"Поздравляем! Игрок {player} победил!")

    def message_if_dead_heat(self):
        print("Ничья")

    def position_is_full(self):
        print("Эта клетка занята. Попробуйте другую")
