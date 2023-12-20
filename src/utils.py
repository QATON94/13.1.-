import json
from typing import Any


def get_json_file(path: Any) -> Any:
    """
    Получем данные с json файла
    :param path: Путь к файлу
    :return: Список с данными json файла
    """
    with open(path, encoding='utf=8') as json_file:
        product_json = json.load(json_file)
    return product_json
