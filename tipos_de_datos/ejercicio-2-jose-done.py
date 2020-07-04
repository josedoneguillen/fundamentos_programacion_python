'''

Ejercicio 2:

Escribe un script que solicite al usuario ingresar un texto, 
luego le indique cuantos caracteres tiene ese texto y luego le solicite al usuario que ingrese una palabra 
para buscarla en el texto e indique si fue encontrada o no.

'''

# Declaracion de variable texto y solicitud de informacion al usuario
texto = input("Ingrese un texto:")

# Imprimir cantidad de caracteres que tiene el texto
print("El texto tien una longitud de " + str(len(texto)) + " caracteres")

# Declaracion de variable palabra y solicitud de informacion al usuario
palabra = input("Ingrese una palabra para buscarla en el texto:")

# Sentencia if para validar existencia de la palabra en el texto
if ( texto.find(palabra) != -1):
    
    # Imprimir si la palabra fue encontrada
    print("La palabra fue encontrada!")

else:
    
    # Imprimir si la palabra no fue encontrada
    print("La palabra no fue encontrada ='(")

