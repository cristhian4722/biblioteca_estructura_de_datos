from tkinter import ttk
from PIL._tkinter_finder import tk


class DataTable:
    keys_data = None

    def __init__(self, titles_table, table_items, view_name, app):
        self.titles_table = titles_table
        self.table_items = table_items
        self.table = None
        self.id_row = None
        self.view_name = view_name
        self.app = app

    def on_row_selected(self, event):
        selected_item = self.table.focus()
        values = self.table.item(selected_item, 'values')
        if isinstance(values, tuple):
            self.id_row = values[0]

    def create_table(self):
        self.table = ttk.Treeview(columns=self.titles_table, show="headings")
        style = ttk.Style()
        style.theme_use('alt')
        style.configure("Treeview.Heading",
                        font=("Arial", 14, "bold"),
                        foreground="#7D3C98",
                        anchor="w",
                        padding=8)

        for title in self.titles_table:
            self.table.column(title, anchor='center')
            self.table.heading(title, text=title)

        self.table.pack(fill="both", expand=True)
        if self.table_items is not None and len(self.table_items) > 0:
            self.keys_data = tuple(self.table_items[0].keys())
        for item in self.table_items:
            user_tuple = tuple(item[k] for k in self.keys_data)
            self.table.insert("", 'end', values=user_tuple)
        self.table.bind("<<TreeviewSelect>>", self.on_row_selected)

    def delete_item_table(self):
        if self.id_row is not None:
            index_delete = None
            for item in self.table_items:
                if item['id'] == self.id_row:
                    index_delete = self.table_items.index(item)

            if index_delete is not None:
                self.table_items.pop(index_delete)
                self.update_tabla()

    def create_item(self, data, second_list=None):
        from modules.users_services import view_user
        from modules.books_services import view_books
        item_field = {}
        for index, data_item in enumerate(data, start=1):
            parse_item = data_item.get("1.0", "end-1c")
            if parse_item is not None and parse_item != '':
                item_field[self.keys_data[index]] = parse_item
            else:
                return
        id_element = self.get_id_last_element()
        item_field['id'] = id_element
        item_field[self.keys_data[len(self.keys_data)-1]] = None
        self.table_items.append(item_field)
        if self.view_name == 'users':
            view_user(self.app, self.table_items, second_list)
        else:
            view_books(self.app, self.table_items, second_list)

    def update_tabla(self):
        for item in self.table.get_children():
            self.table.delete(item)
        for item in self.table_items:
            self.table.insert("", "end", values=tuple(item[k] for k in self.keys_data))

    def get_id_last_element(self):
        if self.table_items is None or len(self.table_items) <= 0:
            id_init = 'ele-1'
            return id_init

        id_element = self.table_items[-1]['id']
        text_ini, number_text = id_element.split("-")
        new_number = str(int(number_text) + 1).zfill(2)
        new_text = f"{text_ini}-{new_number}"
        return new_text


