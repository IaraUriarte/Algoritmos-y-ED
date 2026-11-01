# EJERCICIO 5

from math import inf
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from graph import Graph


EQUIPOS = {
    "pc": ("Manjaro", "Parrot", "Fedora", "Ubuntu", "Mint"),
    "notebook": ("Red Hat", "Debian", "Arch"),
    "servidor": ("Guaraní", "MongoDB"),
    "router": ("Router 1", "Router 2", "Router 3"),
    "switch": ("Switch 1", "Switch 2"),
    "impresora": ("Impresora",),
}

CONEXIONES = (
    (25, "Red Hat", "Router 2"),
    (9, "Guaraní", "Router 2"),
    (50, "Router 2", "Router 3"),
    (37, "Router 2", "Router 1"),
    (43, "Router 3", "Router 1"),
    (61, "Router 3", "Switch 2"),
    (29, "Router 1", "Switch 1"),
    (17, "Switch 1", "Debian"),
    (18, "Switch 1", "Ubuntu"),
    (22, "Switch 1", "Impresora"),
    (80, "Switch 1", "Mint"),
    (40, "Switch 2", "Manjaro"),
    (12, "Switch 2", "Parrot"),
    (5, "Switch 2", "MongoDB"),
    (56, "Switch 2", "Arch"),
    (3, "Switch 2", "Fedora"),
)

AMBIENTES = (
    "cocina",
    "comedor",
    "cochera",
    "quincho",
    "baño 1",
    "baño 2",
    "habitación 1",
    "habitación 2",
    "sala de estar",
    "terraza",
    "patio",
)

CONEXIONES_CASA = (
    (4, "cocina", "comedor"),
    (9, "cocina", "cochera"),
    (3, "cocina", "baño 1"),
    (7, "cocina", "sala de estar"),
    (12, "cocina", "patio"),
    (10, "comedor", "quincho"),
    (5, "comedor", "baño 1"),
    (6, "comedor", "sala de estar"),
    (8, "comedor", "patio"),
    (7, "cochera", "quincho"),
    (6, "cochera", "patio"),
    (8, "quincho", "terraza"),
    (6, "baño 1", "habitación 1"),
    (4, "baño 2", "habitación 1"),
    (5, "habitación 1", "habitación 2"),
    (11, "habitación 1", "terraza"),
    (3, "baño 2", "habitación 2"),
    (9, "baño 2", "sala de estar"),
    (7, "habitación 2", "terraza"),
    (10, "sala de estar", "patio"),
)


def cargar_red() -> Graph:
    # h) La red se modela como un grafo no dirigido.
    grafo = Graph(is_dir=False)

    # a) Cada vértice guarda el tipo de equipo en other_values.
    for tipo, nombres in EQUIPOS.items():
        for nombre in nombres:
            grafo.add_vertex(nombre, other_values={"tipo": tipo})

    for peso, origen, destino in CONEXIONES:
        grafo.add_edge(peso, origen, destino)

    return grafo


def cargar_casa() -> Graph:
    grafo = Graph(is_dir=False)
    for ambiente in AMBIENTES:
        grafo.add_vertex(ambiente)

    for distancia, origen, destino in CONEXIONES_CASA:
        grafo.add_edge(distancia, origen, destino)

    return grafo


def camino_minimo(grafo: Graph, origen: str, destino: str):
    rutas = {}
    pendientes = grafo.dijkstra(origen)
    while pendientes.size() > 0:
        nodo, costo, anterior = pendientes.pop()
        rutas[nodo] = (costo, anterior)

    if destino not in rutas or rutas[destino][0] == inf:
        return None, []

    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        if actual == origen:
            break
        actual = rutas[actual][1]

    if camino[-1] != origen:
        return None, []

    camino.reverse()
    return rutas[destino][0], camino


def mostrar_barridos(grafo: Graph, origenes) -> None:
    for origen in origenes:
        print(f"\nDesde {origen}:")
        print("  Profundidad:")
        grafo.deep_show(origen)
        print("  Amplitud:")
        grafo.amplitude_show(origen)


