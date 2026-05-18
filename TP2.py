# Ejercicio 20

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
        print("Opciones de dirección: Norte, Noreste, Este, Sureste, Sur, Suroeste, Oeste, Noroeste")
        print("Escriba 'fin' en la cantidad de pasos para terminar el registro.\n")

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
            direc_validas = ['Norte', 'Noreste', 'Este', 'Sureste', 'Sur', 'Suroeste', 'Oeste', 'Noroeste']

            if direc not in direc_validas:
                print(f"Dirección '{direc}' no válida. Intente de nuevo")
                continue

            pila_mov.push((pasos, direc))
            print(f"Movimiento registrado: {pasos} pasos hacia el {direc}.\n")

        return(pila_mov)