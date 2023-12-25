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

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__product = products
        Category.number_categories += 1
        self.total_number_of_unique_products = len(self.__product)

    @property
    def displey_list_product(self) -> list:
        """
        Геттер который выводит список товаров
        """
        products = self.__product
        displey_list = []
        for product in products:
            displey_list.append(f'{product["name"]}, {product["price"]} руб. Остаток: {product["quantity"]} шт.')
        return displey_list

    @classmethod
    def init_from_file_for_category(cls, filename: Any) -> list:
        """
        Метод иницилизации ксласса Category
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
        Сеттер записывет новую цену, если цена ниже текущей то спрашивает разрешение на перезапись
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
        Метод добовляет новый продукт или обновляет старый
        :param products: Список продуктов
        :return: обновленный список продуктов
        """
        new_product = Product.crate_new_product()
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
    def crate_new_product() -> dict:
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
