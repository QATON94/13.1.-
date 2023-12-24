from src.moduls import Category, Product
from src.setings import PRODUCTS_PATH


def main() -> None:
    categories = Category.init_from_file(PRODUCTS_PATH)
    products = Product.get_products(PRODUCTS_PATH)
    Product.add_new_product(products)
    #
    # for category in categories:
    #     print(category.name)
    #     print(category.description)
    #     print(category.displey_list_product)
    #     print(category.number_categories)
    #     print(category.total_number_of_unique_products)
    #     print('____________')

    for product in products:
        print(product.name)
        print(product.description)
        print(product.price)
        print(product.quantity)
        print('____________')


if __name__ == '__main__':
    main()
