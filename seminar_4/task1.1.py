squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Вывод: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Вывод: [2, 4, 6, 8, 10]

# Создание множества, содержащего квадраты чисел от 1 до 5
squares_set = {x ** 2 for x in range(1, 6)}
print(squares_set)  # Вывод: {1, 4, 9, 16, 25}

# Создание словаря, где ключами являются числа от 1 до 5, а значениями - их квадраты
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(squares_dict)  # Вывод: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Генерация списка списков с числами от 1 до 3 в каждом внутреннем списке
matrix = [[x for x in range(1, 4)] for _ in range(3)]
print(matrix)


from functools import reduce

# Список студентов с баллами
students = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 88},
    {"name": "Charlie", "score": 92},
    {"name": "David", "score": 78},
]

# Используем reduce для суммирования баллов студентов
total_score = reduce(lambda x, y: x + y["score"], students, 0)

print("Общий суммарный балл всех студентов:", total_score)

# functools.reduce(function, iterable[, initializer])
# Apply function of two arguments cumulatively to the items of iterable, from left to right,
# so as to reduce the iterable to a single value.
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
# The left argument, x, is the accumulated value and the right argument, y,
# is the update value from the iterable. If the optional initializer is present,
# it is placed before the items of the iterable in the calculation,
# and serves as a default when the iterable is empty.
# If initializer is not given and iterable contains only one item, the first item is returned.
#
# Roughly equivalent to:
#
# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#     return value
