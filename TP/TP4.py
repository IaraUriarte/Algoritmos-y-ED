# # EJERCICIO 6

# class Nodo:
#     def __init__(self, info=None):
#         self.info = info
#         self.siguiente = None

# class Lista:
#     def __init__(self):
#         self.inicio = None
#         self.tamanio = 0

#     def insertar(self, dato, campo_orden='nombre'):
#         nodo = Nodo(dato)
#         if self.inicio is None:
#             self.inicio = nodo
#         elif campo_orden is None or dato[campo_orden].lower() < self.inicio.info[campo_orden].lower():
#             nodo.siguiente = self.inicio
#             self.inicio = nodo
#         else:
#             actual = self.inicio
#             while actual.siguiente is not None and actual.siguiente.info[campo_orden].lower() <= dato[campo_orden].lower():
#                 actual = actual.siguiente
#             nodo.siguiente = actual.siguiente
#             actual.siguiente = nodo
#         self.tamanio += 1

#     def eliminar(self, clave, campo='nombre'):
#         actual = self.inicio
#         anterior = None
#         while actual is not None:
#             if actual.info[campo].lower() == clave.lower():
#                 if anterior is None:
#                     self.inicio = actual.siguiente
#                 else:
#                     anterior.siguiente = actual.siguiente
#                 self.tamanio -= 1
#                 return actual.info
#             anterior = actual
#             actual = actual.siguiente
#         return None

#     def busqueda(self, clave, campo='nombre'):
#         actual = self.inicio
#         while actual is not None:
#             if actual.info[campo].lower() == clave.lower():
#                 return actual
#             actual = actual.siguiente
#         return None

#     def barrido(self):
#         actual = self.inicio
#         while actual is not None:
#             print(actual.info)
#             actual = actual.siguiente

#     def __iter__(self):
#         actual = self.inicio
#         while actual is not None:
#             yield actual.info
#             actual = actual.siguiente

# # a.
# def eliminar_linterna_verde(lista):
#     eliminado = lista.eliminar("Linterna Verde", "nombre")
#     if eliminado:
#         print(f"Se eliminó correctamente a {eliminado['nombre']}")
#     else:
#         print("Linterna Verde no se encontró en la lista.")

# # b.
# def mostrar_anio_wolverine(lista):
#     nodo = lista.busqueda("Wolverine", "nombre")
#     if nodo:
#         print(f"El año de aparición de Wolverine es {nodo.info['anio_aparicion']}")
#     else:
#         print("Wolverine no se encuentra en la lista.")

# # c.
# def cambiar_casa_dr_strange(lista):
#     nodo = lista.busqueda("Dr. Strange", "nombre")
#     if not nodo:
#         nodo = lista.busqueda("Doctor Strange", "nombre")
    
#     if nodo:
#         casa_anterior = nodo.info['casa']
#         nodo.info['casa'] = "Marvel"
#         print(f"Se cambió la casa de {nodo.info['nombre']} de '{casa_anterior}' a '{nodo.info['casa']}'.")
#     else:
#         print("Dr. Strange no se encontró en la lista.")

# # d.
# def mostrar_heroes_con_traje_o_armadura(lista):
#     print("Superhéroes con traje o armadura en su biografía:")
#     encontrados = False
#     for heroe in lista:
#         bio = heroe['biografia'].lower()
#         if "traje" in bio or "armadura" in bio:
#             print(heroe['nombre'])
#             encontrados = True
#     if not encontrados:
#         print("Ninguno.")

# # e.
# def mostrar_heroes_anteriores_1963(lista):
#     print("Superhéroes con fecha de aparición anterior a 1963:")
#     encontrados = False
#     for heroe in lista:
#         if heroe['anio_aparicion'] < 1963:
#             print(f"{heroe['nombre']} (Casa: {heroe['casa']}, Año: {heroe['anio_aparicion']})")
#             encontrados = True
#     if not encontrados:
#         print("Ninguno.")

