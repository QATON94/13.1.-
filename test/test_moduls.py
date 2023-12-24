import pytest

from src.moduls import get_category, get_product


@pytest.fixture()
def products():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для "
                           "удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                }
            ]
        }
    ]


def test_get_category(products):
    category = get_category(products)
    assert category[0].name == "Смартфоны"
    assert category[0].description == ("Смартфоны, как средство не только коммуникации, но и получение дополнительных "
                                       "функций для удобства жизни")
    assert category[0].commodities == ["Samsung Galaxy C23 Ultra", "Iphone 15"]
    assert category[0].number_categories == 1
    assert category[0].number_unique_products == 2


def test_get_product(products):
    product = get_product(products)
    assert product[0].name == "Samsung Galaxy C23 Ultra"
    assert product[0].description == "256GB, Серый цвет, 200MP камера"
    assert product[1].price == 210000.0
    assert product[0].quantity_stock == 5
