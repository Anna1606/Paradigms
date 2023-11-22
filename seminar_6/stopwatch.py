import time

# ДЗ: исправить ошибки подсчета времени, добавить комментарии, описать какую парадигму использовали.

'''В данном коде используется структурная парадигма программировани и MVP архитектура
'''

class Stopwatch:
    """
    Класс Секундомер, описывает модель работы секундомера
    """
    def __init__(self):
        """
        Конструктор секурндомера
        """
        self.start_time = None
        """Время начала работы секундомера"""
        self.bool_pause_time = False
        """Секундомер на паузе/в движении"""
        self.pause_start_time = None
        """Время начала паузы"""
        self.total_paused_time = 0
        """Общее время пауз"""

    def start(self):
        """запуск секундомера"""
        # Если секундомер еще не запущен
        if not self.start_time:
            # Запускаем секундомер
            self.start_time = time.time()
            # Если стоит пауза
        elif self.bool_pause_time:
            # Учитываем время паузы
            self.total_paused_time += time.time() - self.pause_start_time
            # Выходим из режима паузы
            self.bool_pause_time = False

    def pause(self):
        """Поставить секурдомер на паузу
        """
        # Если секундомер запущен и не стоит на паузе, то
        # ставим на паузу и запоминаем время начала паузы
        if self.start_time and not self.bool_pause_time:
            self.bool_pause_time = True
            self.pause_start_time = time.time()

    def restart(self):
        """
        Возобновить работу секуномера после паузы
        """
        # Если секундомер стоит на паузе, то возобновляем работу секундомера
        # и учитываем время приостановки на паузу
        if self.bool_pause_time:
            self.bool_pause_time = False
            self.total_paused_time += time.time() - self.pause_start_time

    def stop(self):
        """
        Остановить секундомер и сбросить все переменные
        """
        self.start_time = None
        self.bool_pause_time = False
        self.pause_start_time = None
        self.total_paused_time = 0

    def get_time(self):
        """
        :return: возвращает время работы в секундах
        """
        if self.start_time:
            if self.bool_pause_time:
                return self.pause_start_time - self.start_time - self.total_paused_time
            else:
                return time.time() - self.start_time - self.total_paused_time

    def get_time_format(self):
        """форматирование времени, выводимое в консоль"""
        time = int(self.get_time())
        min = time // 60
        sec = time % 60
        return f"{min:02}: {sec:02}"
