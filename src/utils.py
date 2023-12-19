import json


def get_json_file(path):
    with open(path, encoding='utf=8') as json_file:
        product_json = json.load(json_file)
    return product_json
