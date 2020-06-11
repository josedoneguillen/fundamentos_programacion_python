""" 
Script donde se solicite que se ingrese un valor 
y luego este sea impreso en consola.
Los valores a solicitar son: Los datos de una Persona 
(# de cedula, nombre, apellido, país de nacimiento, dirección etc...)
"""

# Imprimir bienvenida
print("Bienvenido al programa de solicitud de información")

# Declaracion de variables e inicializacion de valores por input
nombre = input("Ingrese su Nombre: \n")
apellido = input("Ingrese su Apellido: \n")
edad = int(input("Ingrese su Edad: \n"))
no_cedula = input("Ingrese su numero de Cédula: \n")
pais_nacimiento = input("Ingrese su País de Nacimiento \n")
direccion = input("Ingrese su Dirección: \n")


# Imprimir valores obtenidos
print(f"Su nombre es {nombre} {apellido} y tiene {edad} años.")
print(f"su numero de cedula es {no_cedula}")
print(f"su país de nacimiento es {pais_nacimiento}")
print(f"su dirección es {direccion}")