import contextlib
import io
import json
import random
import sys
import unicodedata
from pathlib import Path

from queue_ import Queue

with contextlib.redirect_stdout(io.StringIO()):
    from tree import BinaryTree


ARCHIVO_POKEMONS = Path(__file__).with_name("pokemons.json")
TIPOS_CONSULTA = ("fantasma", "fuego", "acero", "eléctrico")
POKEMONS_OBJETIVO = ("Jolteon", "Charizard", "Mewtwo")


def normalizar(texto):
    # Normaliza mayúsculas y tildes para comparar nombres y tipos.
    descompuesto = unicodedata.normalize("NFD", texto.casefold())
    return "".join(
        caracter for caracter in descompuesto
        if unicodedata.category(caracter) != "Mn"
    )


def cargar_json(ruta=ARCHIVO_POKEMONS):
    with Path(ruta).open(encoding="utf-8") as archivo:
        pokemons = json.load(archivo)
    if not isinstance(pokemons, list):
        raise ValueError("El archivo debe contener una lista de Pokémon.")
    for pokemon in pokemons:
        campos = {
            "nombre", "numero", "tipos", "debilidades",
            "megaevolucion", "gigamax",
        }
        if not isinstance(pokemon, dict) or not campos.issubset(pokemon):
            raise ValueError(
                "Cada Pokémon debe tener nombre, numero, tipos, debilidades, "
                "megaevolucion y gigamax."
            )
    return pokemons


def guardar_json(lista, ruta=ARCHIVO_POKEMONS):
    with Path(ruta).open("w", encoding="utf-8") as archivo:
        json.dump(list(lista), archivo, ensure_ascii=False, indent=2)
        archivo.write("\n")


def armar_arboles(lista):
    arbol_nombre = BinaryTree()
    arbol_numero = BinaryTree()
    arbol_tipo = BinaryTree()

    random.shuffle(lista)
    for pokemon in lista:
        arbol_nombre.insert_node(normalizar(pokemon["nombre"]), pokemon)
        arbol_numero.insert_node(pokemon["numero"], pokemon)
        for tipo in pokemon["tipos"]:
            clave_tipo = normalizar(tipo)
            nodo = arbol_tipo.search(clave_tipo)
            if nodo is None:
                arbol_tipo.insert_node(clave_tipo, [pokemon])
            else:
                nodo.other_values.append(pokemon)
    return arbol_nombre, arbol_numero, arbol_tipo


def inorden(raiz):
    if raiz is not None:
        yield from inorden(raiz.left)
        yield raiz
        yield from inorden(raiz.right)


def por_nivel(raiz):
    pendientes = Queue()
    if raiz is not None:
        pendientes.arrive((raiz, 0))
        while pendientes.size() > 0:
            nodo, nivel = pendientes.attention()
            yield nodo, nivel
            if nodo.left is not None:
                pendientes.arrive((nodo.left, nivel + 1))
            if nodo.right is not None:
                pendientes.arrive((nodo.right, nivel + 1))


def mostrar(pokemon):
    print(
        f"#{pokemon['numero']:04d} {pokemon['nombre']} | "
        f"tipos: {', '.join(pokemon['tipos'])} | "
        f"débil frente a: {', '.join(pokemon['debilidades']) or 'ningún tipo'} | "
        f"megaevolución: {'sí' if pokemon['megaevolucion'] else 'no'} | "
        f"Gigamax: {'sí' if pokemon['gigamax'] else 'no'}"
    )


def buscar_por_numero(arbol_numero, numero):
    nodo = arbol_numero.search(numero)
    if nodo is None:
        print(f"No existe el Pokémon número {numero}.")
        return None
    mostrar(nodo.other_values)
    return nodo.other_values


def buscar_por_proximidad(arbol_nombre, texto):
    consulta = normalizar(texto.strip())
    if not consulta:
        print("Ingresá al menos un carácter para buscar.")
        return []

    encontrados = [
        nodo.other_values for nodo in inorden(arbol_nombre.root)
        if consulta in nodo.value
    ]
    for pokemon in encontrados:
        mostrar(pokemon)
    if not encontrados:
        print(f"No se encontraron Pokémon que coincidan con «{texto}».")
    return encontrados


