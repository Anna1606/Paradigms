# Переписать алгоритм в процедурном стиле
# Структурное программирование
# Определение функции merge_sort, которая выполняет сортировку методом слияния.
def merge_left_with_right_halfs(left_half, right_half):
    result = []  # переменная, для хранения отсортированного массива
    i = j = 0  # Инициализация индексов для объединения двух половин.

    # Объединение левой и правой половин в один отсортированный массив.
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:  # Сравнение элементов левой и правой половин.
            result.append(left_half[i])  # Если элемент из левой меньше, помещаем его в result.
            i += 1
        else:
            result.append(right_half[j])  # Если элемент из правой меньше, помещаем его в result.
            j += 1

    # Добавление оставшихся элементов из левой и правой половин (если такие есть).
    while i < len(left_half):
        result.append(left_half[i])
        i += 1

    while j < len(right_half):
        result.append(right_half[j])
        j += 1

    return result


def merge_sort(arr):
    # Проверка, что длина массива больше 1 (иначе сортировка не нужна).
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2  # Вычисление середины массива.
        left_half = arr[:mid]  # Создание левой половины массива.
        right_half = arr[mid:]  # Создание правой половины массива.

    # Рекурсивный вызов merge_sort для левой и правой половин массива.
        left_half_sorted = merge_sort(left_half)
        right_half_sorted = merge_sort(right_half)

    # Объединение левой и правой половин в один отсортированный массив.
        return merge_left_with_right_halfs(left_half_sorted, right_half_sorted)


my_array = [64, 34, 25, 12, 22, 11, 90]  # Создание неотсортированного массива.
my_array_sorted = merge_sort(my_array)  # Вызов функции сортировки слиянием.
print("Отсортированный массив (Merge Sort):", my_array_sorted)  # Вывод отсортированного массива.
