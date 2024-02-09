import pytest

from src.moduls import Category, Product, Smartphone, LawnGrass
from src.setings import TEST_PATH


@pytest.fixture()
def path_test_json():
    return TEST_PATH


def test_category(path_test_json):
    category = Category.init_from_file_for_category(path_test_json)
    assert category[0].name == "Телевизоры"
    assert category[0].description == ('Современный телевизор, который позволяет наслаждаться просмотром, станет '
                                       'вашим другом и помощником')
    assert category[0].number_categories == 1
    assert category[0].total_number_of_unique_products == 1
    print(category)


def test_get_product(path_test_json):
    product = Product.init_from_file_for_product(path_test_json)
    assert product[0].name == "55\" QLED 4K"
    assert product[0].description == "Фоновая подсветка"
    assert product[0].price == 123000.0
    assert product[0].quantity == 7
    print(product)


def test_smartphone():
    phone1 = Smartphone('Xiaomi Redmi Note 10', '256 GB,', 20000.0, 2, 'High',
                        'S+', '256 GB', 'red')
    phone2 = Smartphone('Xiaomi Redmi Note 11', '512 GB,', 40000.0, 2, 'High',
                        'S+', '512 GB', 'blue')
    assert phone1.performance == 'High'
    assert phone1.model == 'S+'
    assert phone2.amount_built_in_memory == '512 GB'


def test_lawn_grass():
    grass1 = LawnGrass('Мятлика', 'Мятлика Лугового 1 кг', 1500.00, 2,
                       'Russia', '3 мес', 'green')
    assert grass1.producing_country == 'Russia'
    assert grass1.germination_period == '3 мес'
    assert grass1.color == 'green'


def test_add():
    phone1 = Smartphone('Xiaomi Redmi Note 10', '256 GB,', 20000.0, 2, 'High',
                        'S+', '256 GB', 'red')
    phone2 = Smartphone('Xiaomi Redmi Note 11', '512 GB,', 40000.0, 2, 'High',
                        'S+', '512 GB', 'blue')
    grass1 = LawnGrass('Мятлика', 'Мятлика Лугового 1 кг', 1500.00, 2,
                       'Russia', '3 мес', 'green')
    assert phone1 + phone2 == 120000.0
    try:
        grass1 + phone1
    except Exception as e:
        assert e


def test_product_append():
    phone1 = Smartphone('Xiaomi Redmi Note 10', '256 GB,', 20000.0, 2, 'High',
                        'S+', '256 GB', 'red')
    phone2 = Smartphone('Xiaomi Redmi Note 10', '256 GB,', 22000.0, 3, 'High',
                        'S+', '256 GB', 'red')
    grass1 = LawnGrass('Мятлика', 'Мятлика Лугового 1 кг', 1500.00, 2,
                       'Russia', '3 мес', 'green')
    category = Category("Смартфоны", "средство не только коммуникации", [{
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }])
    products = Product.append_product(phone1, grass1)
    assert len(products) == 2
    products = Product.append_product(category, products)
    assert len(products) == 2
    products = Product.append_product(phone2, products)
    assert len(products) == 2
    assert products[1].price == 20000.0
    assert products[1].quantity == 5


def test_avg_all_price(path_test_json):
    category = Category.init_from_file_for_category(path_test_json)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        []
    )
    assert Category.avg_all_price(category1) == 0
    assert Category.avg_all_price(category[0]) == 123000.0