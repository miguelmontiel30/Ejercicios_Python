class Lagartija:
    def __init__(self,Color,Tamano,Cola):
        self.Color = Color
        self.Tamano = Tamano
        self.Cola = Cola
        print 'Lagartija de color',self.Color, 'Con tamano',self.Tamano,'Su cola es',self.Cola
    
    def caminar(self):
        print 'Estoy caminando '
    
    def lagartijas(self):
        print 'Casual en el GYM' 
    
    def hablar(self):
        print 'ola k ase xdxd'

    def saludar(self,nombre):
        print 'Hola {0}'.format(nombre)
    
    def despedirse(self,nombre):
        print 'Adios {0}'.format(nombre)

Rango = Lagartija('Roja', 'Larga', 'corta')
Rango.lagartijas()
Rango.saludar('Miguel')
Rango.despedirse('Vaquero')

Pedro = Lagartija('Verde','Chica','Larga')
Pedro.hablar()