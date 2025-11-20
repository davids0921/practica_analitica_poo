class Figuras_Geometricas:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError("este metodo debe calcular el area por sub clase")
