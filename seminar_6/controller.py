from stopwatch import Stopwatch
from menu import Menu


class Controller:
    """
    Управление секундомером
    """
    def __init__(self):
        self.stopwatch = Stopwatch()
        self.menu = Menu()

    def run(self):
        while True:
            self.menu.print_menu()
            choice = input("Choose number: ")
            if choice == "1":
                self.stopwatch.start()
            elif choice == "2":
                self.stopwatch.pause()
            elif choice == "3":
                self.stopwatch.restart()
            elif choice == "4":
                self.stopwatch.stop()
            elif choice == "5":
                print("Exit")
                break
            # После выхода из цикла выводится общее время работы секундомера
        self.menu.print_total_time(self.stopwatch.get_time_format())
