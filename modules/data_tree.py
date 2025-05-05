class NodeBook:
    def __init__(self, dict_book):
        self.dict_book = dict_book
        self.left = None
        self.right = None


class TreeBook:
    def __init__(self):
        self.root = None
        self.table_head = None
        self.max_id = None

    def insert(self, dict_book):
        self.root = self.assign_node(self.root, dict_book)

    def assign_node(self, node, dict_book):
        if node is None:
            return NodeBook(dict_book)
        if dict_book['nombre'].lower() < node.dict_book['nombre'].lower():
            node.left = self.assign_node(node.left, dict_book)
        elif dict_book['nombre'].lower() > node.dict_book['nombre'].lower():
            node.right = self.assign_node(node.right, dict_book)
        return node

    def read_books(self, table):
        def _inorder(node_book):
            if node_book:
                if self.table_head is None:
                    self.table_head = tuple(node_book.dict_book.keys())

                _inorder(node_book.left)
                self.asign_max_id(node_book.dict_book['id'])
                book_tuple = tuple(node_book.dict_book[k] for k in self.table_head)
                table.insert("", 'end', values=book_tuple)
                _inorder(node_book.right)

        _inorder(self.root)
        return self.table_head

    def insert_book(self, dict_book):
        new_book = NodeBook(dict_book)

        if self.root is None:
            self.root = new_book
            return

        current_book = self.root
        while True:
            if dict_book['nombre'].lower() < current_book.dict_book['nombre'].lower():
                if current_book.left is None:
                    current_book.left = new_book
                    break
                current_book = current_book.left
            else:
                if current_book.right is None:
                    current_book.right = new_book
                    break
                current_book = current_book.right

    def delete_by_name(self, nombre):
        def _eliminar(nodo, nombre_param):
            if nodo is None:
                return None

            if nombre_param < nodo.dict_book["nombre"]:
                nodo.left = _eliminar(nodo.left, nombre_param)
            elif nombre_param > nodo.dict_book["nombre"]:
                nodo.right = _eliminar(nodo.right, nombre_param)
            else:
                # Nodo encontrado
                if nodo.left is None:
                    return nodo.right
                elif nodo.right is None:
                    return nodo.left

                # Caso 3: nodo con dos hijos
                sucesor = _minimo(nodo.right)
                nodo.dict_book = sucesor.dict_book
                nodo.right = _eliminar(nodo.right, sucesor.dict_book["nombre"])

            return nodo

        def _minimo(nodo):
            while nodo.left:
                nodo = nodo.left
            return nodo

        self.root = _eliminar(self.root, nombre)

    def asign_max_id(self, id_str):
        try:
            int_id = int(id_str.split('-')[-1])

            if self.max_id is None:
                self.max_id = id_str
            else:
                int_max_id = int(self.max_id.split('-')[-1])
                if int_id > int_max_id:
                    self.max_id = id_str

        except Exception as e:
            print(f"Error al procesar ID: {id_str} → {e}")
