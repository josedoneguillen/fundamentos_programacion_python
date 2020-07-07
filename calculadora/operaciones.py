def suma(lista):
    # Declaracion variable suma
    suma = 0

    # Ciclo for para recorrer los valores ingresados
    for num in lista:

        # Sumar los valores en cada iteracion
        suma += num

    # Retornar suma
    return suma

def resta(lista):

    # Retornar la operacion
    return lista[0]-lista[1]

def multiplicacion(lista):

    # Retornar la operacion
    return lista[0]*lista[1]

def division(lista):

   # Retornar la operacion
    return lista[0]/lista[1]

def potenciacion(lista):
    
    # Retornar la operacion
    return lista[0]**lista[0]

def raiz(lista):

    # Retornar la operacion
    return lista[0]**(1/2.0)

def area(lista):

    # Variable de respuesta
    respuesta = "Figura no definida"
    
    # Contar lados para saber que tipo de area es
    cant = int(len(lista))

    # IF Para operar
    if (cant == 2):

        # Diametro
        d = (lista[0] + lista[1]) / 2

        # Caluclar circulo
        respuesta = "El área del circulo es: " + str( (3.1416 * ( (d ** 2) / 4 )) )

    elif (cant == 3):
        
        # Altura 
        a = (lista[0] + lista[1]) / 2

        # Base
        b = lista[2]

        # Calcular triangulo
        respuesta = "El área del triángulo es: " + str( ((b * a) / 2 ) )

    elif (cant == 4):   

        # Area 
        a = (lista[0] + lista[1] + lista[2] + lista[3]) / 4

        # Calcular cuadrado
        respuesta = "El área del cuadrado es: " + str( a ** 2 )

    return respuesta
