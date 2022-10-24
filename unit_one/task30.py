#todo: Найти сумму элементов матрицы
# Написать функцию msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.

# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)
# 21

import random


def msum(matrix):
    sum_ = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            sum_ = sum_ + matrix[i][j]
    return sum_


m = [[random.randint(0, 10) for x in range(2)] for y in range(2)]
print("Source matrix: ", m)
print("Matrix sum: ", msum(m))
