class Areas:
    radio = 0
    lado = 0
    def __init__(self, pi):
        self.pi=pi
    
    def circulo(self):
        area = self.pi * (self.radio*self.radio)
        print area

    def cuadrado(self):
        area = self.lado*self.lado
        print area

calculos = Areas(3.1416)
calculos.radio = 2
calculos.circulo()

area = Areas(2)
area.lado = 2 
area.cuadrado()
