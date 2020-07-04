'''
Ejercicio 6:
Escribe un script que imprima el indice de una letra dentro de una tupla.
'''

# Declaracion de tupla
tupla = (1, 2, 3, 'a', 5)

# Recorrer tupla con un ciclo for
for k, v in enumerate(tupla) :
    
    # Sentencia if para comparar el tipo de dato
    if type(v) == str :
        
        # Imprimir si el tipo de dato encontrado es string
        print('El indice de la letra (' + str(v) + ') es: ' + str(k) )
