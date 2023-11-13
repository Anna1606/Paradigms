# Структурный подход

# N = 10
# sum = 0
# for i in range(1, N + 1):
#     sum += i
# print('Сумма чисел от 1 до ' + str(N) +' = ' + str(sum))


# Процедурный подход
def get_sum(N):
    summ = 0
    for i in range(1, N + 1):
        summ += i
    return summ


N = 10
print('Сумма чисел от 1 до ' + str(N) + ' = ' + str(get_sum(N)))