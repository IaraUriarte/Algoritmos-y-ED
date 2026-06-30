# EJERCICIO 1: Busqueda y listado de superhéroes.

from list_ import List

nombres_superH = [
    "HombreAraña", "Ironman", "CapitanAmerica", 
    "Thor", "Hulk", "PanteraNegra", "DoctorExtraño", 
    "HombreHormiga", "DuendeVerde", "Deadpool", "Venom", 
    "LinternaVerde", "MaquinaDeGuerra", "Shazam", "FlechaVerde"
]

def busqueda_superheroe(nombres_superH, CapitanAmerica :str, i=0):
    if i == len(nombres_superH):
        return -1
    if nombres_superH[i] == CapitanAmerica:
        return i
    return busqueda_superheroe(nombres_superH, CapitanAmerica, i + 1)

def listar_superheroes(nombres_superH, i=0):
    if i == len(nombres_superH):
        return
    print(f"{i}:{nombres_superH[i]}")
    listar_superheroes(nombres_superH, i + 1)

# BLOQUE PRINCIPAL:

buscado = "CapitanAmerica"

print()
posicion = busqueda_superheroe(nombres_superH, buscado)
if posicion != -1:
    print(f"{buscado} se encuentra en la posicion {posicion}")
else:
    print(f"{buscado} no se encuentra en la lista.")

print()
print("Listado de Superhéroes:")
listar_superheroes(nombres_superH)
print()


# EJERCICIO 2

from super_heroes_data import superheroes
from collections import deque
from list_ import List

class Personaje:
    def __init__(self, data):
        self.nom = data["name"]
        self.alias = data["alias"]
        self.nom_real = data["real_name"] or "Desconocido" 
        self.bio = data["short_bio"]
        self.aparicion = data["first_appearance"]
        self.villano = data["is_villain"]

    def __str__(self):
        tipo = "Villano" if self.villano else "Héroe"
        return f"{self.nom} ({self.nom_real})\n{tipo}\n{self.aparicion}"

lista = List()
for h in superheroes:
    lista.append(Personaje(h))

# BLOQUE PRINCIPAL:

# 1. 
print("1. Ordenado por nombre de manera ascendente")
lista.sort(key=lambda x: x.nom)
for p in lista:
    print(p.nom)

# 2.
print("_" * 20)
print()
print("2. Posición")
for nombre in ["The Thing", "Rocket Raccoon"]:
    pos = lista.search(nombre)
    if pos != -1:
        print(f'"{nombre}" está en la posición {pos}')
    else:
        print(f'"{nombre}" no encontrado')

# 3. 
print("_" * 20)
print()
print("3. Villanos")
for p in lista:
    if p.villano:
        print(p.nom)

# 4. 
print("_" * 20)
print()
print("4. Villanos antes de 1980")
cola = deque(p for p in lista if p.villano)
while cola:
    v = cola.popleft()
    if v.aparicion < 1980:
        print(f"{v.nom}. {v.aparicion}")

# 5. 
print("_" * 20)
print()
print("5. Bl/G/My/W")
prefijos = ("Bl", "G", "My", "W")
for p in lista:
    if p.nom.startswith(prefijos):
        print(p)

# 6. 
print("_" * 20)
print()
print("6. Ordenado por nombre real de manera ascendente")
lista.sort(key=lambda x: x.nom_real)
lista.show()

# 7. 
print("_" * 20)
print()
print("7. Ordenado por aparición")
lista.sort(key=lambda x: x.aparicion)
lista.show()

# 8.
print("_" * 20)
print()
print("8. Modificar Ant Man")
for p in lista:
    if p.nom == "Ant Man":
        p.nom_real = "Scott Lang"
        print(f"Actualizado: {p}")
        break

# 9. 
print("_" * 20)
print()
print("9. Palabras clave: time-traveling/suit")
for p in lista:
    if "time-traveling" in p.bio.lower() or "suit" in p.bio.lower():
        print(f" {p.nom}: {p.bio}")

# 10. 
print("_" * 20)
print()
print(" 10. Eliminar Electro y Baron Zemo")
for nombre in ["Electro", "Baron Zemo"]:
    encontrado = False
    for p in lista:
        if p.nom == nombre:
            print(f"Eliminado: {p}")
            lista.remove(p)
            encontrado = True
            break
    if not encontrado:
        print(f'"{nombre}" no estaba en la lista')