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
        """
        Инициализация класса Category
        :param name: Имя
        :param description: Описание
        :param products: Продукты
        """
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
        return self.__product

    def __str__(self) -> str:
        """
        :return: Название категории, количество продуктов: X шт.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product['quantity']
        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    def __repr__(self) -> str:
        """
        :return: Название категории, количество продуктов: X шт.
        """
        total_quantity = 0
        for product in self.products:
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
        """
        Инициализация класса
        :param name: Имя
        :param description: Описание
        :param price: Цена
        :param quantity: Количество
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """
        :return: Название продукта, X руб. Остаток: Y шт.
        """
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __repr__(self):
        """
        :return: Название продукта, X руб. Остаток: Y шт.
        """
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

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
    def add_new_product(cls, products=None) -> list | Any:
        """
        Метод добавляет новый продукт или обновляет старый
        :param products: Список продуктов
        :return: обновленный список продуктов
        """
        new_product = cls.create_new_product()
        check = False
        if products is None:
            products = []
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
        new_product = {
            "name": input('name = '),
            "description": input('description = '),
            "price": (input('price = ')),
            "quantity": input('quantity = ')
        }
        return new_product

    def __add__(self, other):

        if isinstance(other, self.__class__):
            return self.price * self.quantity + other.price * other.quantity
        raise print('Неверное сложение в продуктах')


class Smartphone(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, performance, model: str,
                 amount_built_in_memory: str, color: str):
        """
        Функция инициализирует класс Smartphone
        :param name: Имя
        :param description: Описание
        :param price: Цена
        :param quantity: Количество
        :param performance: производительность
        :param model: модель
        :param amount_built_in_memory: объем встроенной памяти
        :param color: Цвет продукта
        """
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.amount_built_in_memory = amount_built_in_memory
        self.color = color

    @staticmethod
    def create_new_product() -> dict:
        """
        Функция создает новый продукт
        :return: Словарь
        """
        new_product = {
            "name": input('name = '),
            "description": input('description = '),
            "price": (input('price = ')),
            "quantity": input('quantity = '),
            "performance": input('performance = '),
            "model": input('model = '),
            "amount_built_in_memory": input('amount_built_in_memory = '),
            "color": input('color = ')
        }
        return new_product

    @classmethod
    def add_new_product(cls, products=None) -> list:
        """
        Метод добавляет новый продукт или обновляет старый
        :param products: Список продуктов
        :return: обновленный список продуктов
        """
        return super().add_new_product()


class LawnGrass(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, producing_country: str,
                 germination_period: str, color: str):
        """
        Функция инициализирует класс LawnGrass
        :param name: Имя
        :param description: Описание
        :param price: цена
        :param quantity: количество
        :param producing_country: страна-производитель
        :param germination_period: срок прорастания
        :param color: цвет
        """
        super().__init__(name, description, price, quantity)
        self.producing_country = producing_country
        self.germination_period = germination_period
        self.color = color

    @staticmethod
    def create_new_product() -> dict:
        """
        Функция создает новый продукт
        :return: Словарь
        """
        new_product = {
            "name": input('name = '),
            "description": input('description = '),
            "price": (input('price = ')),
            "quantity": input('quantity = '),
            "producing_country": input('producing_country = '),
            "germination_period": input('germination_period = '),
            "color": input('color = ')
        }
        return new_product

    @classmethod
    def add_new_product(cls, products=None) -> list:
        """
        Метод добавляет новый продукт или обновляет старый
        :param products:
        :return:
        """
        return super().add_new_product()
