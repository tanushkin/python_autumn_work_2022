# БД «Поликлиника».
# Описание предметной области. База данных создаётся для
# информационного обслуживания регистрационного отдела поликлиники. БД
# должна содержать информацию о врачах, ведущих прием, расписании приема, и
# пациентах, проживающих на участке, закрепленном за данной поликлиникой.
#  Готовые запросы :
# 1. Выдавать сводную информацию обо всех врачах поликлиники;
# 2. Выдавать сводную информацию о пациентах;
# 3. Выдавать информацию о записи пациента к врачу;
# 4. Выдавать информацию о приеме врачей на указанную дату;
# 5. Выдавать информацию о пациентах, имеющих льготы на приобретение
# лекарств.

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="variant_14",
    user="tanushkin",
    password="123")

cur = conn.cursor()

# 1. Выдавать сводную информацию обо всех врачах поликлиники;
print('1. Выборка сводной информации обо всех врачах поликлиники')
SQL_SELECTING_ALL_COLUMNS = f"""SELECT *
                            FROM vrach"""

cur.execute(SQL_SELECTING_ALL_COLUMNS)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 2. Выдавать сводную информацию о пациентах;
print('2. Выборка сводной информации о пациентах')
SQL_SELECTING_ALL_COLUMNS = f"""SELECT *
                            FROM pacient"""

cur.execute(SQL_SELECTING_ALL_COLUMNS)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 3. Выдавать информацию о записи пациента к врачу;
print('3. Выдавать информацию о записи пациента к врачу')
zapis_po_uchastky = input('Введите номер участка: ')
SQL_SELECT_PO_UCHASTKY = f"""SELECT p.surname, p.name, v.surname, v.name, v.patroin
                            FROM pacient p, vrach v
                            WHERE  p.uchastok = '{zapis_po_uchastky}'"""

cur.execute(SQL_SELECT_PO_UCHASTKY)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 4. Выдавать информацию о приеме врачей на указанную дату;
print('4. Выдавать информацию о приеме врачей на указанную дату')
data_priema = input('Введите дату: ')

SQL_PRIEM_VRACHA = f"""SELECT id_vrach, vremya, den_nedeli
                    FROM raspisanie
                    WHERE  data = '{data_priema}'"""
# 2022-11-01
cur.execute(SQL_PRIEM_VRACHA)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 5. Выдавать информацию о пациентах, имеющих льготы на приобретение лекарств.
print('5. Выдавать информацию о пациентах, имеющих льготы на приобретение лекарств')

# llo_number = input('Введите запрос: ')
SQL_LLO = f"""SELECT *
              FROM pacient
              WHERE llo is true"""

cur.execute(SQL_LLO)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()
conn.close()