#todo. Транспонирование матрицы, transpose(matrix)
# level:hight
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы.
# Решить с использованием списковых включений.


# Пример:
# transpose([[1, 2, 3], [4, 5, 6]])
#
# [[1, 4], [2, 5], [3, 6]]
#
#
# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
#                ||3 6||
def msum(matrix):
    counter = [sum(num) for num in matrix]
    counter = sum(counter)
    print(counter)


msum([[1, 2, 3], [4, 5, 6]])