class Criatura:

    def __init__(self, name, killer=None, description="", captured=None):
        self.name = name
        self.killer = killer          # quién la derrotó (None = nadie)
        self.description = description
        self.captured = captured      # quién la capturó (None = nadie)

    def __str__(self):
        return (f"{self.name} | Derrotado por: {self.killer or '-'} | "
                f"Capturada por: {self.captured or '-'} | "
                f"Descripción: {self.description or '-'}")


# (criatura, derrotado por)  -- tabla de la consigna
_DATOS = [
    ("Ceto", None), ("Tifón", "Zeus"), ("Equidna", "Argos Panoptes"),
    ("Dino", None), ("Pefredo", None), ("Enio", None), ("Escila", None),
    ("Caribdis", None), ("Euríale", None), ("Esteno", None),
    ("Medusa", "Perseo"), ("Ladón", "Heracles"), ("Águila del Cáucaso", None),
    ("Quimera", "Belerofonte"), ("Hidra de Lerna", "Heracles"),
    ("León de Nemea", "Heracles"), ("Esfinge", "Edipo"),
    ("Dragón de la Cólquida", None), ("Cerbero", None),
    ("Cerda de Cromión", "Teseo"), ("Ortro", "Heracles"),
    ("Toro de Creta", "Teseo"), ("Jabalí de Calidón", "Atalanta"),
    ("Carcinos", None), ("Gerión", "Heracles"), ("Cloto", None),
    ("Láquesis", None), ("Átropos", None), ("Minotauro de Creta", "Teseo"),
    ("Harpías", None), ("Argos Panoptes", "Hermes"),
    ("Aves del Estínfalo", None), ("Talos", "Medea"), ("Sirenas", None),
    ("Pitón", "Apolo"), ("Cierva de Cerinea", None), ("Basilisco", None),
    ("Jabalí de Erimanto", None),
]

Criaturas = [Criatura(nombre, killer) for nombre, killer in _DATOS]


# Descripciones breves (inciso b). Se cargan en el árbol desde tp5.py
DESCRIPCIONES = {
    "Ceto": "Diosa marina, madre de muchos monstruos del mar.",
    "Tifón": "Gigante monstruoso con cien cabezas de dragón, padre de monstruos.",
    "Equidna": "Mitad mujer, mitad serpiente; madre de monstruos.",
    "Dino": "Una de las Greas, ancianas que compartían un ojo y un diente.",
    "Pefredo": "Una de las Greas, hermana de Dino y Enio.",
    "Enio": "Una de las Greas, hermana de Dino y Pefredo.",
    "Escila": "Monstruo marino de seis cabezas que acechaba un estrecho.",
    "Caribdis": "Remolino monstruoso que tragaba los barcos.",
    "Euríale": "Gorgona inmortal, hermana de Medusa.",
    "Esteno": "Gorgona inmortal, hermana de Medusa.",
    "Medusa": "Gorgona con serpientes por cabello; petrificaba con la mirada.",
    "Ladón": "Dragón que custodiaba las manzanas de oro de las Hespérides.",
    "Águila del Cáucaso": "Águila que devoraba el hígado de Prometeo.",
    "Quimera": "Monstruo con cabeza de león, cuerpo de cabra y cola de serpiente.",
    "Hidra de Lerna": "Serpiente acuática de varias cabezas que se regeneraban.",
    "León de Nemea": "León de piel invulnerable que aterrorizaba Nemea.",
    "Esfinge": "Monstruo alado que planteaba un enigma a los viajeros.",
    "Dragón de la Cólquida": "Dragón que custodiaba el vellocino de oro.",
    "Cerbero": "Perro de tres cabezas, guardián de las puertas del Hades.",
    "Cerda de Cromión": "Cerda salvaje que asolaba la región de Cromión.",
    "Ortro": "Perro de dos cabezas que cuidaba el ganado de Gerión.",
    "Toro de Creta": "Toro feroz que asolaba la isla de Creta.",
    "Jabalí de Calidón": "Jabalí enviado por Artemisa para castigar Calidón.",
    "Carcinos": "Cangrejo gigante que ayudó a la Hidra contra Heracles.",
    "Gerión": "Gigante de tres cuerpos, dueño de un rebaño de ganado rojo.",
    "Cloto": "Moira que hilaba el hilo de la vida.",
    "Láquesis": "Moira que medía y asignaba el hilo de la vida.",
    "Átropos": "Moira que cortaba el hilo de la vida.",
    "Minotauro de Creta": "Mitad hombre, mitad toro, encerrado en el laberinto.",
    "Harpías": "Criaturas aladas con rostro de mujer que robaban comida.",
    "Argos Panoptes": "Gigante de cien ojos que vigilaba sin dormir del todo.",
    "Aves del Estínfalo": "Aves de plumas y picos de bronce que atacaban a las personas.",
    "Talos": "Gigante de bronce que protegía la isla de Creta.",
    "Sirenas": "Seres mitad mujer, mitad ave, cuyo canto atraía a los marineros.",
    "Pitón": "Serpiente que custodiaba el oráculo de Delfos.",
    "Cierva de Cerinea": "Cierva de cuernos de oro consagrada a Artemisa.",
    "Basilisco": "Serpiente cuya mirada y aliento resultaban mortales.",
    "Jabalí de Erimanto": "Jabalí gigante que asolaba el monte Erimanto.",
}
