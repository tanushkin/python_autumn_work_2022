# #todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 classwork/task3
# написать Save Game по следующему сценарию:
# В запущенной игре по нажатию клавиши S появляется вывод:
# 1. Продолжить
# 2. Сохранить игру
#
# При выборе пункта 1. игра продолжается.
# При выборе пункта 2. пользователю предлагается ввести название для
# сохранения, после чего нужно сделать сериализацию состояния игры.
# Законсервировать все объекты которые отвечают за состоянии игры в файл
# game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.
#
# При старте игры пользователю должен предлагатся выбор
# 1. Новая игра
# 2. Восстановить игру
# При выборе 1. начинается новая игра.
# При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
# Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.

import random
import pickle

magic_num = 10
max_count = 5
count = 0
data = []

def menu():
    out = f"1. Новая игра\n2. Продолжить игру\n3. Сохранить игру\n4.Загрузить игру"
    print(out)

def save_game():
    data = get_save_game()
    name = input("Введите название игры:")
    save_point = {"name":name, "magic_num": magic_num, "count": count}
    data.append(save_point)
    with open('game_dump.pkl', 'wb') as f:
        pickle.dump(data, f)

def get_save_game():
    with open('game_dump.pkl', "rb") as f:
        data = pickle.load(f)
        return data

def open_game():
    with open('game_dump.pkl', "rb") as f:
        data = pickle.load(f)
        cnt = 1
        for dict in data:
            str = f"{ cnt }: {dict['name']}"
            cnt = cnt + 1
            print(str)

        name_save_game = input("Введите имя")
        global magic_num, count
        for dict in data:
            if name_save_game == dict["name"]:
                magic_num = dict["magic_num"]
                count = dict["count"]
                print(f"Игра восстановлена {dict['name']}")

        # print(data)
def game():
    menu()
    num = int(input())
    global count
    if num == 4:
        open_game()
        num = 1

    if num == 1:
        # Начало игры
        while count < max_count:
            try:
                guess = input('введите число')
                guess = int(guess)
            except:
                pass
            if guess == magic_num:
                print('угадано', count, 'c попыток')
            elif guess == 's':
                save_game()
            elif guess == 'q':
                break
            else:
                count += 1
                print('не верное число, осталось', max_count - count, 'попыток')
    else:
        pass

game()
#open_game()