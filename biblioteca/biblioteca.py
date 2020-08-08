# Crear un sistema de biblioteca utilizando los conceptos aprendidos en el curso.

# Inicializacion clase biblioteca
class Biblioteca():

    def __init__(self):
        self.libros = [
            {
                "nombre": "Sistemas Operativos Modernos", 
                "autor": "Andrew S. Tanenbaum", 
                "copias": 10
            },
            {
                "nombre": "Python Crash Course", 
                "autor": "Eric M.", 
                "copias": 1
            },
            {
                "nombre": "Learn Python: the hard way", 
                "autor": "Zed A. Shaw", 
                "copias": 1
            }
        ]

        self.audio_libros = [
            {
                "nombre": "Sistemas Operativos Modernos (Audio)", 
                "autor": "Andrew S. Tanenbaum",
                "formato": "mp4", 
                "duracion": 100
            },
            {
                "nombre": "Python Crash Course (Audio)", 
                "autor": "Eric M.", 
                "formato": "mp4",
                "duracion": 360
            },
            {
                "nombre": "Learn Python: the hard way (Audio)", 
                "autor": "Zed A. Shaw",
                "formato": "mp4", 
                "duracion": 120
            }
        ]

        self.menu()

    # Funcion para imprimir el menu
    def menu(self):

        
        salir = False

        while (salir == False):

            if(self.menu_principal()):
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

        opcion = int(input("Seleccione una opción: "))

        if (opcion == 1):

            self.menu_catalogo()

        elif (opcion == 3):

            return True


    # Funcion para imprimir menu catálogo
    def menu_catalogo(self):

        print("Catalogo de los Libros y Audiolibros, Biblioteca ITLA:")     
        print("1- Mostrar Libros")
        print("2- Mostrar Audiolibros")
        print("3- Mostrar catalogo completo")
        print("4- Agregar Libro")
        print("5- Agregar Audiolibro")
        print("6- Volver al menu principal")
        print("7- Salir")

        opcion = int(input("Seleccione una opción: "))

        if (opcion == 1):

            self.mostrar_libros()

        elif (opcion == 2):

            self.mostrar_audio_libros()    

        elif (opcion == 6):

            self.menu_catalogo()

        elif (opcion == 7):

            exit()    

    # Funcion para imprimir libros
    def mostrar_libros(self):

        for libro in self.libros:

            print(libro)

 # Funcion para imprimir audio libros
    def mostrar_audio_libros(self):

        for audio_libro in self.audio_libros:

            print(audio_libro)

# instanciar la clase biblioteca
b = Biblioteca()