# # f.
# def mostrar_casa_capitana_y_mujer_maravilla(lista):
#     print("Casa de comic de Capitana Marvel y Mujer Maravilla:")
#     for nombre in ["Capitana Marvel", "Mujer Maravilla"]:
#         nodo = lista.busqueda(nombre, "nombre")
#         if nodo:
#             print(f"{nodo.info['nombre']}: {nodo.info['casa']}")
#         else:
#             print(f"{nombre} no se encuentra en la lista.")

# # g.
# def mostrar_info_flash_y_starlord(lista):
#     print("Información detallada de Flash y Star-Lord:")
#     for nombre in ["Flash", "Star-Lord"]:
#         nodo = lista.busqueda(nombre, "nombre")
#         if nodo:
#             info = nodo.info
#             print(f"Nombre: {info['nombre']}")
#             print(f"Año aparición: {info['anio_aparicion']}")
#             print(f"Casa: {info['casa']}")
#             print(f"Biografía: {info['biografia']}")
#         else:
#             print(f"- {nombre} no se encuentra en la lista.")

# # h.
# def listar_heroes_letras_b_m_s(lista):
#     print("Superhéroes cuyos nombres comienzan con B, M o S:")
#     encontrados = False
#     for heroe in lista:
#         inicial = heroe['nombre'][0].upper()
#         if inicial in ['B', 'M', 'S']:
#             print(heroe['nombre'])
#             encontrados = True
#     if not encontrados:
#         print("Ninguno.")

# # i.
# def contar_superheroes_por_casa(lista):
#     conteo = {}
#     for heroe in lista:
#         casa = heroe['casa']
#         conteo[casa] = conteo.get(casa, 0) + 1
    
#     print("Cantidad de superhéroes por casa de comic:")
#     for casa, cantidad in conteo.items():
#         print(f"{casa}: {cantidad}")

# # BLOQUE PRINCIPAL 
# if __name__ == "__main__":
#     lista_superheroes = Lista()

#     # Datos de prueba
#     superheroes = [
#         {
#             "nombre": "Linterna Verde",
#             "anio_aparicion": 1940,
#             "casa": "DC",
#             "biografia": "Miembro de los Green Lantern Corps que posee un anillo de poder y usa un traje verde."
#         },
#         {
#             "nombre": "Wolverine",
#             "anio_aparicion": 1974,
#             "casa": "Marvel",
#             "biografia": "Mutante con factor de curación y garras de adamantium."
#         },
#         {
#             "nombre": "Dr. Strange",
#             "anio_aparicion": 1963,
#             "casa": "DC",
#             "biografia": "Hechicero supremo protector de la Tierra que viste túnica y capa mística."
#         },
#         {
#             "nombre": "Capitana Marvel",
#             "anio_aparicion": 1968,
#             "casa": "Marvel",
#             "biografia": "Carol Danvers, heroína cósmica que viste un traje espacial de combate."
#         },
#         {
#             "nombre": "Mujer Maravilla",
#             "anio_aparicion": 1941,
#             "casa": "DC",
#             "biografia": "Princesa amazona de Temiscira que combate con su armadura dorada y el lazo de la verdad."
#         },
#         {
#             "nombre": "Flash",
#             "anio_aparicion": 1940,
#             "casa": "DC",
#             "biografia": "Barry Allen, el hombre más rápido del mundo que usa un traje rojo especial."
#         },
#         {
#             "nombre": "Star-Lord",
#             "anio_aparicion": 1976,
#             "casa": "Marvel",
#             "biografia": "Peter Quill, líder de los Guardianes de la Galaxia con armadura ligera y blasters."
#         },
#         {
#             "nombre": "Batman",
#             "anio_aparicion": 1939,
#             "casa": "DC",
#             "biografia": "El caballero de la noche de Gotham que combate el crimen con su traje y tecnología."
#         },
#         {
#             "nombre": "Superman",
#             "anio_aparicion": 1938,
#             "casa": "DC",
#             "biografia": "El último hijo de Krypton, defensor de la justicia."
#         }
#     ]

#     for sh in superheroes:
#         lista_superheroes.insertar(sh)

#     print("a. Eliminar a Linterna Verde")
#     eliminar_linterna_verde(lista_superheroes)
#     print()

