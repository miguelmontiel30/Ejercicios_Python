class Transporte:
    
    color = ''
    velocidad = ''
    modelo = ''
    no_ruedas = ''

    def __init__(self):
        pass

    def avanzar (self):
        print 'Avanza a',self.velocidad,' Kph'

    def detenerse (self):
        print 'detenerse'

    def girar (self):
        print 'girar'

    def acelerar (self):
        return 'acelerar'

    def suma (self, n1, n2):
        return n1 + n2