import math
from Figuras_Geometricas import Figuras_Geometricas

# Clase circulo que hereda de Figuras_Geometricas
class circulo(Figuras_Geometricas):

    # Constructor que recibe el radio
    def __init__(self, radio):
        self.radio = radio

    # Método que calcula el área del círculo usando PI
    def area(self):
        return math.pi * (self.radio ** 2)
