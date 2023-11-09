# пример 1
N = 10
sum = 0
for i in range(1, N + 1):
    sum += i
print("Сумма чисел от 1 до", N, "равна", sum)

# пример 2
numbers = [4, 2, 7, 1, 9, 3]
sorted_numbers = []
while numbers:
    min_num = min(numbers)
    sorted_numbers.append(min_num)
    numbers.remove(min_num)
print("Отсортированный список:", sorted_numbers)


# пример 3
def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
# Создаем двумерный массив для хранения длин НОП для подстрок str1 и str2.
    lcs_lengths = [[0] * (n + 1) for _ in range(m + 1)]

# Заполняем массив lcs_lengths в соответствии с алгоритмом динамического программирования.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs_lengths[i][j] = lcs_lengths[i - 1][j - 1] + 1
            else:
                lcs_lengths[i][j] = max(lcs_lengths[i - 1][j], lcs_lengths[i][j - 1])

# Теперь восстанавливаем саму НОП, начиная с конца массива lcs_lengths.
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif lcs_lengths[i - 1][j] > lcs_lengths[i][j - 1]:
            i -= 1
        else:
            j -= 1

# Инвертируем список, чтобы получить НОП в правильном порядке.
    lcs = lcs[::-1]
    return "".join(lcs)


# Пример использования:
str1 = "AGGTAB"
str2 = "GXTXAYB"
result = longest_common_subsequence(str1, str2)
print("Наибольшая общая подпоследовательность:", result)


# пример 4
numbers = [5, 2, 9, 8, 3, 6]
result = []

for num in numbers:
    if num % 2 == 0:  # Проверяем, является ли число четным.
        result.append(num)

result.sort(reverse=True)  # Сортируем по убыванию.
for i in range(len(result)):
    result[i] = result[i] ** 2  # Возводим в квадрат.
