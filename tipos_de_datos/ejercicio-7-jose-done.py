'''
Ejercicio 7:
Escribe un script que solicite al usuario la llave 
y el valor y luego agrégalos a un diccionario. 
Al final, imprime el diccionario.
'''

# Declaracion de diccionario
diccionario = {}

#Solicitar llave para el diccionario
llave = input("Ingrese una llave:")

#Solicitar valor para el diccionario
valor = input("Ingrese una valor:")

# Asignar llave y valor al diccionario
diccionario[llave] = valor

# Imprimir diccionario
print(diccionario)
