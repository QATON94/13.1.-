from src.moduls import get_category, get_product
from src.setings import PRODUCTS_PATH
from src.utils import get_json_file


def main() -> None:
    products_json = get_json_file(PRODUCTS_PATH)
    categories = get_category(products_json)
    products = get_product(products_json)
    for category in categories:
        print(category.name)
        print(category.description)
        print(category.commodities)
        print(category.number_categories)
        print(category.number_unique_products)
        print('____________')

    for product in products:
        print(product.name)
        print(product.description)
        print(product.price)
        print(product.quantity_stock)
        print('____________')


if __name__ == '__main__':
    main()
