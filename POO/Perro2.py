class Perro:
    def __init__(self, Nombre, Raza, Edad):
        self.Nombre = Nombre
        self.Raza = Raza
        self.Edad = Edad
        print "Hola soy {1} y mi Raza es {2} tengo {3}". format(self. Nombre, Raza, Edad)
A = Perro ("Terry" ,"Pastor Aleman","10 anos")