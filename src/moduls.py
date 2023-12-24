import json
from typing import Any


class FromFile:
    @staticmethod
    def get_json_file(path: Any) -> list[dict]:
        """
        Получем данные с json файла
        :param path: Путь к файлу
        :return: Список с данными json файла
        """
        with open(path, encoding='utf=8') as json_file:
            product_json = json.load(json_file)
        return product_json


class Category(FromFile):
    number_categories = 0

    def __init__(self, name: str, description: str, products):
        self.name = name
        self.description = description
        self.__product = Category.get_commodities(products)
        Category.number_categories += 1
        self.total_number_of_unique_products = len(self.__product)


    @classmethod
    def init_from_file(cls, filename):
        data = cls.get_json_file(filename)
        initialization_categories = []
        for item in data:
            initialization_categories.append(cls(**item))
        return initialization_categories

    @staticmethod
    def get_commodities(product: dict) -> list:
        """
        Получаем список товаров
        """
        list_products = []
        for name in product:
            list_products.append(name['name'])
        return list_products


class Product(FromFile):

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def get_products(cls, filename):
        """
        Функция инициализирует класс Product
        :param products: Список продукций
        :return: Список класса Product
        """
        data = cls.get_json_file(filename)
        initialization_products = []
        for item in data:
            for prod in item['products']:
                initialization_products.append(cls(**prod))

        return initialization_products
