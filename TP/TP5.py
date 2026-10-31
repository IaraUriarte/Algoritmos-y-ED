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