def ejercicio_5() -> None:
    grafo = cargar_red()

    print("Ejercicio 5 - Red")

    print()
    print("a) Equipos cargados (nombre y tipo):")
    for vertice in grafo:
        print(f"  {vertice.value}: {vertice.other_values['tipo']}")

    print()
    print("b) Barridos en profundidad y amplitud desde las notebooks:")
    mostrar_barridos(grafo, ("Red Hat", "Debian", "Arch"))

    print()
    print("c) Camino más corto hasta la impresora:")
    for equipo in ("Manjaro", "Red Hat", "Fedora"):
        costo, camino = camino_minimo(grafo, equipo, "Impresora")
        print(f"  {equipo}: {' -> '.join(camino)} (costo {costo})")

    print()
    print("d) Árbol de expansión mínima:")
    arbol = grafo.kruskal("Router 1")
    peso_total = 0
    for conexion in arbol.split(";"):
        origen, destino, peso = conexion.rsplit("-", 2)
        print(f"  {origen} - {destino}: {peso}")
        peso_total += int(peso)
    print(f"  Peso total: {peso_total}")

    print()
    print("e) PC (no notebook) con el camino más corto al servidor Guaraní:")
    pcs = (
        vertice.value
        for vertice in grafo
        if vertice.other_values["tipo"] == "pc"
    )
    opciones = []
    for pc in pcs:
        costo, camino = camino_minimo(grafo, pc, "Guaraní")
        opciones.append((costo, pc, camino))
    costo, equipo, camino = min(opciones, key=lambda opcion: opcion[0])
    print(f"  {equipo}: {' -> '.join(camino)} (costo {costo})")

    print()
    print("f) Computadora del Switch 1 con el camino más corto a MongoDB:")
    posicion_switch = grafo.search("Switch 1", "value")
    equipos_switch = []
    for arista in grafo[posicion_switch].edges:
        posicion_equipo = grafo.search(arista.destination, "value")
        tipo = grafo[posicion_equipo].other_values["tipo"]
        if tipo in ("pc", "notebook"):
            equipos_switch.append(arista.destination)

    opciones = []
    for equipo in equipos_switch:
        costo, camino = camino_minimo(grafo, equipo, "MongoDB")
        opciones.append((costo, equipo, camino))
    costo, equipo, camino = min(opciones, key=lambda opcion: opcion[0])
    print(f"  {equipo}: {' -> '.join(camino)} (costo {costo})")

    print()
    print("g) Cambiar la impresora al Router 2 y repetir el punto b:")
    grafo.delete_edge("Switch 1", "Impresora")
    # Se conserva el peso de la conexión original porque la consigna no indica otro.
    grafo.add_edge(22, "Router 2", "Impresora")
    mostrar_barridos(grafo, ("Red Hat", "Debian", "Arch"))

# EJERCICIO 14

def ejercicio_14() -> None:
    grafo = cargar_casa()

    print()
    print("Ejercicio 14 - Ambientes de la casa")

    print()
    print("a) Vértices (ambientes):")
    print("  " + ", ".join(AMBIENTES))

    print()
    print("b) Aristas cargadas por ambiente:")
    for vertice in grafo:
        print(f"  {vertice.value}: {len(vertice.edges)}")

    print()
    print("c) Árbol de expansión mínima:")
    arbol = grafo.kruskal("cocina")
    peso_total = 0
    for conexion in arbol.split(";"):
        origen, destino, distancia = conexion.rsplit("-", 2)
        print(f"  {origen} - {destino}: {distancia} m")
        peso_total += int(distancia)
    print(f"  Cable total: {peso_total} m")

    print()
    print("d) Cable de red desde el router en habitación 1 hasta la Smart TV en sala de estar:")
    distancia, camino = camino_minimo(grafo, "habitación 1", "sala de estar")
    print(f"  {' -> '.join(camino)}: {distancia} m")


if __name__ == "__main__":
    ejercicio_5()
    ejercicio_14()
