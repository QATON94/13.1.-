import json
from typing import Any


class FromFile:
    @staticmethod
    def get_json_file(path: Any) -> list[dict]:
        """
        Получаем данные с json файла
        :param path: Путь к файлу
        :return: Список с данными json файла
        """
        with open(path, encoding='utf=8') as json_file:
            product_json = json.load(json_file)
        return product_json


class Category(FromFile):
    number_categories = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__product = products
        Category.number_categories += 1
        self.total_number_of_unique_products = len(self.__product)

    @property
    def products(self) -> list:
        """
        Получаем доступ к self.__product
        :return:
        """
        products = self.__product
        return products

    @property
    def display_list_product(self) -> str:
        """
        Геттер, который выводит список товаров
        """
        products = self.__product
        display_list = []
        for product in products:
            display_list.append(f'{product["name"]}, {product["price"]} руб. Остаток: {product["quantity"]} шт.')
        return '\n'.join(display_list)

    @property
    def display_quantity_products(self) -> str:
        """
        Геттер, который выводит общее количество продуктов в одной категории
        :return: Название категории, количество продуктов: X шт.
        """
        products = self.__product
        total_quantity = 0
        for product in products:
            total_quantity += product['quantity']
        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    @classmethod
    def init_from_file_for_category(cls, filename: Any) -> list:
        """
        Метод инициализации класса Category
        :param filename: путь к json файлу
        :return: Список с категориями продуктов
        """
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

    @property
    def change_price(self):
        """
        Геттер аргумента price
        """
        return self.price

    @change_price.setter
    def change_price(self, new_price: float):
        """
        Сеттер записывает новую цену, если цена ниже текущей то спрашивает разрешение на перезапись
        :param new_price: новая цена
        """
        if self.price > new_price:
            input_user = input("Eсли хотите изменить цену товара введите Y ")

            if input_user.lower() == 'y':
                print(input_user)
                self.price = new_price
        else:
            self.price = new_price

    @classmethod
    def init_from_file_for_product(cls, filename: Any) -> list:
        """
        Функция инициализирует класс Product
        :param filename: Путь к файлу
        :return: Список класса Product
        """
        data = cls.get_json_file(filename)
        initialization_products = []
        for item in data:
            for prod in item['products']:
                initialization_products.append(cls(**prod))
        return initialization_products

    @classmethod
    def add_new_product(cls, products: list) -> list:
        """
        Метод добавляет новый продукт или обновляет старый
        :param products: Список продуктов
        :return: обновленный список продуктов
        """
        new_product = Product.create_new_product()
        check = False
        i = 0
        for item in products:
            if item.name == new_product['name']:
                check = True
                products[i].change_price = float(new_product['price'])
                products[i].quantity += new_product['quantity']
            i += 1
        if not check:
            products.append(cls(**new_product))
        return products

    @staticmethod
    def create_new_product() -> dict:
        """
        Функция создает новый продукт
        :return: Словарь
        """
        # new_product = {
        #     "name": input('name = '),
        #     "description": input('description = '),
        #     "price": (input('price = ')),
        #     "quantity": input('quantity = ')
        # }
        new_product = {
            "name": "Xiaomi Redmi Note 10",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 20000.0,
            "quantity": 5
        }
        return new_product

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity
