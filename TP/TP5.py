# EJERCICIO 5

import sys
from pathlib import Path
 
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
 
import unicodedata
 
from tree import BinaryTree
from super_heroes_data import superheroes
from criatura import Criaturas, DESCRIPCIONES
  
def inorden(root):
    if root is not None:
        yield from inorden(root.left)
        yield root
        yield from inorden(root.right)
 
def inorden_inverso(root):
    if root is not None:
        yield from inorden_inverso(root.right)
        yield root
        yield from inorden_inverso(root.left)
 
def es_villano(nodo):
    return nodo.other_values['is_villain']
 
def borrar_nodo(arbol, nombre):
    nodo = arbol.search(nombre)
    pred = None
    if nodo is not None and nodo.left is not None and nodo.right is not None:
        pred = nodo.left
        while pred.right is not None:
            pred = pred.right
        pred_value, pred_other = pred.value, pred.other_values
 
    valor, otros = arbol.delete_node(nombre)
 
    if pred is not None:
        arbol.search(pred_value).other_values = pred_other
    return valor, otros
    
def ejercicio_5():
    print("Ejercicio 5: superheroes y villanos de MCU")
 
    # a) Cargar el árbol
    arbol = BinaryTree()
    for c in superheroes:
        arbol.insert_node(c['name'], other_value=c)
    print()
    print("a. Árbol cargado")
    print(f"Cantidad total de elementos: {len(superheroes)}")
 
    # b) Villanos ordenados alfabéticamente
    print()
    print("b. Villanos ordenados alfabéticamente")
    for nodo in inorden(arbol.root):
        if es_villano(nodo):
            print(" ", nodo.value)
 
    # c) Superhéroes que empiezan con C
    print()
    print("c. Superhéroes que empiezan con 'C'")
    for nodo in inorden(arbol.root):
        if not es_villano(nodo) and nodo.value.startswith('C'):
            print(" ", nodo.value)
 
    # d) Cantidad de superhéroes
    print()
    print("d. Cantidad de superhéroes")
    cant = sum(1 for n in inorden(arbol.root) if not es_villano(n))
    print(f"Cantidad de héroes: {cant}")
 
    # e) Búsqueda por proximidad de "strange" y corrección del nombre
    print()
    print("e. Búsqueda por proximidad y modificación")
    encontrados = [n.value for n in inorden(arbol.root)
                   if 'strange' in n.value.lower()]
    for nombre in encontrados:
        print(" Encontrado:", nombre)
 
    for nombre in encontrados:
        _, datos = borrar_nodo(arbol, nombre)
        datos['name'] = "Doctor Strange"
        arbol.insert_node("Doctor Strange", other_value=datos)
        print(f" '{nombre}' modificado a 'Doctor Strange'")
 
    # f) Superhéroes en orden descendente
    print()
    print("f. Superhéroes en orden descendente")
    for nodo in inorden_inverso(arbol.root):
        if not es_villano(nodo):
            print(" ", nodo.value)
 
    # g) Bosque: un árbol con los héroes y otro con los villanos
    arbol_heroes = BinaryTree()
    arbol_villanos = BinaryTree()
    for nodo in inorden(arbol.root):
        destino = arbol_villanos if es_villano(nodo) else arbol_heroes
        destino.insert_node(nodo.value, other_value=nodo.other_values)
 
    print()
    print("g. I Cantidad de nodos de cada árbol")
    print("Héroes:  ", sum(1 for _ in inorden(arbol_heroes.root)))
    print("Villanos:", sum(1 for _ in inorden(arbol_villanos.root)))
 
    print()
    print("g. II Barrido alfabético de Héroes")
    for nodo in inorden(arbol_heroes.root):
        print(" ", nodo.value)
 
    print()
    print("g. II Barrido alfabético de Villanos")
    for nodo in inorden(arbol_villanos.root):
        print(" ", nodo.value)

# EJERCICIO 23

def remove_accents(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
 
class Nombre(str):
    # Ordena sin tener en cuenta tildes ni mayúsculas
    # (sin esto "Átropos" y "Águila" quedarían al final del árbol)
    def __lt__(self, otro):
        return remove_accents(str(self)).lower() < remove_accents(str(otro)).lower()
 
    def __gt__(self, otro):
        return remove_accents(str(self)).lower() > remove_accents(str(otro)).lower()
 
def cargar_descripcion(arbol, nombre, texto):
    nodo = arbol.search(nombre)
    if nodo is None:
        return False
    nodo.other_values.description = texto
    return True
 
def imprimir_informacion_criatura(criatura):
    print(criatura.name)
    print(f"Derrotado por: {criatura.killer or '-'}")
    print(f"Capturada por: {criatura.captured or '-'}")
    print(f"Descripción: {criatura.description or '-'}")
 
def buscar_por_coincidencia(arbol, texto):
    t = remove_accents(texto).lower()
    return [n.other_values for n in inorden(arbol.root)
            if t in remove_accents(n.value).lower()]
 
def ejercicio_23():
    print()
    print("Ejercicio 23: criaturas de la mitología griega")
 
    # Generar el árbol con los datos de la tabla
    arbol = BinaryTree()
    for c in Criaturas:
        arbol.insert_node(Nombre(c.name), other_value=c)
 
    # a) Listado inorden de las criaturas y quiénes las derrotaron
    print()
    print("a. Listado inorden de criaturas y quién las derrotó")
    for nodo in inorden(arbol.root):
        c = nodo.other_values
        print(f"  {c.name} - Derrotado por {c.killer or '-'}")
 
    # b) Cargar una breve descripción sobre cada criatura
    print()
    print("b. Carga de descripciones")
    for nombre, texto in DESCRIPCIONES.items():
        cargar_descripcion(arbol, nombre, texto)
    print(f"Descripciones cargadas: {len(DESCRIPCIONES)}")
 
    # c) Toda la información de Talos
    print()
    print("c. Información de Talos")
    talos = arbol.search("Talos")
    if talos is not None:
        imprimir_informacion_criatura(talos.other_values)
 
    # d) Los 3 héroes o dioses que derrotaron más criaturas
    print()
    print("d. Top 3 de héroes/dioses con más criaturas derrotadas")
    conteo = {}
    for nodo in inorden(arbol.root):
        killer = nodo.other_values.killer
        if killer:
            conteo[killer] = conteo.get(killer, 0) + 1
    ranking = sorted(conteo.items(), key=lambda x: (-x[1], x[0]))
    top3 = ranking[:3]
    for pos, (heroe, cant) in enumerate(top3, 1):
        print(f"  {pos}. {heroe}: {cant} criatura(s)")
    empatados = [h for h, c in ranking[3:] if c == top3[-1][1]]
    if empatados:
        print("  También empatan en el puesto 3:", ", ".join(empatados))
 
    # e) Criaturas derrotadas por Heracles
    print()
    print("e. Criaturas derrotadas por Heracles")
    for nodo in inorden(arbol.root):
        if nodo.other_values.killer == "Heracles":
            print(" ", nodo.value)
 
    # f) Criaturas que no han sido derrotadas
    print()
    print("f. Criaturas no derrotadas")
    for nodo in inorden(arbol.root):
        if not nodo.other_values.killer:
            print(" ", nodo.value)
 
    # g) Cada nodo tiene el campo 'captured' (definido en la clase Criatura)
 
    # h) Heracles atrapó a Cerbero, Toro de Creta, Cierva de Cerinea
    #    y Jabalí de Erimanto
    print()
    print("h. Capturas de Heracles")
    for nombre in ["Cerbero", "Toro de Creta", "Cierva de Cerinea",
                   "Jabalí de Erimanto"]:
        nodo = arbol.search(nombre)
        if nodo is not None:
            nodo.other_values.captured = "Heracles"
            print(f"  {nombre} -> capturada por Heracles")
 
    # i) Búsquedas por coincidencia
    print()
    print("i. Búsqueda por coincidencia")
    for texto in ["dragon", "jabali"]:
        print(f"  Coincidencias con '{texto}':")
        for c in buscar_por_coincidencia(arbol, texto):
            print("   ", c.name)
 
    # j) Eliminar al Basilisco y a las Sirenas
    print()
    print("j. Eliminar Basilisco y Sirenas")
    for nombre in ["Basilisco", "Sirenas"]:
        valor, _ = borrar_nodo(arbol, nombre)
        if valor is not None:
            print(f"  '{valor}' eliminada")
 
    # k) Aves del Estínfalo: Heracles derrotó a varias
    print()
    print("k. Modificar Aves del Estínfalo")
    aves = arbol.search("Aves del Estínfalo")
    if aves is not None:
        aves.other_values.killer = "Heracles"
        aves.other_values.description += " Heracles derrotó a varias."
        imprimir_informacion_criatura(aves.other_values)
 
    # l) Cambiar el nombre de Ladón por Dragón Ladón
    print()
    print("l. Renombrar 'Ladón' a 'Dragón Ladón'")
    valor, criatura = borrar_nodo(arbol, "Ladón")
    if criatura is not None:
        criatura.name = "Dragón Ladón"
        arbol.insert_node(Nombre("Dragón Ladón"), other_value=criatura)
        print("  Ladón renombrado a Dragón Ladón")
 
    # m) Listado por nivel del árbol
    print()
    print("m. Listado por nivel")
    arbol.by_level()
 
    # n) Criaturas capturadas por Heracles
    print()
    print("n. Criaturas capturadas por Heracles")
    for nodo in inorden(arbol.root):
        if nodo.other_values.captured == "Heracles":
            print(" ", nodo.value)
 
def main():
    ejercicio_5()
    ejercicio_23()
 
 
if __name__ == "__main__":
    main()