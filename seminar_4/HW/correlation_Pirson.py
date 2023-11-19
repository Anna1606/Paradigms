# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.

import statistics
import numpy as np


def pirson_correlation(arr1, arr2):
    if len(arr1) != len(arr2):
        print("длины массивов должны быть равны")
    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)
    return statistics.correlation(sorted_arr1, sorted_arr2)


# Создаем два случайных массива из 100 случайных чисел от 0 до 1
x = np.random.rand(100)
y = np.random.rand(100)
result = pirson_correlation(x, y)
print(result)
