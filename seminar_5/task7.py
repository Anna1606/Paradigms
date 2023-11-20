from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, age, total_age, number_of_people, average_age')

+ age('Мария', 30)
+ age('Иван', 40)
+ age('Алексей', 20)

total_age[X] = sum(Y, for_each=age[X, Y])
number_of_people[X] = count(Y, for_each=age[X, Y])
average_age[Y] = (total_age[X] / number_of_people[X])
