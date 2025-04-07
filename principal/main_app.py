from modules.books_services import view_books
from modules.users_services import view_user
from principal.main_components import create_view, create_image, create_custom_buttom, close_view, refresh_app


def view_main(app, list_element=None):
    refresh_app(app)
    create_view(app)
    user_list = None
    book_list = None
    if list_element is not None:
        if 'user' in list_element:
            user_list = list_element['user']
        if 'book' in list_element:
            book_list = list_element['book']
    create_image('resources/images', 'logo.png', 200, 200)
    create_custom_buttom("Usuarios", "#3498db", lambda: view_user(app, user_list, book_list)).pack(padx=10, pady=10)
    create_custom_buttom("Libros", "#2ecc71", lambda: view_books(app, book_list, user_list)).pack(padx=10, pady=10)
    create_custom_buttom("Salir", "#e74c3c", lambda: close_view(app)).pack(padx=10, pady=10)
