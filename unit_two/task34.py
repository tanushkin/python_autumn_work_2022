#todo: Сделать рефакторинг кода задачи task1  22 лекции .
#  1. Реализовать из класса DB синглтон. Экземляр класса(подключение) должно быть единственным.
#  2. Реализовать  фабрику которая создает модели различных производителей

from abc import ABC, abstractmethod
class AbsCar(ABC):
    @abstractmethod
    def sold(self):
        pass
    @abstractmethod
    def discount(self):
        pass

class Car(AbsCar):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        """Инициализируйте атрибуты brand и model"""
    @classmethod
    def make_lada(cls):
        return cls('Z', 'Урал')
        "реализуйте метод для создания  автомобиля Lada"

    @classmethod
    def make_mercedes(cls):
        "реализуйте метод для создания  автомобиля Mercedes"
        return cls('ZZ', 'Урал1')

    @classmethod
    def make_toyota(cls):
        return cls('ZZZ', 'Урал2')
        "реализуйте метод для создания создания Toyota"

    def __repr__(self):
        return (f"brand {self.brand}")
        "Реализуйте логику дандера"
    def sold(self):
        """Автомобиль продан"""
        print(f"Автомобиль {self.brand} {self.model} продан ")

    def discount(self):
        """Скидка на автомобиль"""
        print(f"На автомобиль {self.brand} {self.model} скидка 5%")

print(Car.make_toyota())
element = Car.make_toyota()
element.sold()
# 3. Реализовать для класса Car абстрактный класс который содержит
# aбстрактные методы sold, discount

    # def sold(self):
    #     """Автомобиль продан"""
    #     print(f"Автомобиль {self.brand} {self.model} продан ")
    #
    # def discount(self):
    #     """Скидка на автомобиль"""
    #     print(f"На автомобиль {self.brand} {self.model} скидка 5%")