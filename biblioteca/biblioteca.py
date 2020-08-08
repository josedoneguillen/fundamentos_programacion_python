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
                "duracion": 100,
                "copias": 12
            },
            {
                "nombre": "Python Crash Course (Audio)", 
                "autor": "Eric M.", 
                "formato": "mp4",
                "duracion": 360,
                "copias": 12
            },
            {
                "nombre": "Learn Python: the hard way (Audio)", 
                "autor": "Zed A. Shaw",
                "formato": "mp4", 
                "duracion": 120,
                "copias": 12
            }
        ]

        self.clientes = [
            {
                "nombre": "José",
                "apellido": "Doñe",
                "libros": []
            }
        ]

        self.menu()

    # Funcion para imprimir el menu
    def menu(self):

        
        salir = False

        while (salir == False):

            self.menu_principal()

            print("Desea cerrar el programa:")
            print("1- Sí")
            print("2- No")

            salir = int(input("Seleccione una opción: "))

            if (salir == 1):
                salir = True
            else:
                salir = False    

    # Funcion para imprimir menu principal
    def menu_principal(self):

        print("Bienvenidos a la Librería ITLA:")
        print("1- Catalogo")
        print("2- Clientes")
        print("3- Prestar")
        print("4- Salir")

        opcion = int(input("Seleccione una opción: "))

        if (opcion == 1):

            self.menu_catalogo()

        elif (opcion == 2):

            self.menu_clientes()

        elif (opcion == 3):

            self.prestar()          

        elif (opcion == 4):

            exit()


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

        elif (opcion == 3):

            print("Libros:")
            self.mostrar_libros()

            print("Audio libros:")
            self.mostrar_audio_libros()   

        elif (opcion == 4):

            self.agregar_libro()

        elif (opcion == 5):

            self.agregar_audio_libro()                   

        elif (opcion == 6):

            self.menu_principal()

        elif (opcion == 7):

            exit()

    # Funcion para imprimir menu clientes
    def menu_clientes(self):

        print("Clientes, Biblioteca ITLA:")     
        print("1- Agregar nuevo Cliente")
        print("2- Ver Clientes")
        print("3- Buscar Cliente")
        print("4- Volver al menu principal")
        print("5- Salir")

        opcion = int(input("Seleccione una opción: "))

        if (opcion == 1):

            self.agregar_cliente()

        elif (opcion == 2):

            self.ver_clientes()

        elif (opcion == 3):
            
            self.buscar_cliente()                

        elif (opcion == 4):

            self.menu_principal()

        elif (opcion == 5):

            exit()            

    # Funcion para imprimir libros
    def mostrar_libros(self):

        for libro in self.libros:

            print(libro)
        
        self.volver()

    # Funcion para imprimir audio libros
    def mostrar_audio_libros(self):

        for audio_libro in self.audio_libros:

            print(audio_libro)
        
        self.volver()

    # Funcion para imprimir clientes
    def ver_clientes(self):

        for cliente in self.clientes:

            print(cliente)
        
        self.volver()


    #  Funcion para agregar libro
    def agregar_libro(self):

        nombre = input('Ingrese el nombre del libro: ')
        autor = input('Ingrese el nombre del autor libro: ')   
        copias = int(input('Ingrese las copias disponibles del libro: '))

        self.libros.append({"nombre": nombre, "autor": autor, "copias": copias})

        self.mostrar_libros();


    #  Funcion para agregar libro
    def agregar_audio_libro(self):

        nombre = input('Ingrese el nombre del libro: ')
        autor = input('Ingrese el nombre del autor libro: ')
        formato = input('Ingrese el formato del audio: ')      
        duracion = int(input('Ingrese la duración del audio: '))
        copias = int(input('Ingrese las copias disponibles del libro: '))

        self.audio_libros.append({"nombre": nombre, "autor": autor, "formato": formato, "duracion": duracion, "copias": copias})

        self.mostrar_audio_libros();

    #  Funcion para agregar cliente
    def agregar_cliente(self):

        nombre = input('Ingrese el nombre del cliente: ')
        apellido = input('Ingrese el apellido del cliente: ')

        self.clientes.append({"nombre": nombre, "apellido": apellido, "libros": []})

        self.ver_clientes();

    # Funcion para buscar clientes
    def buscar_cliente(self):

        nombre = input("Ingrese el nombre del cliente: ")

        for cliente in self.clientes:

            if (cliente['nombre'] == nombre):
                print(cliente)
        
        self.volver()

    # Funcion para prestar libros
    def prestar(self):

        print("Desea solicitar: ")
        print("1- Libro")
        print("2- Audio libro")

        tipo = int(input("Seleccione una opción: "))
        n_libro = 0
        i = 0

        if (tipo == 1):

            i = 1

            for libro in self.libros:

                print(str(i) + "- " + libro['nombre'])
                i += 1

            n_libro = int(input("Seleccione una opción: "))    

            if(self.libros[n_libro-1]['copias'] > 0):

                c = 1 

                for cliente in self.clientes:

                    print(str(c) + "- " + cliente['nombre'] + " " + cliente['apellido'])
                    c += 1

                n_cliente = int(input('Seleccione un cliente: '))

                self.clientes[n_cliente-1]['libros'].append({"nombre": self.libros[n_libro-1]['nombre'], "tipo": tipo, "posicion": n_libro-1})

                self.libros[n_libro-1]['copias'] -= 1


            else:
                print('No hay suficientes copias de este libro')            

        elif (tipo == 2):

            i = 1

            for audio_libro in self.audio_libros:
                
                print(str(i) + "- " + audio_libro['nombre'])
                i += 1

            n_libro = int(input("Seleccione una opción: "))    

            if(self.audio_libros[n_libro-1]['copias'] > 0):

                c = 1 

                for cliente in self.clientes:

                    print(str(c) + "- " + cliente['nombre'] + " " + cliente['apellido'])
                    c += 1

                n_cliente = int(input('Seleccione un cliente: '))

                self.clientes[n_cliente-1]['libros'].append({"nombre": self.audio_libros[n_libro-1]['nombre'], "tipo": tipo, "posicion": n_libro-1})

                self.audio_libros[n_libro-1]['copias'] -= 1


            else:
                print('No hay suficientes copias de este libro')  
        
        self.volver()        

    # Funcion para volver
    def volver(self):

        print("Desea volver al menu principal: ")
        print("1- Sí")
        print("2- No")

        volver = int(input("Seleccione una opción: "))

        if (volver == 1):

            self.menu_principal()

        else:

            exit()

# instanciar la clase biblioteca
b = Biblioteca()