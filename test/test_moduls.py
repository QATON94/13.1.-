import pytest

from src.moduls import Category, Product, Smartphone, LawnGrass
from src.setings import TEST_PATH


@pytest.fixture()
def path_test_json():
    return TEST_PATH


def test_product(path_test_json):
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
    Product.add_new_product(product)
    assert product[1].name == 'Xiaomi Redmi Note 10'
    assert product[1].description == '256GB, Серый цвет, 200MP камера'
    assert product[1].price == 20000.0
    assert product[1].quantity == 5
    assert product[0] + product[1] == 961000.0
    print(product)


def test_smartphone(path_test_json):
    phone1 = Smartphone('Xiaomi Redmi Note 10', '256 GB,', 20000.0, 2, 'High',
                        'S+', '256 GB', 'red')
    phone2 = Smartphone('Xiaomi Redmi Note 11', '512 GB,', 40000.0, 2, 'High',
                        'S+', '512 GB', 'blue')
    assert phone1.performance == 'High'
    assert phone1.model == 'S+'
    assert phone2.amount_built_in_memory == '512 GB'


def test_lawn_grass(path_test_json):
    grass1 = LawnGrass('Мятлика', 'Мятлика Лугового 1 кг', 1500.00, 2,
                       'Russia', '3 мес', 'green')
    assert grass1.producing_country == 'Russia'
    assert grass1.germination_period == '3 мес'
    assert grass1.color == 'green'


def test_add(path_test_json):
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
