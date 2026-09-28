# EJERCICIO 6

class Nodo:
    def __init__(self, info=None):
        self.info = info
        self.siguiente = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

    def insertar(self, dato, campo_orden='nombre'):
        nodo = Nodo(dato)
        if self.inicio is None:
            self.inicio = nodo
        elif campo_orden is None or dato[campo_orden].lower() < self.inicio.info[campo_orden].lower():
            nodo.siguiente = self.inicio
            self.inicio = nodo
        else:
            actual = self.inicio
            while actual.siguiente is not None and actual.siguiente.info[campo_orden].lower() <= dato[campo_orden].lower():
                actual = actual.siguiente
            nodo.siguiente = actual.siguiente
            actual.siguiente = nodo
        self.tamanio += 1

    def eliminar(self, clave, campo='nombre'):
        actual = self.inicio
        anterior = None
        while actual is not None:
            if actual.info[campo].lower() == clave.lower():
                if anterior is None:
                    self.inicio = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.tamanio -= 1
                return actual.info
            anterior = actual
            actual = actual.siguiente
        return None

    def busqueda(self, clave, campo='nombre'):
        actual = self.inicio
        while actual is not None:
            if actual.info[campo].lower() == clave.lower():
                return actual
            actual = actual.siguiente
        return None

    def barrido(self):
        actual = self.inicio
        while actual is not None:
            print(actual.info)
            actual = actual.siguiente

    def __iter__(self):
        actual = self.inicio
        while actual is not None:
            yield actual.info
            actual = actual.siguiente








