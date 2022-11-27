#todo: Представить структуру БД из курсовой работы в виде описания классов ORM системы
#  см. model.py  Заполнить стуктуру(таблицы) тестовыми данными с использования синтаксиса SQL Alchemy ORM
# см. документацию по CRUD операциям:
# https://flask-sqlalchemy.palletsprojects.com/en/latest/queries/#insert-update-delete

from model import Filter, Customers, Workers, db, app

filter = Filter(country='thailand', city='phyket', duration='14', nutrition='bb', hotel='4', price='2000')
with app.app_contex():
    db.session.add(filter)
    db.session.commit()

filter = Filter(country='egypt', city='hurgada', duration='7', nutrition='all', hotel='5', price='1500')
with app.app_contex():
    db.session.add(filter)
    db.session.commit()

customers = Customers(surname='ivanova', age='35', discount=True)
with app.app_contex():
    db.session.add(customers)
    db.session.commit()

workers = Workers(surname='petrova')
with app.app_contex():
   db.session.add(workers)
   db.session.commit()