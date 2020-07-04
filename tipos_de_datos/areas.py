'''

Crea un programa que te permita calcular el Área de un cuadrado, un triángulo y 
un círculo. El usuario debe elegir la figura que desea buscar el área e ingresar
los valores necesarios para poder calcularla. El programa debe permitir al 
usuario seguir calcular las distintas áreas y cerrar el programa cuando lo desee.

'''
import math


# Variable para salir del bucle
salir = 0

while(salir == 0):

    print("Ingrese una figura básicas: \n1- Cuadrado \n2- Triángulo \n3- Círculo")

    # Solicitar figura al usuario
    figura = int(input())

    # Sentencia if para determinar la figura seleccionada
    if figura == 1 :
    
        # Cuadrado
        a = int(input("Ingrese el área del cuadrado: "))
        
        # Imprimir el area del cuadrado
        print("El área del cuadrado es: " + str( a ** 2 ))
    
    elif figura == 2 :
    
        # Triángulo
        b = int(input("Ingrese la base del Triángulo: "))
        a = int(input("Ingrese la altura del Triángulo: "))
        
        # Imprimir area del triangulo
        print("El área del triángulo es: " + str( ((b * a) / 2 ) ))
    
    elif figura == 3 :
    
        # Circulo
         # Triángulo
        d = int(input("Ingrese el diametro del Circulo: "))
        
        # Imprimir area del triangulo
        print("El área del circulo es: " + str( (math.pi * ( (d ** 2) / 4 )) ))
    
        
    else :
        # Imprimir si el usuario escoge una figura invalida
        print("Figura invalida")
        
    # Preguntar al usuario si desea salir
    salir = int(input("presione 1 para salir y 0 para volver a calcular:"))