#     print("b. Mostrar año de aparición de Wolverine")
#     mostrar_anio_wolverine(lista_superheroes)
#     print()

#     print("c. Cambiar casa de Dr. Strange")
#     cambiar_casa_dr_strange(lista_superheroes)
#     print()

#     print("d. Mostrar superhéroes con traje o armadura en su biografía")
#     mostrar_heroes_con_traje_o_armadura(lista_superheroes)
#     print()

#     print("e. Mostrar superhéroes anteriores a 1963")
#     mostrar_heroes_anteriores_1963(lista_superheroes)
#     print()

#     print("f. Mostrar casa de Capitana Marvel y Mujer Maravilla")
#     mostrar_casa_capitana_y_mujer_maravilla(lista_superheroes)
#     print()

#     print("g. Mostrar información detallada de Flash y Star-Lord")
#     mostrar_info_flash_y_starlord(lista_superheroes)
#     print()

#     print("h. Listar superhéroes cuyos nombres comienzan con B, M o S")
#     listar_heroes_letras_b_m_s(lista_superheroes)
#     print()

#     print("i. Cantidad de superhéroes por casa de comic")
#     contar_superheroes_por_casa(lista_superheroes)
#     print()


# EJERCICIO 15

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
        elif campo_orden is None or str(dato[campo_orden]).lower() < str(self.inicio.info[campo_orden]).lower():
            nodo.siguiente = self.inicio
            self.inicio = nodo
        else:
            actual = self.inicio
            while actual.siguiente is not None and str(actual.siguiente.info[campo_orden]).lower() <= str(dato[campo_orden]).lower():
                actual = actual.siguiente
            nodo.siguiente = actual.siguiente
            actual.siguiente = nodo
        self.tamanio += 1

    def eliminar(self, clave, campo='nombre'):
        actual = self.inicio
        anterior = None
        while actual is not None:
            if str(actual.info[campo]).lower() == str(clave).lower():
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
            if str(actual.info[campo]).lower() == str(clave).lower():
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
def cantidad_pokemones_entrenador(lista_entrenadores, nombre_entrenador):
    nodo = lista_entrenadores.busqueda(nombre_entrenador, 'nombre')
    if nodo:
        cant = nodo.info['pokemones'].tamanio
        print(f"El entrenador {nombre_entrenador} tiene {cant} Pokémones.")
        return cant
    else:
        print(f"El entrenador {nombre_entrenador} no fue encontrado.")
        return 0

# b. 
def entrenadores_mas_de_tres_torneos(lista_entrenadores):
    print("Entrenadores que han ganado más de 3 torneos:")
    encontrados = False
    for entrenador in lista_entrenadores:
        if entrenador['torneos_ganados'] > 3:
            print(f"{entrenador['nombre']}; Torneos ganados: {entrenador['torneos_ganados']}")
            encontrados = True
    if not encontrados:
        print("Ninguno.")

# c. 
def pokemon_mayor_nivel_entrenador_mas_torneos(lista_entrenadores):
    if lista_entrenadores.tamanio == 0:
        print("La lista de entrenadores está vacía.")
        return

    max_torneos = -1
    entrenador_max = None
    for entrenador in lista_entrenadores:
        if entrenador['torneos_ganados'] > max_torneos:
            max_torneos = entrenador['torneos_ganados']
            entrenador_max = entrenador

    if entrenador_max:
        print(f"Entrenador con más torneos ganados: {entrenador_max['nombre']} ({entrenador_max['torneos_ganados']} torneos)")
        sublista = entrenador_max['pokemones']
        if sublista.tamanio == 0:
            print("El entrenador no tiene Pokémons.")
            return

        pok_max = None
        max_nivel = -1
        for pok in sublista:
            if pok['nivel'] > max_nivel:
                max_nivel = pok['nivel']
                pok_max = pok

        if pok_max:
            print(f"Pokémon de mayor nivel de {entrenador_max['nombre']}: {pok_max['nombre']} (Nivel: {pok_max['nivel']}, Tipo: {pok_max['tipo']}, Subtipo: {pok_max['subtipo']})")

