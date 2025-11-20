# Importamos las clases de cada archivo
from Figuras_Geometricas import Figuras_Geometricas
from triangulo import triangulo
from circulo import circulo
from cuadrado import cuadrado
from rectangulo import rectangulo
from cilindro import cilindro
from paralelograma import paralelograma
from trapecio import Trapecio
while True:
 print("------ MENÚ -------------")
 print("1. Triangulo")
 print("2. Circulo")
 print("3. Cuadrado")
 print("4. Rectangulo")
 print("5. Cilindro")
 print("6. Paralelogramo")
 print("7. trapecio")
 print("8. salir del programa")

 opcion = input("Que figura desea usar (1-4): ")
 print("Usted seleccionó la opción:",opcion)

 if opcion == "1":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        figura = Triangulo(base, altura)
        print("El area del triangulo es :", figura.area())
    

 elif opcion == "2":
        radio = float(input("Ingrese el radio del círculo: "))
        figura = Circulo(radio) 
        print("El area del circulo es :", figura.area())

 elif opcion == "3":
        lado = float(input("Ingrese el lado del cuadrado: "))
        figura = Cuadrado(lado)
        print("El area del triangulo es :", figura.area())
 
 elif opcion == "4":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        figura = Rectangulo(base, altura)
        print("El area del triangulo es :", figura.area())

 elif opcion == "5":
        radio = float(input("Ingrese el radio del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))
        figura = Cilindro(radio, altura)
        print("El área total del cilindro es:", figura.area())
 
 elif opcion == "6":
         base = float(input("Ingrese la base del paralelogramo: "))
         altura = float(input("Ingrese la altura del paralelogramo: "))
         figura = Paralelogramo(base, altura)
         print("El área del paralelogramo es:", figura.area())

 elif opcion == "7":
        b_mayor = float(input("Ingrese la base mayor del trapecio: "))
        b_menor = float(input("Ingrese la base menor del trapecio: "))
        altura = float(input("Ingrese la altura del trapecio: "))
        figura = Trapecio(b_mayor, b_menor, altura)     
        print("El área del trapecio es:", figura.area())    
    


 elif opcion == "8":
      print("Salio del progrma")

 else:
    print("Opción no válida. Por favor, seleccione un número del 1 al 8.")