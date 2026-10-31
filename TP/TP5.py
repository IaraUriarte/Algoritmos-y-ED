# EJERCICIO 5

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tree import BinaryTree
from super_heroes_data import superheroes
  
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
 
 
def main():
    ejercicio_5()
 
 
if __name__ == "__main__":
    main()