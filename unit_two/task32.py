# todo: Реализовать класс "Игровой персонаж".
#  Класс должен содержать атрибуты(свойства): Идентификатор, Имя, Здоровье, Раса, Тип персонажа, урон.
#  Инициализация атрибутов(состояние объекта) должна происходить в конструкторе.
#  В классе реализовать метод изменения здоровья по нанесенному урону(параметр функции).
#  Заложить логику: При достижении порога здоровья персонаж погибает
#  В классе реализовать метод получения значения атрибута урона
#  При достижении порога здоровья персонаж погибает
#  Реализовать дандер __repr__ для отладки персонажа
#  Реализовать дандер вычитания __sub__()  написав логику "боя" которая срабатывает
#  в момент вычитания объектов класса obj1 - obj2 и заключается в вычитании из
#  здоровья первого объекта урона наносимого вторым объектом

# 1. реализовать свой класс exception
#
# login = "admin"
#
# class LoginNotFound(Exception):
#     pass
#
# try:
#     if login != "admin":
#         raise LoginNotFound


#
# try:
#td = open()

import random

new_id = int(input('Введите id персонажа: '))
new_health = int(input('Введите здоровье персонажа: '))
new_race = str(input('Введите расу персонажа: '))
new_type = str(input('Введите тип персонажа: '))
new_damage = random.randint(10, 100)

character_list_1 = [new_id, new_health, new_race, new_type, new_damage]

print()

new_id_2 = int(input('Введите id персонажа: '))
new_health_2 = int(input('Введите здоровье персонажа: '))
new_race_2 = str(input('Введите расу персонажа: '))
new_type_2 = str(input('Введите тип персонажа: '))
new_damage_2 = random.randint(10, 100)

character_list_2 = [new_id_2, new_health_2, new_race_2, new_type_2, new_damage_2]

print()


class GameCharacter:

    def __init__(self, id, health, race, characters_type, damage):
        self.id: int = id
        self.health: int = health
        self.race: str = race
        self.characters_type: str = characters_type
        self.damage: int = damage

    def __sub__(self, enemy):
        self.health -= enemy.damage
        if self.health < 0:
            self.health = 0

    def __repr__(self):
        return f"Персонаж с id {self.id} и уровнем здоровья {self.health} наносит противнику урон равный {self.damage}"


class Battle:

    def __init__(self, first_fighter, second_fighter):
        self.first_fighter = first_fighter
        self.second_fighter = second_fighter

    def fight(self):
        while self.first_fighter.health > 0 or self.second_fighter.health > 0:
            if self.first_fighter.health <= 0:
                print(f"\nПерсонаж с id {self.second_fighter.id} победил!")
                break
            elif self.second_fighter.health <= 0:
                print(f"\nПерсонаж с id {self.first_fighter.id} победил!")
                break
            else:
                print(repr(self.first_fighter))
                self.second_fighter.__sub__(self.first_fighter)
                print(repr(self.second_fighter))
                self.first_fighter.__sub__(self.second_fighter)


character_1 = GameCharacter(*character_list_1)
character_2 = GameCharacter(*character_list_2)

start_the_battle = Battle(character_1, character_2)
start_the_battle.fight()

