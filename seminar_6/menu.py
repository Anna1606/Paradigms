class Menu:
    """
    Класс отвечает за отображение меню Секундомера
    """
    def print_menu(self):
        print("1 - start")
        print("2 - pause")
        print("3 - continue")
        print("4 - stop")
        print("5 - exit")

    def print_total_time(self, total):
        print("Total time: ", total)
