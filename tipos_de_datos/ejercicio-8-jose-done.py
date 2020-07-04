'''
Ejercicio 8:
Escribe un script que agregue una lista a una llave de un diccionario y luego imprímelo.
'''
# Declarar diccionario
diccionario = {
    "nombre": "Jose",
    "apellido": "Doñe",
    "edad": 27
}

# Agregar lista al diccionario
diccionario["lenguajes"] = ["PHP","SQL","JavaScript","C#", "Python"]

# Imprimir diccionario
print(diccionario)
