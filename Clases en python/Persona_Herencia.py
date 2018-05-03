class Persona:
    
    def __init__(self,nombre):
        self.nombre = nombre
    
    def saludar (self):               #Esto se va a heredar a la clase ingeniero
        print 'Hola soy', self.nombre

class Ingeniero (Persona):            #En esta parte estamos haciendo referencia a la clase anterior
    
    def __init__(self,nombre,lenguaje):
        self.nombre = nombre
        self.lenguaje = lenguaje
    
    def programador (self):
        print 'Programo en ', self.lenguaje

Miguel = Persona('Miguel')
Luis = Ingeniero('Luis', 'Python') 

Miguel.saludar()
Luis.saludar()
Luis.programador()


