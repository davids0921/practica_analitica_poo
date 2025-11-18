from Figuras_Geometricas import Figuras_Geometricas

# Clase rectangulo que hereda de Figuras_Geometricas
class rectangulo(Figuras_Geometricas):

    # Constructor que recibe base y altura
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Método para calcular el área del rectángulo
    def area(self):
        return self.base * self.altura
