from Figuras_Geometricas import Figuras_Geometricas

# Clase cuadrado que hereda de Figuras_Geometricas
class cuadrado(Figuras_Geometricas):

    # Constructor que recibe el lado del cuadrado
    def __init__(self, lado):
        self.lado = lado

    # Método para calcular el área del cuadrado
    def area(self):
        return self.lado * self.lado
