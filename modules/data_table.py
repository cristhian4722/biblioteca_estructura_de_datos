from tkinter import ttk


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
            if self.view_name == 'users':
                self.id_row = values[0]
            else:
                self.id_row = values[2]

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
        if self.view_name == 'users':
            self.create_list_elements()
        elif self.view_name == 'books':
            self.create_tree_elements(self.table_items)
        self.table.bind("<<TreeviewSelect>>", self.on_row_selected)

    def delete_item_table(self):
        if self.id_row is not None:
            if self.view_name == 'users':
                self.delete_list_element()
            else:
                self.table_items.delete_by_name(self.id_row)
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
        item_field[self.keys_data[len(self.keys_data) - 1]] = None
        if self.view_name == 'users':
            self.table_items.append(item_field)
            view_user(self.app, self.table_items, second_list)
        else:
            self.table_items.insert_book(item_field)
            view_books(self.app, self.table_items, second_list)

    def update_tabla(self):
        for item in self.table.get_children():
            self.table.delete(item)
        if self.view_name == 'users':
            for item in self.table_items:
                self.table.insert("", "end", values=tuple(item[k] for k in self.keys_data))
        else:
            self.create_tree_elements(self.table_items)

    def get_id_last_element(self):
        if self.view_name == 'users':
            if self.table_items is None or len(self.table_items) <= 0:
                id_init = 'ele-1'
                return id_init
            id_element = self.table_items[-1]['id']
        else:
            if self.table_items is None or self.table_items.root is None:
                id_init = 'ele-1'
                return id_init
            id_element = self.table_items.max_id

        text_ini, number_text = id_element.split("-")
        new_number = str(int(number_text) + 1).zfill(2)
        new_text = f"{text_ini}-{new_number}"
        return new_text

    def create_list_elements(self):
        if self.table_items is not None and len(self.table_items) > 0:
            self.keys_data = tuple(self.table_items[0].keys())
        for item in self.table_items:
            user_tuple = tuple(item[k] for k in self.keys_data)
            self.table.insert("", 'end', values=user_tuple)

    def create_tree_elements(self, tree_book):
        if tree_book is not None:
            self.keys_data = tree_book.read_books(self.table)

    def delete_list_element(self):
        index_delete = None
        for item in self.table_items:
            if item['id'] == self.id_row:
                index_delete = self.table_items.index(item)

        if index_delete is not None:
            self.table_items.pop(index_delete)
            self.update_tabla()
