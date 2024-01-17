from src.moduls import Category, Product, Smartphone, LawnGrass
from src.setings import PRODUCTS_PATH


def main() -> None:
    products = Product.init_from_file_for_product(PRODUCTS_PATH)
    categories = Category.init_from_file_for_category(PRODUCTS_PATH)
    # new_product1 = Product.add_new_product()
    # product1 = Product(**new_product1)
    # for category in categories:
    #     print(category.name)
    #     print(category.description)
    #     print(category.number_categories)
    #     print(category.total_number_of_unique_products)
    #     print('____________')

    phone1 = Smartphone('Xiaomi Redmi Note 10 PRO MAX', '256 GB,', 20000.0, 2, 'High',
                        'S+', '256 GB', 'red')
    grass1 = LawnGrass('Мятлика', 'Мятлика Лугового 1 кг', 1500.00, 2,
                       'Russia', '3 мес', 'green')
    # products = Product.append_product(product1, products)
    products = Product.append_product(phone1, products)
    products = Product.append_product(grass1, products)
    # products = Product.append_product(categories, products)

    # for product in products:
    #     print(product.name)
    #     print(product.description)
    #     print(product.price)
    #     print(product.quantity)
    #     print(product)
    #     print('____________')


if __name__ == '__main__':
    main()
