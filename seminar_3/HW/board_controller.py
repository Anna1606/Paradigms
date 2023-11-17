from model_board import Board
from board_view import View


class Controller:
    def __init__(self):
        """
        Инициализация контроллера
        """
        self.board = Board()
        self.view = View()

    def run(self):
        """
        Запуск игры
        :return: играем, до выигрыша или ничьей
        """
        self.view.welcome_to_game()
        players = self.board.players
        game_over = False
        while not game_over:
            for actual_player, actual_symbol in players.items():
                self.view.print_table(self.board.get_actual_board())
                move_choice = int(input(self.view.welcome_to_move(actual_player))) - 1
                if self.board.is_position_empy(move_choice):
                    self.board.__setitem__(move_choice, actual_symbol)
                else:
                    self.view.position_is_full()
                if self.board.check_winner(actual_symbol):
                    self.view.message_to_winner(actual_player)
                    game_over = True
                    break
            if len(set(self.board.board)) == 2:
                self.view.message_if_dead_heat()
                game_over = True
