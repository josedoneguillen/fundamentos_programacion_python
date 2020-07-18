class Persona:

    __abstracto = "abstracto"

    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def hablar(self):
        print("Hola, mi nombre es " + self.nombre + " y tengo " + str(self.edad) + " " + self.__abstracto)

    def caminar(self, metros):
        print("Estoy caminando " + str(metros) + " Metros")


p = Persona("Jose", 28, 130)

p.hablar()
p.caminar(100)