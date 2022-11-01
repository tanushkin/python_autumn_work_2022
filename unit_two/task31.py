#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import logging

first = range(123)
count = 0
def decorator_one(func):
    def wrapper(first):
        global count
        count += 1
        func(first)
        logging.basicConfig(
            filename = "debug.log",
            filemode='at',
            level=logging.DEBUG,
            format='%(message)s, %(asctime)s ',
        )
        logging.debug(f'{func.__name__} {count}')

    return wrapper


@ decorator_one
def render(first):
    a = sorted(first)
    return a
@ decorator_one
def show(first):
    print(first)

render(first)
print(render)