# d. 
def mostrar_datos_entrenador_y_pokemones(lista_entrenadores, nombre_entrenador):
    nodo = lista_entrenadores.busqueda(nombre_entrenador, 'nombre')
    if nodo:
        ent = nodo.info
        print(f"Datos del entrenador {ent['nombre']}")
        print(f"Torneos Ganados: {ent['torneos_ganados']}")
        print(f"Batallas Ganadas: {ent['batallas_ganadas']}")
        print(f"Batallas Perdidas: {ent['batallas_perdidas']}")
        print(f"Cantidad de Pokémons: {ent['pokemones'].tamanio}")
        print("Pokémons:")
        for pok in ent['pokemones']:
            print(f"Nombre: {pok['nombre']}; Nivel: {pok['nivel']}; Tipo: {pok['tipo']}; Subtipo: {pok['subtipo']}")
    else:
        print(f"No se encontró al entrenador '{nombre_entrenador}'.")

# e. 
def entrenadores_porcentaje_victorias_mayor_79(lista_entrenadores):
    print("Entrenadores con porcentaje de victorias mayor al 79%:")
    encontrados = False
    for ent in lista_entrenadores:
        total_batallas = ent['batallas_ganadas'] + ent['batallas_perdidas']
        if total_batallas > 0:
            porcentaje = (ent['batallas_ganadas'] / total_batallas) * 100
            if porcentaje > 79:
                print(f"{ent['nombre']}: {porcentaje:.2f}% ({ent['batallas_ganadas']} ganadas de {total_batallas} batallas)")
                encontrados = True
    if not encontrados:
        print("Ninguno.")

# f. 
def entrenadores_con_pokemones_tipo_especifico(lista_entrenadores):
    print("Entrenadores con Pokémons de tipo Fuego/Planta o Agua/Volador:")
    encontrados = False
    for ent in lista_entrenadores:
        tiene_fuego_planta = False
        tiene_agua_volador = False

        tiene_fuego = False
        tiene_planta = False

        pokemones_coincidentes = []

        for pok in ent['pokemones']:
            t = pok['tipo'].lower()
            st = pok['subtipo'].lower()

            if t == 'fuego' or st == 'fuego': tiene_fuego = True
            if t == 'planta' or st == 'planta': tiene_planta = True

            is_fp = (t == 'fuego' and st == 'planta') or (t == 'planta' and st == 'fuego')
            is_av = (t == 'agua' and st == 'volador') or (t == 'volador' and st == 'agua')

            if is_fp or is_av:
                pokemones_coincidentes.append(f"{pok['nombre']} ({pok['tipo']}/{pok['subtipo']})")
                if is_fp: tiene_fuego_planta = True
                if is_av: tiene_agua_volador = True

        if (tiene_fuego and tiene_planta):
            tiene_fuego_planta = True

        if tiene_fuego_planta or tiene_agua_volador:
            coincidentes_str = f" -> {', '.join(pokemones_coincidentes)}" if pokemones_coincidentes else ""
            print(f"{ent['nombre']}{coincidentes_str}")
            encontrados = True

    if not encontrados:
        print("Ninguno.")

# g. 
def promedio_nivel_pokemones(lista_entrenadores, nombre_entrenador):
    nodo = lista_entrenadores.busqueda(nombre_entrenador, 'nombre')
    if nodo:
        ent = nodo.info
        sublista = ent['pokemones']
        if sublista.tamanio == 0:
            print(f"El entrenador {ent['nombre']} no tiene Pokémons.")
            return 0.0
        total_nivel = sum(pok['nivel'] for pok in sublista)
        promedio = total_nivel / sublista.tamanio
        print(f"El promedio de nivel de los Pokémons de {ent['nombre']} es: {promedio:.2f}")
        return promedio
    else:
        print(f"No se encontró al entrenador '{nombre_entrenador}'.")
        return 0.0

