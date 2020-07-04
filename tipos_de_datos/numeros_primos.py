'''

Crea un programa que solicite al usuario ingresar un número y le 
indique si el número ingresado es primo o no. El sistema debe mantenerse 
corriendo hasta que el usuario indique lo contrario. Cada vez que indique si es 
primo o no, debe preguntar al usuario si desea salir o ingresar otro número.

'''

# Variable para salir del bucle
salir = 0

# Ciclo while para ejecutar el bloque mientras el usuario lo desee
while(salir == 0):

    # Solicitar numero
    num = int(input("Ingrese un numero:"))
    
    # Declarar contador (Para saber cuantas veces es divisible)
    cont = 0
    
    # Ciclo for para iterar el numero y dividirlo
    for i in range(1 , num + 1):
        if (num % i) == 0:
            cont = cont + 1

    # Si el numero fue divisible 2 veces dentro del rango es primo
    if cont == 2:
        print("Es primo")
    else:
        print("No es primo")
        
    # Preguntar al usuario si desea salir
    salir = int(input("presione 1 para salir y 0 para volver a calcular:"))
    