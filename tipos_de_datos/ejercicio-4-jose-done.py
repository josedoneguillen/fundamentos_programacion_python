'''
Ejercicio 4:
Escribe un script que imprima una lista y luego que la reimprima sin valores repetidos.
'''

# Declaracion de lista
lista = [
    "Jose", 
    "Manuel", 
    "Jose", 
    "Manuel", 
    "Doñe", 
    "Guillen", 
    "Doñe", 
    "Guillen"]
    
'''
Convirtiendo la lista a diccionario y luego a lista eliminamos
los duplicados ya que se remplazan al ser reinsertados a la lista
'''
lista = list(dict.fromkeys(lista))

# Imprimir lista sin duplicados
print(lista)
