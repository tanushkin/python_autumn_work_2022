# todo: Реализовать собственный класс исключений, которые будут вызываться (бросаться) в случае:
#  1. пользователь ввел некорректное значение в заданном диапазоне
#  2. результат запроса вернул 0 строк
#  3. Произошел разрыв соединения с сервером

# 1. Реализовать свой класс exception. пользователь ввел некорректное значение в заданном диапазоне
phone = input('Введите телефон:')
class IndentationError(Exception):

    def __init__(self):
        super().__init__()
try:
    if phone != "8-911-111-11-11":
        raise IndentationError()
except IndentationError as e:
    print(e)
else:
    print("Исключения нет!")
finally:
    print("Блок сработает в любом случае")
print(phone)

#  2. результат запроса вернул 0 строк

import psycopg2
conn = psycopg2.connect(
        dbname = "task",
        user = "tanushkin",
        host = "localhost",
        password = "123"
        )

cur = conn.cursor()
    # print('Выборка одной строки')

SQL_ONE_ROW_SELECTION = f"""SELECT id, name, condition
                            FROM task
                            WHERE id = 0"""
cur.execute(SQL_ONE_ROW_SELECTION)
# Retrieve query results
records = cur.fetchall()
for row in records:
    print(row)
    print(records)
if not records:
    print('пустая строка')
    print()

class IndentationError(Exception):

    def __init__(self):
        super().__init__()

try:
    if records = NULL:
    # if not records:
        raise IndentationError()
except IndentationError as e:
    print(e)
else:
    print("Исключения нет!")
finally:
    print("Блок сработает в любом случае")
print(records)

#  3. Произошел разрыв соединения с сервером

import psycopg2
try:
    conn = psycopg2.connect(
            dbname = "task",
            user = "tanushkin",
            host = "localhost",
            password = "1234"
        )
except psycopg2.OperationalError as e:
    print(e)
    print("Соединение не установлено")



# Виталий, почему у меня вот так не получилось сделать 1 задание?
# import psycopg2
# conn = psycopg2.connect(
#         dbname = "auth",
#         user = "tanushkin",
#         host = "localhost",
#         password = "123"
#         )
#
# # 1. Реализовать свой класс exception. пользователь ввел некорректное значение в заданном диапазоне
#
# class Auth(Exception):
#
#     def __init__(self, conn):
#         self.conn = conn
#         super().__init__()
#
#     def phone(self):
#         phone = input('Введите телефон:')
#
# try:
#     if phone != "8-911-111-11-11":
#         raise IndentationError()
# except IndentationError as e:
#     print(e)
# else:
#     print("Исключения нет!")
# finally:
#     print("Блок сработает в любом случае")
# print(phone)
#
# auth = Auth(conn)
# conn.close()