def nombres_por_tipo(arbol_tipo, tipo):
    nodo = arbol_tipo.search(normalizar(tipo.strip()))
    if nodo is None:
        print(f"No se encontraron Pokémon de tipo {tipo}.")
        return []
    pokemons = sorted(
        nodo.other_values, key=lambda pokemon: normalizar(pokemon["nombre"])
    )
    nombres = [pokemon["nombre"] for pokemon in pokemons]
    print(f"Tipo {tipo} ({len(nombres)}): {', '.join(nombres)}")
    return nombres


def listado_por_numero(arbol_numero):
    pokemons = []
    for nodo in inorden(arbol_numero.root):
        pokemon = nodo.other_values
        print(f"{pokemon['numero']}: {pokemon['nombre']}")
        pokemons.append(pokemon)
    return pokemons


def listado_por_nombre(arbol_nombre):
    pokemons = []
    for nodo in inorden(arbol_nombre.root):
        pokemon = nodo.other_values
        print(f"{pokemon['nombre']} (#{pokemon['numero']})")
        pokemons.append(pokemon)
    return pokemons


def listado_por_nivel_nombre(arbol_nombre):
    pokemons = []
    for nodo, nivel in por_nivel(arbol_nombre.root):
        pokemon = nodo.other_values
        print(f"Nivel {nivel}: {pokemon['nombre']}")
        pokemons.append(pokemon)
    return pokemons


def debiles_frente_a(arbol_nombre, arbol_numero, nombre):
    atacante = arbol_nombre.search(normalizar(nombre))
    if atacante is None:
        print(f"{nombre} no está cargado.")
        return []

    tipos_atacante = {
        normalizar(tipo) for tipo in atacante.other_values["tipos"]
    }
    debiles = [
        nodo.other_values
        for nodo in inorden(arbol_numero.root)
        if tipos_atacante.intersection(
            normalizar(tipo)
            for tipo in nodo.other_values["debilidades"]
        )
    ]
    print(
        f"Débiles frente a {nombre} "
        f"({', '.join(atacante.other_values['tipos'])}) - {len(debiles)}:"
    )
    print(", ".join(pokemon["nombre"] for pokemon in debiles))
    return debiles


def cantidad_por_tipo(arbol_tipo):
    cantidades = {}
    for nodo in inorden(arbol_tipo.root):
        cantidad = len(nodo.other_values)
        cantidades[nodo.value] = cantidad
        print(f"{nodo.value}: {cantidad}")
    return cantidades


def contar_mega(arbol_numero):
    return sum(
        nodo.other_values["megaevolucion"]
        for nodo in inorden(arbol_numero.root)
    )


def contar_gigamax(arbol_numero):
    return sum(
        nodo.other_values["gigamax"]
        for nodo in inorden(arbol_numero.root)
    )


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else ARCHIVO_POKEMONS
    pokemons = cargar_json(ruta)
    print(f"Pokémon cargados: {len(pokemons)}")
    arboles = armar_arboles(pokemons)
    arbol_nombre, arbol_numero, arbol_tipo = arboles

    print("\n Ejercicio 1")
    print("\n punto a) Búsqueda por número: 25")
    buscar_por_numero(arbol_numero, 25)

    print("\n punto b) Búsqueda por proximidad: «bul»")
    buscar_por_proximidad(arbol_nombre, "bul")

    print("\n punto c) Nombres por tipo")
    for tipo in TIPOS_CONSULTA:
        nombres_por_tipo(arbol_tipo, tipo)

    print("\n punto d) Listado ascendente por número")
    listado_por_numero(arbol_numero)

    print("\n punto e) Listado ascendente por nombre")
    listado_por_nombre(arbol_nombre)

    print("\n punto f) Listado por nivel del árbol de nombres")
    listado_por_nivel_nombre(arbol_nombre)

    print("\n punto g) Pokémon débiles frente a los Pokémon indicados")
    for nombre in POKEMONS_OBJETIVO:
        debiles_frente_a(arbol_nombre, arbol_numero, nombre)

    print("\n punto h) Cantidad de Pokémon por tipo")
    cantidad_por_tipo(arbol_tipo)

    print("\n punto i) Pokémon con megaevolución:", contar_mega(arbol_numero))
    print("\n punto j) Pokémon con forma Gigamax:", contar_gigamax(arbol_numero))
    print()


if __name__ == "__main__":
    main()
