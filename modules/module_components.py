import json


def get_data(route):
    data = {'state': False}
    try:
        with open(route, "r", encoding="utf-8") as f:
            json_data = json.load(f)
            data['state'] = True
            data['content'] = json_data
    except FileNotFoundError:
        data['content'] = 'Error: Ruta de datos incorrecta'
    except json.JSONDecodeError:
        data['content'] = "Error: El archivo JSON tiene un formato incorrecto"
    return data
