import pytest

from src.moduls import Category, Product
from src.setings import TEST_PATH


@pytest.fixture()
def path_test_json():
    return TEST_PATH


def test_product(path_test_json):
    category = Category.init_from_file_for_category(path_test_json)
    error = f"'Category' object has no attribute '__product'"
    assert category[0].name == "Телевизоры"
    assert category[0].description == ('Современный телевизор, который позволяет наслаждаться просмотром, станет '
                                       'вашим другом и помощником')
    assert category[0].displey_list_product == ['55" QLED 4K, 123000.0 руб. Остаток: 7 шт.']
    assert category[0].number_categories == 1
    assert category[0].total_number_of_unique_products == 1



def test_get_product(path_test_json):
    product = Product.init_from_file_for_product(path_test_json)
    assert product[0].name == "55\" QLED 4K"
    assert product[0].description == "Фоновая подсветка"
    assert product[0].price == 123000.0
    assert product[0].quantity == 7
