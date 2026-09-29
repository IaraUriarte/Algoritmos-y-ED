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

# BLOQUE PRINCIPAL 
if __name__ == "__main__":
    lista_superheroes = Lista()

    # Datos de prueba
    superheroes = [
        {
            "nombre": "Linterna Verde",
            "anio_aparicion": 1940,
            "casa": "DC",
            "biografia": "Miembro de los Green Lantern Corps que posee un anillo de poder y usa un traje verde."
        },
        {
            "nombre": "Wolverine",
            "anio_aparicion": 1974,
            "casa": "Marvel",
            "biografia": "Mutante con factor de curación y garras de adamantium."
        },
        {
            "nombre": "Dr. Strange",
            "anio_aparicion": 1963,
            "casa": "DC",
            "biografia": "Hechicero supremo protector de la Tierra que viste túnica y capa mística."
        },
        {
            "nombre": "Capitana Marvel",
            "anio_aparicion": 1968,
            "casa": "Marvel",
            "biografia": "Carol Danvers, heroína cósmica que viste un traje espacial de combate."
        },
        {
            "nombre": "Mujer Maravilla",
            "anio_aparicion": 1941,
            "casa": "DC",
            "biografia": "Princesa amazona de Temiscira que combate con su armadura dorada y el lazo de la verdad."
        },
        {
            "nombre": "Flash",
            "anio_aparicion": 1940,
            "casa": "DC",
            "biografia": "Barry Allen, el hombre más rápido del mundo que usa un traje rojo especial."
        },
        {
            "nombre": "Star-Lord",
            "anio_aparicion": 1976,
            "casa": "Marvel",
            "biografia": "Peter Quill, líder de los Guardianes de la Galaxia con armadura ligera y blasters."
        },
        {
            "nombre": "Batman",
            "anio_aparicion": 1939,
            "casa": "DC",
            "biografia": "El caballero de la noche de Gotham que combate el crimen con su traje y tecnología."
        },
        {
            "nombre": "Superman",
            "anio_aparicion": 1938,
            "casa": "DC",
            "biografia": "El último hijo de Krypton, defensor de la justicia."
        }
    ]

    for sh in superheroes:
        lista_superheroes.insertar(sh)

    print("a. Eliminar a Linterna Verde")
    eliminar_linterna_verde(lista_superheroes)
    print()

    print("b. Mostrar año de aparición de Wolverine")
    mostrar_anio_wolverine(lista_superheroes)
    print()

    print("c. Cambiar casa de Dr. Strange")
    cambiar_casa_dr_strange(lista_superheroes)
    print()

    print("d. Mostrar superhéroes con traje o armadura en su biografía")
    mostrar_heroes_con_traje_o_armadura(lista_superheroes)
    print()

    print("e. Mostrar superhéroes anteriores a 1963")
    mostrar_heroes_anteriores_1963(lista_superheroes)
    print()

    print("f. Mostrar casa de Capitana Marvel y Mujer Maravilla")
    mostrar_casa_capitana_y_mujer_maravilla(lista_superheroes)
    print()

    print("g. Mostrar información detallada de Flash y Star-Lord")
    mostrar_info_flash_y_starlord(lista_superheroes)
    print()

    print("h. Listar superhéroes cuyos nombres comienzan con B, M o S")
    listar_heroes_letras_b_m_s(lista_superheroes)
    print()

    print("i. Cantidad de superhéroes por casa de comic")
    contar_superheroes_por_casa(lista_superheroes)
    print()




