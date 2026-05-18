# EJERCICIO 20

class stack:
    def __init__(self):
        self.__elements = []

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        return self.__elements.pop()
    
    def size(self):
        return len(self.__elements)
    
    def show(self):
        print(self.__elements)

def reg_mov():
    pila_mov = stack()
    print("Anotador de los pasos del robot")
    print("Opciones de dirección: norte, noreste, este, sureste, sur, suroeste, oeste, noroeste")
    print("Escriba 'fin' en la cantidad de pasos para terminar el registro.")

    while True:
        entrada_pasos = input("Cantidad de pasos ('fin' para terminar): ").strip().lower()
        if entrada_pasos == 'fin':
            break

        try:
            pasos = int(entrada_pasos)
        except(ValueError):
            print("Ingrese un número válido")
            continue

        direc = input("Dirección: ").strip().lower()
        direc_validas = ['norte', 'noreste', 'este', 'sureste', 'sur', 'suroeste', 'oeste', 'noroeste']

        if direc not in direc_validas:
            print(f"Dirección '{direc}' no válida. Intente de nuevo")
            continue

        pila_mov.push((pasos, direc))
        print(f"Movimiento registrado: {pasos} pasos hacia el {direc}.")

    return(pila_mov)
    
def retorno_robot(pila_mov):
    opuestas = {
        'norte': 'sur',
        'sur': 'norte',
        'este': 'oeste',
        'oeste': 'este',
        'noreste': 'suroeste',
        'suroeste': 'noreste',
        'noroeste': 'sureste',
        'sureste': 'noroeste'
    }

    print("Secuencia de retorno al punto de partida")
    if pila_mov.size() == 0:
        print("El robot no se movio, ya esta en el punto de partida")
        return
        
    while pila_mov.size() > 0:
        pasos, direc = pila_mov.pop()
        direc_opuesta = opuestas[direc]
        print(f"Mover {pasos} pasos hacie el {direc_opuesta}")

    print("El robot ha regresado al lugar de partida")


# BLOQUE PRINCIPAL
if __name__ == "__main__":
    movimientos = reg_mov()
    print("Pila de movimientos")
    movimientos.show()
    retorno_robot(movimientos)


# EJERCICIO 24
def analizar_mcu(pila_pers):
    pila_aux = Stack()
    pos_rocket = -1
    pos_groot = -1
    posicion_actual = 1
    mas_de_5 = []
    pelis_viuda_negra = 0
    empiezan_c_d_g = []

    while pila_pers.size() > 0:
        personaje = pila_pers.pop()
        nombre = personaje[0]
        pelis = personaje[1]

        # a)
        if nombre == "Rocket Raccoon":
            pos_rocket = posicion_actual
        elif nombre == "Groot":
            pos_groot = posicion_actual

        # b)
        if pelis > 5:
            mas_de_5.append((nombre, pelis))

        # c)
        if nombre in ["Black Widow", "Viuda Negra"]:
            pelis_viuda_negra = pelis

        # d)
        if nombre and nombre[0].upper() in ['C', 'D', 'G']:
            empiezan_c_d_g.append(nombre)

        pila_aux.push(personaje)
        posicion_actual += 1

    while pila_aux.size() > 0:
        pila_pers.push(pila_aux.pop())

    return {
        "pos_rocket": pos_rocket,
        "pos_groot": pos_groot,
        "mas_de_5": mas_de_5,
        "peliculas_viuda_negra": pelis_viuda_negra,
        "empiezan_c_d_g": empiezan_c_d_g
    }

