# EJERCICIO 10

class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        if self.size() > 0:
            return self.__elements.pop()
        return None

    def size(self):
        return len(self.__elements)

    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]
        return None

    def show(self):
        print(self.__elements)

class Cola:
    def __init__(self):
        self.__elements = []

    def arribo(self, value):
        self.__elements.append(value)

    def atencion(self):
        if self.size() > 0:
            return self.__elements.pop(0)
        return None

    def size(self):
        return len(self.__elements)

    def on_front(self):
        if self.size() > 0:
            return self.__elements[0]
        return None

    def show(self):
        print(self.__elements)

# # a) 
# def eliminar_facebook(cola):
#     tamanio = cola.size()
#     for _ in range(tamanio):
#         notif = cola.atencion()
#         if notif["App"].lower() != "facebook":
#             cola.arribo(notif)

# # b) 
# def mostrar_twitter_python(cola):
#     tamanio = cola.size()
#     for _ in range(tamanio):
#         notif = cola.atencion()
#         if notif["App"].lower() == "twitter" and "python" in notif["Mensaje"].lower():
#             print(f"Notificación de Twitter: [{notif['Hora']}] {notif['Mensaje']}")
#         cola.arribo(notif)

# # c) 
# def notificaciones_rango_horario(cola):
#     pila_temp = Stack()
#     tamanio = cola.size()

#     for _ in range(tamanio):
#         notif = cola.atencion()
#         if "11:43" <= notif["Hora"] <= "15:57":
#             pila_temp.push(notif)
#         cola.arribo(notif)

#     cantidad = pila_temp.size()
#     return cantidad, pila_temp

# # BLOQUE PRINCIPAL
# if __name__ == "__main__":
#     cola_notificaciones = Cola()
    
#     notificaciones_iniciales = [
#         {"Hora": "08:30", "App": "facebook", "Mensaje": "Susana Gomez te envió una solicitud de amistad"},
#         {"Hora": "11:45", "App": "twitter", "Mensaje": "Nuevo curso de Python para principiantes disponible ya"},
#         {"Hora": "12:15", "App": "whatsapp", "Mensaje": "Mamá: ¿venís a comer hoy?"},
#         {"Hora": "13:00", "App": "facebook", "Mensaje": "A Maria Gomez le gustó tu foto de perfil"},
#         {"Hora": "14:20", "App": "twitter", "Mensaje": "Debatiendo sobre las ventajas de usar Python en la nube"},
#         {"Hora": "15:30", "App": "instagram", "Mensaje": "lucia_g te empezó a seguir"},
#         {"Hora": "15:57", "App": "twitter", "Mensaje": "Python es el mejor lenguaje para aprender a programar"},
#         {"Hora": "16:05", "App": "twitter", "Mensaje": "Un tweet sobre desarrollo web sin palabras clave"},
#         {"Hora": "18:00", "App": "facebook", "Mensaje": "Recordatorio: Hoy es el cumpleaños de Pedro Martinez"}
#     ]

#     for n in notificaciones_iniciales:
#         cola_notificaciones.arribo(n)

#     print("Cola inicial")
#     tamanio = cola_notificaciones.size()
#     for _ in range(tamanio):
#         notif = cola_notificaciones.atencion()
#         print(f"[{notif['Hora']}] {notif['App']}: {notif['Mensaje']}")
#         cola_notificaciones.arribo(notif)
#     print()

#     # b)
#     print("Notificaciones de twitter con la palabra python")
#     mostrar_twitter_python(cola_notificaciones)
#     print()

#     # c) 
#     print("Notificaciones entre las 11:43 y las 15:57 (Guardadas en Pila)")
#     cant, pila = notificaciones_rango_horario(cola_notificaciones)
#     print(f"Cantidad encontrada: {cant}")
#     print("Contenido de la pila (desapilando):")
#     while pila.size() > 0:
#         notif = pila.pop()
#         print(f"[{notif['Hora']}] {notif['App']}: {notif['Mensaje']}")
#     print()

#     # a)
#     print("Eliminando notificaciones de facebook")
#     eliminar_facebook(cola_notificaciones)
#     print()

#     print("Cola final")
#     tamanio = cola_notificaciones.size()
#     for _ in range(tamanio):
#         notif = cola_notificaciones.atencion()
#         print(f"[{notif['Hora']}] {notif['App']}: {notif['Mensaje']}")
#         cola_notificaciones.arribo(notif)


# EJERCICIO 22

# a)
def personaje_capitana_marvel(cola):
    tamanio = cola.size()
    nombre = None
    for _ in range(tamanio):
        p = cola.atencion()
        if p["superheroe"].lower() == "capitana marvel":
            nombre = p["personaje"]
        cola.arribo(p)
    return nombre

# b)
def mostrar_superheroes_femeninos(cola):
    tamanio = cola.size()
    for _ in range(tamanio):
        p = cola.atencion()
        if p["genero"].upper() == "F":
            print(f"- {p['superheroe']}")
        cola.arribo(p)

# c)
def mostrar_personajes_masculinos(cola):
    tamanio = cola.size()
    for _ in range(tamanio):
        p = cola.atencion()
        if p["genero"].upper() == "M":
            print(f"- {p['personaje']}")
        cola.arribo(p)

# d)
def superheroe_scott_lang(cola):
    tamanio = cola.size()
    nombre_superheroe = None
    for _ in range(tamanio):
        p = cola.atencion()
        if p["personaje"].lower() == "scott lang":
            nombre_superheroe = p["superheroe"]
        cola.arribo(p)
    return nombre_superheroe

# e)
def mostrar_datos_letra_s(cola):
    tamanio = cola.size()
    for _ in range(tamanio):
        p = cola.atencion()
        if p["personaje"].lower().startswith("s") or p["superheroe"].lower().startswith("s"):
            print(f"- Personaje: {p['personaje']}, Héroe: {p['superheroe']}, Género: {p['genero']}")
        cola.arribo(p)

# f)
def buscar_carol_danvers(cola):
    tamanio = cola.size()
    encontrado = False
    superheroe = None
    for _ in range(tamanio):
        p = cola.atencion()
        if p["personaje"].lower() == "carol danvers":
            encontrado = True
            superheroe = p["superheroe"]
        cola.arribo(p)
    return encontrado, superheroe


# BLOQUE PRINCIPAL
if __name__ == "__main__":
    print()
    
    cola_mcu = Cola()
    personajes = [
        {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
        {"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
        {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
        {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
        {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
        {"personaje": "Sam Wilson", "superheroe": "Falcon", "genero": "M"},
        {"personaje": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"},
        {"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"}
    ]
    
    for p in personajes:
        cola_mcu.arribo(p)
        
    # a)
    print()
    print("Personaje de Capitana Marvel:")
    print(personaje_capitana_marvel(cola_mcu))
    
    # b)
    print()
    print("Superhéroes femeninos:")
    mostrar_superheroes_femeninos(cola_mcu)
    
    # c)
    print()
    print("Personajes masculinos:")
    mostrar_personajes_masculinos(cola_mcu)
    
    # d)
    print()
    print("Superhéroe de Scott Lang:")
    print(superheroe_scott_lang(cola_mcu))
    
    # e)
    print()
    print("Personajes o superhéroes que empiezan con 'S':")
    mostrar_datos_letra_s(cola_mcu)
    
    # f)
    print()
    print("¿Se encuentra Carol Danvers en la cola?")
    encontrado, heroe = buscar_carol_danvers(cola_mcu)
    if encontrado:
        print(f"Sí, su nombre de superhéroe es: {heroe}")
    else:
        print("No se encuentra en la cola.")
