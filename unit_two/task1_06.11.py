# todo: Реализовать функционал систем для авторизации. Любой класс можно расширить до той функциональности которая
# потребуется в результате написания кода.
class DB:
    # '''Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются переменные
    #  (атрибуты доступа к БД) . Метод возвращает соединение.'''
    # def __init__(self, dbname, user, password):
    # # В констукторе инициализируем атрибуты доступа к БД
    #     pass

    def __init__(self, dbname, user, password):
        self.dbname = dbname
        self.user = user
        self.passw = password
    # def get_connect(self):
    #     # Метод возвращает соединение к БД
    #     pass

    def get_connect(self):
        try:
            return psycopg.connect(f'dbname = {self.dbname} user = {self.user} password = {self.passw}')

        except psycopg.errors.OperationalError as err:
            print('Ошибка подключения к БД\n', err)
            return None
# class Auth:
#     """Класс содержит методы регистрации, захода в систему и выхода из нее"""
#     is_auth = False
#     def registration(self):
#         """Метод создания профиля пользователя в системе """
#         pass
#
#     def login(self):
#         """Метод аутентификации пользователя в системе"""
#         pass
#
#     def logout(self):
#         Auth.is_auth = False


class Profile:
    # ''' Данный класс содержит конструктор и метод set_profile и get_profile для добавления и получения
    #  пользователя соответсвенно'''
    # def __init__(self, login, password, name, surname, age, tel, email):
    #     """В констукторе инициализируем атрибуты сущности Profile"""
    #     pass
    def __init__(self, login, password, name, surname, age, tel, email):
        self.login = login
        self.passw = password
        self.name = name
        self.surname = surname
        self.age = age
        self.tel = tel
        self.email = email
        self.today = datetime.date.today()
    # def set_profile(self, conn):
    #     """в аргументе conn передается дискриптор подключения к БД"""
    #     # Добавляет профиль в БД
    #     pass
    def set_profile(self, conn):
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT login FROM public.user WHERE login LIKE '{self.login}'")
                if cur.fetchone() == None:
                    cur.execute(f"""
                                INSERT INTO public.user (login, password, dt_create) 
                                VALUES ('{self.login}', '{self.passw}', '{self.today.strftime("%Y-%m-%d")}'""")
                    cur.execute(f"""
                                INSERT INTO profile (name, id_user, surname, age, tel, email)
                                VALUES ('{self.name}', (SELECT id_user FROM public.user WHERE login LIKE '{self.login}'), 
                                '{self.surname}', '{self.age}', '{self.tel}', '{self.email}')
                                """)

        except psycopg.Error as err:
            print(err)
            return None
    # def get_profile(self, conn):
    #     # Извлекает профиль из БД
    #     pass
    def get_profile(self, conn):
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                SELECT a.name, a.surname, a.age, a.tel, a.email 
                FROM profile a JOIN public.user b ON a.id_user = b.id_user
                WHERE b.login LIKE '{self.login}'""")
                return cur.fetchone()

        except psycopg.Error as err:
            print(err)
            return None