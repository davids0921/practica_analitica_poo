from Figuras_Geometricas import Figuras_Geometricas

class Trapecio(Figuras_Geometricas):
    def __init__(self, base_mayor: float, base_menor: float, altura: float, nombre="Trapecio"):
        super().__init__(nombre)
        self._base_mayor = base_mayor
        self._base_menor = base_menor
        self._altura = altura

    @property
    def base_mayor(self):
        return self._base_mayor

    @base_mayor.setter
    def base_mayor(self, valor):
        self._base_mayor = valor

    @property
    def base_menor(self):
        return self._base_menor

    @base_menor.setter
    def base_menor(self, valor):
        self._base_menor = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = valor

    def area(self):
        return (self.base_mayor + self.base_menor) * self.altura / 2