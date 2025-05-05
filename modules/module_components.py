import json

from modules.data_tree import TreeBook


def get_data(route):
    data = {'state': False}
    try:
        with open(route, "r", encoding="utf-8") as f:
            json_data = json.load(f)
            data['state'] = True
            data_list = tree_transform(json_data, route)
            data['content'] = data_list
    except FileNotFoundError:
        data['content'] = 'Error: Ruta de datos incorrecta'
    except json.JSONDecodeError:
        data['content'] = "Error: El archivo JSON tiene un formato incorrecto"
    return data


def tree_transform(list_item, route):
    if route != 'resources/data/books.json':
        return list_item
    tree_book = TreeBook()
    for book in list_item:
        tree_book.insert(book)
    return tree_book
