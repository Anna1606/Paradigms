# Задача №1
# Дан список целых чисел numbers.
# Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

# Быстрая сортировка (quicksort)
def sort_list_imperative(numbers):
    def quick_sort(list_of_numbers, start, end):
        left = start  # наибольший элемент
        right = end  # наименьший элемент
        pivot = list_of_numbers[round((start + end) / 2)]  # опорный элемент для разбиения списка на две части
        # до тех пор пока индексы слева и справа не пересекутся повторяем цикл
        while left <= right:
            # последовательно сравниваем значения с опорными
            while list_of_numbers[left] > pivot:
                left += 1

            while pivot > list_of_numbers[right]:
                right -= 1
            # меняем местами найденные элементы, чтобы все элементы левее пивота были больше либо равны ему
            if left <= right:
                list_of_numbers[left], list_of_numbers[right] = list_of_numbers[right], list_of_numbers[left]
                left += 1
                right -= 1
        # запускаем рекурсию для сортировки слева от пивота
        if left < end:
            quick_sort(list_of_numbers, left, end)
        # запускаем рекурсию для сортировки справа от пивота
        if start < right:
            quick_sort(list_of_numbers, start, right)
    quick_sort(numbers, 0, len(numbers) - 1)
    return numbers


# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
def sort_list_declarative(numbers):
    return numbers.sort(reverse=True)


# Проверка работы кода
lst = [4, 8, 3, 5, 9, 1]
sort_list_imperative(lst)
print(lst)

lst1 = [4, 8, 3, 5, 9, 1]
sort_list_declarative(lst1)
print(lst1)
