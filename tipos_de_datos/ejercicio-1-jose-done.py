'''
Ejercicio 1:
Escribe un script que solicite una palabra al usuario y que imprima en consola las 
2 primeras letras y las últimas 2 letras de esa palabra. 
En caso de tener 2 letras o menos, deberá imprimir: "Esta palabra es muy corta"
'''

# Declaracion de variable y solicitud de informacion al usuario
palabra = input("Ingrese una palabra:")

# Sentencia if para evaluar la cantidad de palabras
if (len(palabra) > 2):
    
    # Imprimir las primeras 2 palabras
    print("Las primeras 2 letras son: " + palabra[0] + palabra[1])
    
    # Imprimir las ultimas 2 palabras
    print("Las ultimas 2 letras son: " + palabra[-2] + palabra[-1])
    
else :
    
    # Imprimir texto si la palabra es muy corta
    print("Esta palabra es muy corta")
