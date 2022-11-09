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
uch = input('Введите номер участка: ')
SQL_SELECT_PO_UCHASTKY = f"""SELECT v.*, p.* from grouppa g, pacient p, raspisanie r, vrach v
                             WHERE g.id_pacients = p.id
                             AND g.id_raspisanie = r.id
                             AND r.id_vrach = v.id
                             AND p.uchastok = '{uch}'"""

cur.execute(SQL_SELECT_PO_UCHASTKY)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 4. Выдавать информацию о приеме врачей на указанную дату;
print('4. Выдавать информацию о приеме врачей на указанную дату')
data_priema = input('Введите дату: ')

SQL_PRIEM_VRACHA = f"""SELECT vremya r, den_nedeli r, surname v, name v, patroin v
                    FROM raspisanie r, vrach v
                    WHERE  v.id = r.id_vrach
                    AND r.data = '{data_priema}'"""
cur.execute(SQL_PRIEM_VRACHA)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 5. Выдавать информацию о пациентах, имеющих льготы на приобретение лекарств.
print('5. Выдавать информацию о пациентах, имеющих льготы на приобретение лекарств')

# llo_number = input('Введите запрос: ')
SQL_LLO = f"""SELECT p.surname, p.name, p.patrion
              FROM pacient p
              WHERE llo is true"""

cur.execute(SQL_LLO)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()
conn.close()