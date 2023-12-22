class Category:
    def __init__(self, name, description, commodities, number_categories):
        self.name = name
        self.description = description
        self.commodities = commodities
        self.number_categories = number_categories
        self.number_unique_products = len(commodities)


class Product:
    def __init__(self, name, description, price, quantity_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_stock = quantity_stock


def get_category(products: list):
    initialization_categories = []
    for product_category in products:
        if product_category:
            initialization_category: Category = Category(
                name=product_category['name'],
                description=product_category['description'],
                commodities=get_commodities(product_category),
                number_categories=len(products))

            initialization_categories.append(initialization_category)
    return initialization_categories


def get_product(products: list):
    initialization_products = []
    for product_category in products:
        if product_category:
            for product in product_category['products']:
                initialization_product: Product = Product(
                    name=product['name'],
                    description=product['description'],
                    price=product['price'],
                    quantity_stock=product['quantity'])
                initialization_products.append(initialization_product)

    return initialization_products


def get_commodities(product: dict) -> list:
    list_products = []
    for name in product['products']:
        list_products.append(name['name'])
    return list_products

