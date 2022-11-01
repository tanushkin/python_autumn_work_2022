import psycopg2
from configparser import ConfigParser


def config(filename='database.ini', section='postgresgl'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    #         кортежи
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
params = config()
print('Connecting to the PostgreSQL database...')
conn = psycopg2.connect(**params)
cur = conn.cursor()

conn = psycopg2.connect(
    host="localhost",
    database="task",
    user="tanushkin",
    password="123")

cur = conn.cursor()
id_student = input("Введите ID студента")
# благодаря этому мы можем самым простым способом работатьс базой данных, строить графики

# заводим переменную, для красивости кода
SQL_GET_TASK_BY_STUDENT = f"""SELECT s.surname, t."name", t."condition"
                               FROM student s, student_task st, task t
                               WHERE s.id = st.id_student
                               AND st.id_task = t.id
                               AND s.id = {id_student}"""
cur.execute(SQL_GET_TASK_BY_STUDENT)
records = cur.fetchall()
for row in records:
    print(row)
#    и нам пришли студенты с задачами

print(records)
print(conn)
db.conn(close)