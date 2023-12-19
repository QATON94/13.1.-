from src.setings import PRODUCTS_PATH
from src.moduls import get_category
from src.utils import get_json_file


def main() ->None:
    products = get_json_file(PRODUCTS_PATH)
    category, product = get_category(products)
    print()
    # print(product.price)

if __name__ == '__main__':
    main()