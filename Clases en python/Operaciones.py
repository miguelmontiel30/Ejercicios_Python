class Operaciones:
    def __init(self):
        pass

    def suma (self,n1,n2):
        return n1+n2

    def resta (self,n1,n2):
        return n1-n2

    def multiplicacion (self,n1,n2):
        return n1*n2

    def division (self,n1,n2):
        return n1/n2

    def residuo (self,n1,n2):
        return n1%n2

class Perimetros:
    def __init(self):
        pass

    def cuadrado (self,l1):
        return l1+l1+l1+l1

    def rectangulo (self,l1,l2):
        return l1+l1+l2+l2

    def circulo (self,d):
        return 3.14*d

    def trapecio (self,l,B,b):
        return B+b+l+l
   
    def triangulo (self,l1):
        return l1+l1+l1

class Areas:
    def __init(self):
        pass

    def cuadrado (self,l1):
        return l1*l1

    def rectangulo (self,l1,l2):
        return l1*l2

    def circulo (self,r):
        return 3.14*(r*r)

    def trapecio (self,h,B,b):
        return B+b/2*h
   
    def triangulo (self,b,h):
        return b*h/2
