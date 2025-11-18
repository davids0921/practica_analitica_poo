# Importamos las clases de cada archivo
from Figuras_Geometricas import Figuras_Geometricas
from triangulo import triangulo
from cuadrado import cuadrado
from rectangulo import rectangulo
from circulo import circulo

# Bucle infinito para mostrar el menú hasta que el usuario decida salir
while True:
    # Mostramos el menú principal
    print("------- FIGURAS GEOMETRICAS AREAS -------")
    print("1. AREA DEL Triangulo")
    print("2. AREA DEL Cuadrado")
    print("3. AREA DEL Rectangulo")
    print("4. AREA DEL Circulo")
    print("5. CERRAR EL PROGRAMA")

    # Solicitamos la opción al usuario como cadena (string)
    opcion = input("SELECIONE UNA OPCION DE LAS 5: ").strip()

    if opcion == "1":
        # Solicitamos base y altura del triángulo
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))

        # Creamos un objeto de la clase triangulo
        tr = triangulo(base, altura)

        # Llamamos al método area() y mostramos el resultado
        print("El area del triangulo es:", tr.area())

    elif opcion == "2":
        # Pedimos el lado del cuadrado
        lado = float(input("Ingrese el lado del cuadrado: "))

        # Creamos un objeto de la clase cuadrado
        cd = cuadrado(lado)

        # Mostramos el área calculada
        print("El area del cuadrado es:", cd.area())

