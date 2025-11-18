from Figuras_Geometricas import Figuras_Geometricas

# Clase triangulo que hereda de Figuras_Geometricas
class triangulo(Figuras_Geometricas):

    # Constructor que recibe la base y altura
    def __init__(self, base, altura):
        self.base = base       # Guarda la base
        self.altura = altura   # Guarda la altura

    # Método que calcula el área del triángulo
    def area(self):
        return (self.base * self.altura) / 2
