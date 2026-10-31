# EJERCICIO 5

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