# h. 
def cantidad_entrenadores_tienen_pokemon(lista_entrenadores, nombre_pokemon):
    count = 0
    nombre_pokemon_lower = nombre_pokemon.lower()
    for ent in lista_entrenadores:
        for pok in ent['pokemones']:
            if pok['nombre'].lower() == nombre_pokemon_lower:
                count += 1
                break
    print(f"Cantidad de entrenadores que tienen al Pokémon {nombre_pokemon}: {count}")
    return count

# i. 
def entrenadores_con_pokemones_repetidos(lista_entrenadores):
    print("Entrenadores que tienen Pokémons repetidos:")
    encontrados = False
    for ent in lista_entrenadores:
        vistos = set()
        repetidos = set()
        for pok in ent['pokemones']:
            nombre_pok = pok['nombre'].lower()
            if nombre_pok in vistos:
                repetidos.add(pok['nombre'])
            else:
                vistos.add(nombre_pok)
        if repetidos:
            print(f"{ent['nombre']}: Pokémon repetido -> {', '.join(repetidos)}")
            encontrados = True
    if not encontrados:
        print("Ninguno.")

# j. 
def entrenadores_con_pokemones_especificos(lista_entrenadores):
    buscados = {"tyrantrum", "terrakion", "wingull"}
    print("Entrenadores que tienen a Tyrantrum, Terrakion o Wingull:")
    encontrados = False
    for ent in lista_entrenadores:
        poks_hallados = set()
        for pok in ent['pokemones']:
            if pok['nombre'].lower() in buscados:
                poks_hallados.add(pok['nombre'])
        if poks_hallados:
            print(f"{ent['nombre']} (Tiene: {', '.join(poks_hallados)})")
            encontrados = True
    if not encontrados:
        print("Ninguno.")

# k. 
def buscar_entrenador_y_pokemon(lista_entrenadores, nombre_entrenador, nombre_pokemon):
    print(f"Búsqueda del entrenador {nombre_entrenador} y el Pokémon {nombre_pokemon}")
    nodo_ent = lista_entrenadores.busqueda(nombre_entrenador, 'nombre')
    if not nodo_ent:
        print(f"El entrenador {nombre_entrenador} no existe.")
        return
    
    ent = nodo_ent.info
    sublista = ent['pokemones']
    nodo_pok = sublista.busqueda(nombre_pokemon, 'nombre')

    if nodo_pok:
        pok = nodo_pok.info
        print(f"El entrenador {ent['nombre']} sí tiene al Pokémon {pok['nombre']}.")
        print("Datos del entrenador:")
        print(f"Nombre: {ent['nombre']}")
        print(f"Torneos Ganados: {ent['torneos_ganados']}")
        print(f"Batallas Ganadas: {ent['batallas_ganadas']}")
        print(f"Batallas Perdidas: {ent['batallas_perdidas']}")
        print("Datos del Pokémon:")
        print(f"Nombre: {pok['nombre']}")
        print(f"Nivel: {pok['nivel']}")
        print(f"Tipo: {pok['tipo']}")
        print(f"Subtipo: {pok['subtipo']}")
    else:
        print(f"El entrenador {ent['nombre']} no tiene al Pokémon {nombre_pokemon}.")


