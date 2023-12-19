class Category:
    name: str
    description: str
    commodities: list
    number_categories: int
    number_unique_products: int

    def __init__(self, name, description, commodities):
        self.name = name
        self.description = description
        self.commodities = commodities
        # self.number_categories = number_categories
        # self.number_unique_products = number_unique_products

    @classmethod
    def get_quantity(cls, number_categories: int, number_unique_products: int):
        number_categories = number_categories
        number_unique_products = number_unique_products
        return


class Product:
    name: str
    description: str
    price: float
    quantity_stock: int

    def __init__(self, name, description, price, quantity_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_stock = quantity_stock


def get_category(products: list):
    initialization_categories = []
    initialization_products = []
    i = '1'
    for product_category in products:
        if product_category:
            initialization_category: Category = Category(
                name=product_category['name'],
                description=product_category['description'],
                commodities=get_commodities(product_category)
            )
            for product in product_category['products']:
                if product:
                    initialization_product: Product = Product(
                        name=product['name'],
                        description=product['description'],
                        price=product['price'],
                        quantity_stock=product['quantity']
                    )
                    initialization_products.append(initialization_product)
            initialization_categories.append(initialization_category)

    return initialization_categories, initialization_products


def get_commodities(product: dict) -> list:
    list_products = []
    for name in product['products']:
        list_products.append(name['name'])
    return list_products


def get_number_categories(product_category: dict):
    print(len(product_category['products']))
    return len(product_category['products'])
