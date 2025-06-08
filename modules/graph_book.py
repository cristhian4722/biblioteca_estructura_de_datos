class Grafo:
    def __init__(self):
        self.nodos = {}
        self.adyacencia = {}

    def agregar_libro(self, libro_dict):
        libro_id = libro_dict["id"]
        self.nodos[libro_id] = libro_dict
        self.adyacencia[libro_id] = []

    def construir_relaciones(self):
        # Agrupar por prefijo
        grupos = {}
        for libro in self.nodos.values():
            prefijo = libro["id"][:3]
            grupos.setdefault(prefijo, []).append(libro)

        # Crear aristas entre libros con el mismo prefijo
        for libros in grupos.values():
            for i in range(len(libros)):
                for j in range(i + 1, len(libros)):
                    a = libros[i]["id"]
                    b = libros[j]["id"]
                    self.adyacencia[a].append(b)
                    self.adyacencia[b].append(a)

    def recomendar(self, libro_id):
        relacionados = self.adyacencia.get(libro_id, [])
        return [self.nodos[rel_id] for rel_id in relacionados]
