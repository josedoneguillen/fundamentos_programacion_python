# Crear un sistema de biblioteca utilizando los conceptos aprendidos en el curso.

# Inicializacion clase biblioteca
class Biblioteca():

    def __init__(self):
        self.catalogo = [
            {
                "libro": "Sistemas Operativos Modernos", 
                "autor": "Andrew S. Tanenbaum", 
                "copias": 10
            },
            {
                "libro": "Python Crash Course", 
                "autor": "Eric M.", 
                "copias": 1
            },
            {
                "libro": "Learn Python: the hard way", 
                "autor": "Zed A. Shaw", 
                "copias": 1
            }
        ]

        self.menu()

    # Funcion para imprimir el menu
    def menu(self):

        
        salir = False

        while (salir == False):

            self.menu_principal()
            opcion = input("Seleccione una opción")

            if (opcion == 1):

                self.menu_catalogo()

            elif (opcion == 3):
                
                break    
            
            print("Desea cerrar el programa:")
            print("1- Sí")
            print("2- No")

            salir = input("Seleccione una opción")

            if (salir == 1):
                salir = True
            else:
                salir = False    

    # Funcion para imprimir menu principal
    def menu_principal(self):

        print("Bienvenidos a la Librería ITLA:")
        print("1- Catalogo")
        print("2- Clientes")
        print("3- Salir")


    # Funcion para imprimir menu catálogo
    def menu_catalogo(self):

        print("Bienvenidos a la Librería ITLA:")
        print("1- Catálogo")
        print("2- Clientes")
        print("3- Salir")


# instanciar la clase biblioteca
b = Biblioteca()