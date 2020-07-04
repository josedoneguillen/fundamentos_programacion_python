'''

Ejercicio 3:

Escribe un script que solicite al usuario ingresar 1 palabra hasta completar una lista con 5 items. 
Luego imprimir la lista excluyendo el 3er y 5to elemento.

'''
# Declaracion de lista vacias
palabras = []

# Explicar al usuario que se le pedira una palabra 5 veces
print("Debera ingresar 5 palabras")

# Declaracion de bucle for hasta 5
for i in range(5):
    
  #Solicitar al usuario palabras
  palabra = input("Ingrese una palabra para la lista:")
  
  # Insertar palabra en la lista
  palabras.append(palabra)

# Declaracion de bucle for para palabras
for k, v in enumerate(palabras):
  ''' 
  Sentencia if para excluir 3er y 5to elemento 
  (Intente usar or en el if pero no queria funcionar no se por que)
  Ej:
  if (k != 2 or k != 4):
  '''

  if(k != 2):
      
        if(k != 4):
            
            # Imprimir palabra
            print((k+1), v)
    