# BLOQUE PRINCIPAL
if __name__ == "__main__":
    lista_entrenadores = Lista()

    # Datos de prueba
    datos_entrenadores = [
        {
            "nombre": "Ash Ketchum",
            "torneos_ganados": 5,
            "batallas_ganadas": 85,
            "batallas_perdidas": 15,
            "pokemones": [
                {"nombre": "Pikachu", "nivel": 90, "tipo": "Eléctrico", "subtipo": "Ninguno"},
                {"nombre": "Charizard", "nivel": 85, "tipo": "Fuego", "subtipo": "Volador"},
                {"nombre": "Bulbasaur", "nivel": 50, "tipo": "Planta", "subtipo": "Veneno"},
                {"nombre": "Pikachu", "nivel": 40, "tipo": "Eléctrico", "subtipo": "Ninguno"},  # Repetido
                {"nombre": "Tyrantrum", "nivel": 70, "tipo": "Roca", "subtipo": "Dragón"}
            ]
        },
        {
            "nombre": "Misty",
            "torneos_ganados": 2,
            "batallas_ganadas": 60,
            "batallas_perdidas": 40,
            "pokemones": [
                {"nombre": "Starmie", "nivel": 65, "tipo": "Agua", "subtipo": "Psíquico"},
                {"nombre": "Gyarados", "nivel": 75, "tipo": "Agua", "subtipo": "Volador"},
                {"nombre": "Psyduck", "nivel": 30, "tipo": "Agua", "subtipo": "Ninguno"},
                {"nombre": "Wingull", "nivel": 25, "tipo": "Agua", "subtipo": "Volador"}
            ]
        },
        {
            "nombre": "Brock",
            "torneos_ganados": 1,
            "batallas_ganadas": 50,
            "batallas_perdidas": 10,
            "pokemones": [
                {"nombre": "Onix", "nivel": 60, "tipo": "Roca", "subtipo": "Tierra"},
                {"nombre": "Geodude", "nivel": 45, "tipo": "Roca", "subtipo": "Tierra"},
                {"nombre": "Terrakion", "nivel": 80, "tipo": "Roca", "subtipo": "Lucha"}
            ]
        },
        {
            "nombre": "Cynthia",
            "torneos_ganados": 10,
            "batallas_ganadas": 120,
            "batallas_perdidas": 10,
            "pokemones": [
                {"nombre": "Garchomp", "nivel": 95, "tipo": "Dragón", "subtipo": "Tierra"},
                {"nombre": "Lucario", "nivel": 88, "tipo": "Lucha", "subtipo": "Acero"},
                {"nombre": "Milotic", "nivel": 85, "tipo": "Agua", "subtipo": "Ninguno"}
            ]
        }
    ]

    for ent in datos_entrenadores:
        sublista_poks = Lista()
        for pok in ent["pokemones"]:
            sublista_poks.insertar(pok, campo_orden='nombre')
        
        ent_dict = {
            "nombre": ent["nombre"],
            "torneos_ganados": ent["torneos_ganados"],
            "batallas_ganadas": ent["batallas_ganadas"],
            "batallas_perdidas": ent["batallas_perdidas"],
            "pokemones": sublista_poks
        }
        lista_entrenadores.insertar(ent_dict, campo_orden='nombre')


    print("a. Cantidad de Pokémons de un determinado entrenador.")
    cantidad_pokemones_entrenador(lista_entrenadores, "Ash Ketchum")
    print()

    print("b. Entrenadores que ganaron más de 3 torneos.")
    entrenadores_mas_de_tres_torneos(lista_entrenadores)
    print()

    print("c. Pokémon de mayor nivel del entrenador con más torneos ganados.")
    pokemon_mayor_nivel_entrenador_mas_torneos(lista_entrenadores)
    print()

    print("d. Datos completos de un entrenador y sus Pokémons.")
    mostrar_datos_entrenador_y_pokemones(lista_entrenadores, "Ash Ketchum")
    print()

    print("e. Entrenadores con porcentaje de victorias mayor al 79%.")
    entrenadores_porcentaje_victorias_mayor_79(lista_entrenadores)
    print()

    print("f. Entrenadores con Pokémons de tipo Fuego/Planta o Agua/Volador.")
    entrenadores_con_pokemones_tipo_especifico(lista_entrenadores)
    print()

    print("g. Promedio de nivel de Pokémons de un entrenador.")
    promedio_nivel_pokemones(lista_entrenadores, "Ash Ketchum")
    print()

    print("h. Cantidad de entrenadores que tienen un Pokémon específico.")
    cantidad_entrenadores_tienen_pokemon(lista_entrenadores, "Pikachu")
    print()

    print("i. Entrenadores con Pokémons repetidos.")
    entrenadores_con_pokemones_repetidos(lista_entrenadores)
    print()

    print("j. Entrenadores con Tyrantrum, Terrakion o Wingull.")
    entrenadores_con_pokemones_especificos(lista_entrenadores)
    print()

    print("k. Búsqueda de entrenador y Pokémon específico.")
    buscar_entrenador_y_pokemon(lista_entrenadores, "Ash Ketchum", "Pikachu")
    print()




