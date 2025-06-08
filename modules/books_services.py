import json

from modules.graph_book import Grafo
from modules.module_components import get_data
from modules.data_table import DataTable
from principal.main_components import create_title, create_custom_buttom, view_form, refresh_app


def view_books(app, list_element=None, second_list=None):
    from principal.main_app import view_main
    route = "resources/data/books.json"
    field_user = ['ID', 'ISBN', 'Nombre', 'Prestado a']
    books_list = {'state': True, 'content': list_element}
    if books_list['content'] is None:
        books_list = get_data(route)
    list_books = {'book': list_element}
    if second_list is not None:
        list_books['user'] = second_list
    refresh_app(app)
    data_table = None

    if books_list['state']:
        data_table = DataTable(field_user, books_list['content'], 'books', app)
        btn_c = create_custom_buttom("Agregar Libro", "#2ecc71",
                                     lambda: view_form(app, ['Nit', 'Nombre'], 'Registrar libro',
                                                       'books', data_table.create_item, list_element, second_list))
        btn_p = create_custom_buttom("Sugerencias", "#7D3C98", lambda: view_recommendations(app, data_table.recomend))
        btn_c.pack(padx=1, pady=3)
        btn_c.config(width=15, height=1)
        btn_b = create_custom_buttom("Eliminar Libro", "#e74c3c", lambda: data_table.delete_item_table())
        btn_b.pack(padx=1, pady=3)
        btn_b.config(width=15, height=1)
        btn_p.pack(padx=1, pady=3)
        btn_p.config(width=15, height=1)

    btn_v = create_custom_buttom("Volver", "#3498db", lambda: view_main(app, list_books))
    btn_v.pack(padx=1, pady=3)
    btn_v.config(width=15, height=1)
    if data_table is not None:
        data_table.create_table()


def view_recommendations(app, id):
    field_user = ['ID', 'ISBN', 'Nombre', 'Prestado a']
    route = "resources/data/books.json"
    grafo = Grafo()

    try:
        with open(route, "r", encoding="utf-8") as f:
            libros_data = json.load(f)
    except FileNotFoundError:
        print('Error: Ruta de datos incorrecta')
    except json.JSONDecodeError:
        print('Error: Ruta de datos incorrecta')

    for data in libros_data:
        grafo.agregar_libro(data)

    grafo.construir_relaciones()
    for frame in app.winfo_children():
        frame.destroy()
    data_table = DataTable(field_user, grafo.recomendar(id), 'users', app)
    data_table.create_table()
    btn_r = create_custom_buttom('Volver', '#3498db',lambda: view_books(app))
    btn_r.pack(padx=5, pady=5)
    btn_r.config(width=15, height=1)
