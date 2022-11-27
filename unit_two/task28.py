# todo 1: Для игры "Морской бой" файл sea_battle.py написать создание игрового поля nxn

# todo 2: В игровой матрице nxn найти кол-во всех 1

#  Задачи решить через генераторы списков (списковые включения)

import random
def game_field(rows=5, kolumns=5):
    res = []
    for row in range(0, rows):
        line = [(lambda: random.randint(0, 1))() for _ in range(0, kolumns)]
        res.append(line)
    res = [[random.randint(0, 1) for _ in range(kolumns)] for _ in range(rows)]
    return res

def count_ship(field):
    line = [digit for row in field for digit in row]
    return line.count(1)


print("\n\nАнализ статистики")
stat = {}
count = []
mass = [(lambda: game_field(10, 10))() for _ in range(100)]
for i in mass:
    count.append(count_ship(i))
print(count)
for res in count:
    if res not in stat:
        stat[res] = 1
    else:
        stat[res] = stat[res] + 1
print(sorted(stat.items()))

print("\n\nАнализ статистики")
stat = {}
count = []