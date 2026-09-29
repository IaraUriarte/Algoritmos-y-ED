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

# a.
def eliminar_linterna_verde(lista):
    eliminado = lista.eliminar("Linterna Verde", "nombre")
    if eliminado:
        print(f"Se eliminó correctamente a {eliminado['nombre']}")
    else:
        print("Linterna Verde no se encontró en la lista.")

# b.
def mostrar_anio_wolverine(lista):
    nodo = lista.busqueda("Wolverine", "nombre")
    if nodo:
        print(f"El año de aparición de Wolverine es {nodo.info['anio_aparicion']}")
    else:
        print("Wolverine no se encuentra en la lista.")

# c.
def cambiar_casa_dr_strange(lista):
    nodo = lista.busqueda("Dr. Strange", "nombre")
    if not nodo:
        nodo = lista.busqueda("Doctor Strange", "nombre")
    
    if nodo:
        casa_anterior = nodo.info['casa']
        nodo.info['casa'] = "Marvel"
        print(f"Se cambió la casa de {nodo.info['nombre']} de '{casa_anterior}' a '{nodo.info['casa']}'.")
    else:
        print("Dr. Strange no se encontró en la lista.")

# d.
def mostrar_heroes_con_traje_o_armadura(lista):
    print("Superhéroes con traje o armadura en su biografía:")
    encontrados = False
    for heroe in lista:
        bio = heroe['biografia'].lower()
        if "traje" in bio or "armadura" in bio:
            print(heroe['nombre'])
            encontrados = True
    if not encontrados:
        print("Ninguno.")

# e.
def mostrar_heroes_anteriores_1963(lista):
    print("Superhéroes con fecha de aparición anterior a 1963:")
    encontrados = False
    for heroe in lista:
        if heroe['anio_aparicion'] < 1963:
            print(f"{heroe['nombre']} (Casa: {heroe['casa']}, Año: {heroe['anio_aparicion']})")
            encontrados = True
    if not encontrados:
        print("Ninguno.")

# f.
def mostrar_casa_capitana_y_mujer_maravilla(lista):
    print("Casa de comic de Capitana Marvel y Mujer Maravilla:")
    for nombre in ["Capitana Marvel", "Mujer Maravilla"]:
        nodo = lista.busqueda(nombre, "nombre")
        if nodo:
            print(f"{nodo.info['nombre']}: {nodo.info['casa']}")
        else:
            print(f"{nombre} no se encuentra en la lista.")

# g.
def mostrar_info_flash_y_starlord(lista):
    print("Información detallada de Flash y Star-Lord:")
    for nombre in ["Flash", "Star-Lord"]:
        nodo = lista.busqueda(nombre, "nombre")
        if nodo:
            info = nodo.info
            print(f"Nombre: {info['nombre']}")
            print(f"Año aparición: {info['anio_aparicion']}")
            print(f"Casa: {info['casa']}")
            print(f"Biografía: {info['biografia']}")
        else:
            print(f"- {nombre} no se encuentra en la lista.")

# h.
def listar_heroes_letras_b_m_s(lista):
    print("Superhéroes cuyos nombres comienzan con B, M o S:")
    encontrados = False
    for heroe in lista:
        inicial = heroe['nombre'][0].upper()
        if inicial in ['B', 'M', 'S']:
            print(heroe['nombre'])
            encontrados = True
    if not encontrados:
        print("Ninguno.")

# i.
def contar_superheroes_por_casa(lista):
    conteo = {}
    for heroe in lista:
        casa = heroe['casa']
        conteo[casa] = conteo.get(casa, 0) + 1
    
    print("Cantidad de superhéroes por casa de comic:")
    for casa, cantidad in conteo.items():
        print(f"{casa}: {cantidad}")







