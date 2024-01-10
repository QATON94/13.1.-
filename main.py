from src.moduls import Category, Product, Smartphone, LawnGrass
from src.setings import PRODUCTS_PATH


def main() -> None:
    categories = Category.init_from_file_for_category(PRODUCTS_PATH)
    products = Product.init_from_file_for_product(PRODUCTS_PATH)
    # Product.add_new_product(products)
    for category in categories:
        print(category.name)
        print(category.description)
        print(category.number_categories)
        print(category.total_number_of_unique_products)
        print('____________')

    for product in products:
        print(product.name)
        print(product.description)
        print(product.price)
        print(product.quantity)
        print(product)
        print('____________')

    print(products[0] + products[1])
    print(categories)
    print(products)

    phone1 = Smartphone('Xiaomi Redmi Note 10', '256 GB,', 20000.0, 2, 'High',
                        'S+', '256 GB', 'red')
    phone2 = Smartphone('Xiaomi Redmi Note 11', '512 GB,', 40000.0, 2, 'High',
                        'S+', '512 GB', 'blue')
    print(phone1.performance)
    print(phone1.model)
    print(phone1.amount_built_in_memory)
    print(phone1.color)

    grass1 = LawnGrass('Мятлика', 'Мятлика Лугового 1 кг', 1500.00, 2,
                       'Russia', '3 мес', 'green')
    print('--------------------')
    print(phone1 + phone2)
    print('--------------------')
    # print(grass1 + phone1)
    phone3 = Smartphone.add_new_product()
    print(phone3[0].color)

    grass2 = LawnGrass.add_new_product()
    print(grass2[0].color)


if __name__ == '__main__':
    main()
