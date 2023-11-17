# Пустая доска 3 × 3 клетки.
# Два игрока ходят по очереди, ставя свою фигуру в пустую ячейку.
# Любой горизонтальный, вертикальный или диагональный ряд,
# заполненный фигурой игрока, приносит ему выигрыш и заканчивает игру.
# Когда больше нет свободных полей — игра тоже заканчивается, ничьёй.
# Для простоты отображения выберем заглавные латинские «X» и «O» в качестве фигур игроков и пробел для пустой ячейки.
# Пусть «X» ходит первым.
class Board:
    """
    Доска для игры в крестики-нолики
    """
    def __init__(self):
        """
        Инициализация игрового поля
        """
        self.board = [1, 2, 3,  # игровое поле
                      4, 5, 6,
                      7, 8, 9]
        self.vin_map = [[0, 1, 2],  # карта с выигрышными полями
                        [3, 4, 5],
                        [6, 7, 8],
                        [0, 3, 6],
                        [1, 4, 7],
                        [2, 5, 8],
                        [0, 4, 8],
                        [2, 4, 6]]
        self.players = {"player1": "O", "player2": "X"}  # записываем в память игроков

    def __getitem__(self, item):
        """
        Получение значений на игровой доске
        :param item: игдекс элемента игровой доски
        :return: значение элемента
        """
        return self.board[item]

    def __setitem__(self, key, symbol):
        """
        Запись значений на игровой доске по ходу игры
        :param key: игдекс элемента игровой доски
        :param symbol: символ для записи
        :return: записанный элемент на доске
        """
        self.board[key] = symbol

    def is_position_empy(self, position):
        """
        Проверяем, свободна ли ячейка игровой доски
        :param position: индекс ячейки игровой доски
        :return: true or false
        """
        is_empty = False
        for i in self.players.values():
            if self.__getitem__(position) != i:
                is_empty = True
        return is_empty

    def check_winner(self, symbol):
        """
        Проверка победных комбинаций
        :param symbol: символ игрока
        :return: bool
        """
        check = False
        for i in self.vin_map:
            if self.board[i[0]] == symbol and self.board[i[1]] == symbol and self.board[i[2]] == symbol:
                check = True
                break
        return check

    def get_actual_board(self):
        """
        Получить актуальное состояние игровой доски
        :return:
        """
        return self.board
