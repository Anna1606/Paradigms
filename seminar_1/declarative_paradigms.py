# пример 1
N = 10
numbers = range(1, N + 1)
total = sum(numbers)
print("Сумма чисел от 1 до", N, "равна", total)

# пример 2
numbers = [5, 2, 9, 8, 3, 6]
# Декларативно выбираем четные числа, сортируем и возводим в квадрат.
result = sorted((x ** 2 for x in numbers if x % 2 == 0), reverse=True)
