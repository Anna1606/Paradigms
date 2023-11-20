from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, age, average_age, total_age, number_of_people')

+ age('Мария', 30)
+ age('Иван', 40)
+ age('Алексей', 20)

# Определение общего возраста
total_age(X) <= sum_(Y, for_each= age(X, Y))

# Определение количества людей
number_of_people() <= count_(X, for_each= age(X, Y))

# Расчет среднего возраста
average_age(Y) <= (total_age(X) & number_of_people(Z)) & (Y == X/Z)

# Запрос среднего возраста
print(average_age(Y))