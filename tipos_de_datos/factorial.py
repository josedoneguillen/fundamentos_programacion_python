'''

Crea un programa que te permita imprimir el factorial de un número ingresado 
por el usuario. El programa debe permitir al usuario calcular tantos numero 
como desee y sólo salir cuando el usuario indique que desea salir.

'''
# Definir funcion para calcular el factorial
def fact(n):
  if n>0:
    n = n * fact(n - 1)
  else:
    n = 1
  return int(n)


# Variable para salir del bucle
salir = 0

# Ciclo while para ejecutar el bloque mientras el usuario lo desee
while(salir == 0):

    # Solicitar numero
    num = int(input("Ingrese un numero:"))
    
    # Imprimir el factorial del numero
    print("El factorial de " + str(num)  + " es " + str(fact(num)))
        
    # Preguntar al usuario si desea salir
    salir = int(input("presione 1 para salir y 0 para volver a calcular:"))
    