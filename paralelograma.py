from Figuras_Geometricas import Figuras_Geometricas

class paralelograma(Figuras_Geometricas):

    def __init__(self, base: float, altura: float):
        self._base = base
        self._altura = altura

    
    @property
    def base(self) -> float:
        return self._base
    
    @base.setter
    def base(self, valor: float):
        self._base = valor

    
    @property
    def altura(self) -> float:
        return self._altura
    
    @altura.setter
    def altura(self, valor: float):
        self._altura = valor


    def area(self) -> float:
        return self._base * self._altura