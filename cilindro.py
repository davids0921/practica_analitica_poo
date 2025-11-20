from Figuras_Geometricas import Figuras_Geometricas

class cilindro(Figuras_Geometricas):
 
    def _init_(self,nombre):
     super()._init_(nombre)


    @property
    def radio(self) -> float:
         return self._radio
    
    @radio.setter
    def radio(self,radio:float):
        self._radio=radio

    @property
    def altura(self)-> float:
        return self._altura
    
    @altura.setter
    def altura(self,altura:float):
      self.altura=altura

    def area(self):
       pi=3.1416
       return 2*pi*self.radio*(self.radio*self.altura)
