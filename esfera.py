from Figuras_Geometricas import Figuras_Geometricas
import math

class Esfera(Figuras_Geometricas):

    def __init__(self, radio: float, nombre="Esfera"):
        super().__init__(nombre)
        self._radio = radio

    # ---- PROPIEDADES ----
    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        self._radio = valor

    # ---- MÉTODO DEL ÁREA ----
    def area(self):
        return 4 * math.pi * (self.radio ** 2)
