# encoding: utf-8 
class Persona:
    def __init__(self, Nombre,Edad):
        self.Nombre = Nombre
        self.Edad = Edad
        print ' '
        print 'Hola soy ', self.Nombre,'tengo ', self.Edad, 'Añios'
        print ' '

    def saludar(self):
        print 'Hola soy', self.Nombre, 
    def despedirse(self):
        print 'Hasta luego',self.Nombre
    def platicar(self):
        print '¿Te gusta comer?'
    def confirmar(self):
        print 'Si'

Miguel = Persona ('Miguel',18)
Miguel.despedirse()
Miguel.confirmar()

Carlos = Persona ('Carlos',20)
Carlos.platicar()
