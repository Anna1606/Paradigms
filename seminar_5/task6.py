from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, ancestor, parent')

+ parent('Мария', 'Иван')
+ parent('Иван', 'Сергей')

ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= parent(X, Z) & ancestor(Z, Y)

# Запрос: кто является предком для Сергея?
print(ancestor(X, 'Сергей'))