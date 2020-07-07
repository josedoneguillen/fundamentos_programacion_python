'''
Crea una calculadora donde solicites al usuario que indique la operación que desea realizar y 
que luego introduzca 2 números.La calculadora debe realizar las operaciones básicas 
(Suma, Resta, Multiplicación y División). Tener en cuenta que si el usuario introduce 
algo que no sea un número, el sistema debe indicar que no es un número y solicitarle 
al usuario que introduzca el número nuevamente. El sistema estará corriendo 
hasta que el usuario indique que desea salir

Para este ejercicio, van a utilizar la calculadora que realizaron la semana pasa y le aplicaran las siguientes modificaciones:

    La solicitudes de ingreso de operación, etc. va a estar en un módulo separado.
    Deben crear un paquete nuevo, que tengas distintos módulos para calcular operaciones más avanzadas 
    (nota: no deben utilizar a Math.). Estas operaciones avanzadas son: potenciación, raíz cuadrada.
    En el paquete de operaciones avanzadas, incluir cálculos para áreas de circulo, rectángulo y cuadrado.

Tener en cuenta reglas de PEP8 y al mismo tiempo, dividir adecuadamente su proyecto.

Nota: Es un plus que su calculadora identifique de forma automática cuando sea un cuadrado o un rectángulo.

'''

# Importar paquete de operaciones
import operaciones

# Variable para salir del bucle
salir = 0

# Funcion de solicitud de datos
def numeros(cant):

    #Definir lista con la cantidad de valores
    lista = []

    # Definit contador para el ciclo
    i = 0

    # Ciclo while
    while (i < int(cant)):

        # Es numerico
        not_num = True

        # Declarar variable numero
        numero = input("Ingrese un numero: ")

         # Ciclo while para pedir lados mientras no sea numerico
        while(not_num):

            # Si es numerico
            if (numero.isdigit()):

                # Solicitar y almacenar numeros en la lista
                lista.append(float(numero))

                # Definir a verdadero para romper el ciclo
                not_num = False

                # Incrementar contador
                i += 1

            else:
                # Imprimir mensaje en caso de no ser numerico
                print("El dato ingresado no es numerico.")    

    # Retornar la lista
    return lista

# Ciclo while para operar mientras el usuario lo desee
while(salir == 0):

    # Imprimir menu de opciones
    print("Ingrese una operacion básicas:") 
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicación") 
    print("4- División")
    print("5- Potenciación")
    print("6- Raíz cuadrada")
    print("7- Área")

    # Solicitar operacion al usuario
    operacion = int(input())

    # Sentencia if para determinar la operacion a realizar
    if operacion == 1 :
    
        # Sumar
        print(operaciones.suma(numeros(2)))
    
    elif operacion == 2 :
    
        # Restar
        print(operaciones.resta(numeros(2)))   
    
    elif operacion == 3 :
    
        # Multiplicar
        print(operaciones.multiplicacion(numeros(2)))
    
    elif operacion == 4 :
    
        # Dividir
        print(operaciones.division(numeros(2)))

    elif operacion == 5 :
    
        # Potenciación
        print(operaciones.potenciacion(numeros(1)))

    elif operacion == 6 :

        # Raiz Cuadrada
        print(operaciones.raiz(numeros(1)))  

    elif operacion == 7 :

        # Es numerico
        not_num = True

        # Ciclo while para pedir lados mientras no sea numerico
        while(not_num):

            # Preguntar al usuario cuantos lados tiene el area que desea calcular
            lados = input("Ingrese la cantidad de lados:")
            
            # Si es numerico
            if (lados.isdigit()):

                # Convertir a entero
                lados = int(lados);

                # Definir a verdadero para romper el ciclo
                not_num = False

            else:
                # Imprimir mensaje en caso de no ser numerico
                print("El dato ingresado no es numerico.")    

        # Area
        print(operaciones.area(numeros(lados)))       
    
    else :
        # Imprimir si el usuario escoge una operacion invalida
        print("Operacion invalida")

    # Preguntar al usuario si desea salir
    salir = int(input("presione 1 para salir y 0 para volver a calcular:"))