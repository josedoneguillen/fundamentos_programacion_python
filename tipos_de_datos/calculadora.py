'''

Crea una calculadora donde solicites al usuario que indique la operación que desea realizar y 
que luego introduzca 2 números.La calculadora debe realizar las operaciones básicas 
(Suma, Resta, Multiplicación y División). Tener en cuenta que si el usuario introduce 
algo que no sea un número, el sistema debe indicar que no es un número y solicitarle 
al usuario que introduzca el número nuevamente. El sistema estará corriendo 
hasta que el usuario indique que desea salir

'''

# Variable para salir del bucle
salir = 0

while(salir == 0):

    print("Ingrese una operacion básicas: \n1- Suma \n2- Resta \n3- Multiplicación \n4-División")

    # Solicitar operacion al usuario
    operacion = int(input())

    # Solicitar num1
    num1 = input("Ingrese el primer numero:")

    # Solicitar num2
    num2 = input("Ingrese el segundo numero:")
    
    # Sentencia if para validar que el usuario ingreso numeros
    if num1.isdigit() and num2.isdigit() :
        
        # Convertir valores para poder operar
        num1 = int(num1)
        num2 = int(num2)

        # Sentencia if para determinar la operacion a realizar
        if operacion == 1 :
    
            # Sumar
            print(num1 + num2)
    
        elif operacion == 2 :
    
            # Restar
            print(num1 - num2)    
    
        elif operacion == 3 :
    
            # Multiplicar
            print(num1 * num2)
    
        elif operacion == 4 :
    
            # Dividir
            print(num1 / num2)
    
        else :
            # Imprimir si el usuario escoge una operacion invalida
            print("Operacion invalida")
            
    else:
        print("Uno de los valores ingresados no es un numerico.")
        
    # Preguntar al usuario si desea salir
    salir = int(input("presione 1 para salir y 0 para volver a calcular:"))