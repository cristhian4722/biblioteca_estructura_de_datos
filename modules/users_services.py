from modules.module_components import get_data
from modules.data_table import DataTable
from principal.main_components import  create_title, create_custom_buttom, view_form, refresh_app


def view_user(app, list_element=None, second_list=None):
    from principal.main_app import view_main
    route = "resources/data/users.json"
    field_user = ['ID', 'Nit', 'Nombre', 'Prestado']
    users = {'state': True, 'content': list_element}
    if users['content'] is None:
        users = get_data(route)
    list_users = {'user': list_element}
    if second_list is not None:
        list_users['book'] = second_list
    refresh_app(app)
    create_title("Usuarios")
    data_table = None

    if users['state']:
        data_table = DataTable(field_user, users['content'], 'users', app)
        btn_c = create_custom_buttom("Agregar usuario", "#2ecc71",
                                     lambda: view_form(app, ['Nit', 'Nombre'], 'Registrar usuario',
                                                       'users', data_table.create_item, list_element, second_list))
        btn_c.pack(padx=5, pady=5)
        btn_c.config(width=15, height=1)
        btn_b = create_custom_buttom("Eliminar usuario", "#e74c3c", lambda: data_table.delete_item_table())
        btn_b.pack(padx=5, pady=5)
        btn_b.config(width=15, height=1)

    btn_v = create_custom_buttom("Volver", "#3498db", lambda: view_main(app, list_users))
    btn_v.pack(padx=5, pady=5)
    btn_v.config(width=15, height=1)
    if data_table is not None:
        data_table.create_table()

