import tkinter as tk
from PIL import Image, ImageTk
import os


def create_main_app():
    main_app = tk.Tk()
    main_app.title("Biblioteca App")
    main_app.geometry("1024x650")
    return main_app


def create_view(main_app):
    view = tk.Frame(main_app)
    view.tkraise()


def create_custom_buttom(text, color, callback):
    btn_style = {
        "font": ("Arial", 16, "bold"),
        "width": 20,
        "height": 2,
        "bd": 0,
        "fg": "white",
        "activebackground": "#34495e",
        "cursor": "hand2"
    }
    return tk.Button(text=text, bg=color, **btn_style, command=callback)


def create_image(path_folder, name_image, width, height):
    ruta_archivo_actual = os.path.abspath(__file__)
    ruta_raiz = os.path.dirname(os.path.dirname(ruta_archivo_actual))
    ruta_relativa = os.path.join(ruta_raiz, path_folder, name_image)
    imagen_pil = Image.open(ruta_relativa)
    imagen_pil = imagen_pil.resize((width, height), Image.LANCZOS)  # R
    imagen_tk = ImageTk.PhotoImage(imagen_pil)
    etiqueta_imagen = tk.Label(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk
    etiqueta_imagen.pack()
    return etiqueta_imagen


def create_title(text):
    titulo = tk.Label(text=text, font=("Arial", 20, "bold"), fg="#7D3C98")
    titulo.pack()


def view_form(app, text_list, title, old_frame, event_form, list_elements=None, second_list=None):
    from modules.users_services import view_user
    from modules.books_services import view_books
    from principal.main_app import view_main
    frames = {'main': lambda: view_main(app),
              'users': lambda: view_user(app, list_elements, second_list),
              'books': lambda: view_books(app, list_elements, second_list)}
    for frame in app.winfo_children():
        frame.destroy()
    create_title(title)
    btn_r = create_custom_buttom('Volver', '#3498db', frames[old_frame])
    btn_r.pack(padx=5, pady=5)
    btn_r.config(width=15, height=1)
    text_boxes = []
    for text in text_list:
        label = tk.Label(text=text)
        label.pack()
        text_box = tk.Text(app, height=1, width=50)
        text_box.pack(padx=10, pady=10)
        text_boxes.append(text_box)

    label_error = tk.Label(text='Debes registrar todos los campos', foreground='red', font=("Arial", 12, "bold"))
    label_error.pack()

    btn_g = create_custom_buttom('Registrar', '#2ecc71', lambda: event_form(text_boxes, second_list))
    btn_g.pack(padx=5, pady=5)
    btn_g.config(width=15, height=1)


def refresh_app(app):
    for frame in app.winfo_children():
        frame.destroy()
    create_view(app)


def close_view(view):
    view.quit()
