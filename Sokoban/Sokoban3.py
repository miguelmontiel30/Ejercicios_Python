python -m pip install readchart
class Sokoban:
    #variables globales
    mapa = [[2,2,2,2,2],
           [2,1,1,1,2],
           [2,0,3,1,2],
           [2,1,2,4,2],
           [2,2,2,2,2]]
    mapa1 = [0,0,0,0,0]
    posicion_columna = 1
    posicion_fila = 2
    jalar = False
    
    def __init__(self):
        print '\n**** SOKOBAN ****\n'
    
    def cargar_mapa(self):
        file = open('L_2.txt','r')
        for line in file:
            fila = []
            for columna in line [:-1]:
                fila.append(fila)
    
    def print_map(self):
        for row in range(len(self.mapa)):
            for c in range (len(self.mapa)):
                self.mapa[row][c])
            print self.mapa

    def imprimir_mapa(self):
        for f in range (5):
            for c in range (5):
                self.mapa1[c] = self.mapa[f][c]
            print self.mapa1

    def mover_derecha(self):
        if self.mapa[self.posicion_fila][self.posicion_columna -1] == 3 and self.mapa[self.posicion_fila][self.posicion_columna +1] == 1 and self.jalar == True:
             self.posicion_columna += 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna -1] = 3
             self.mapa[self.posicion_fila][self.posicion_columna -2] = 1
       
        elif self.mapa[self.posicion_fila][self.posicion_columna -1] == 5 and self.mapa[self.posicion_fila][self.posicion_columna +1] == 1 and self.jalar == True:
             self.posicion_columna += 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna -1] = 3
             self.mapa[self.posicion_fila][self.posicion_columna -2] = 4

        elif self.mapa[self.posicion_fila][self.posicion_columna +1] == 1:
             self.posicion_columna += 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna -1] = 1
        
        elif self.mapa[self.posicion_fila][self.posicion_columna +1] == 3 and self.mapa[self.posicion_fila][self.posicion_columna +2] == 1:
             self.posicion_columna += 1
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna -1] = 1
             self.mapa[self.posicion_fila][self.posicion_columna +1] = 3 

        elif self.mapa[self.posicion_fila][self.posicion_columna +1] == 3 and self.mapa[self.posicion_fila][self.posicion_columna +2] == 4:
             self.posicion_columna += 1
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna -1] = 1
             self.mapa[self.posicion_fila][self.posicion_columna +1] = 5 
    
    def mover_izquierda(self):    
        if self.mapa[self.posicion_fila][self.posicion_columna +1] == 3 and self.mapa[self.posicion_fila][self.posicion_columna -1] == 1 and self.jalar == True:
             self.posicion_columna -= 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna +1] = 3
             self.mapa[self.posicion_fila][self.posicion_columna +2] = 1
        
        elif self.mapa[self.posicion_fila][self.posicion_columna +1] == 5 and self.mapa[self.posicion_fila][self.posicion_columna -1] == 1 and self.jalar == True:
             self.posicion_columna -= 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna +1] = 3
             self.mapa[self.posicion_fila][self.posicion_columna +2] = 4
        
        elif self.mapa[self.posicion_fila][self.posicion_columna -1] == 1:
             self.posicion_columna -= 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna +1] = 1
        
        elif self.mapa[self.posicion_fila][self.posicion_columna -1] == 3 and self.mapa[self.posicion_fila][self.posicion_columna -2] == 1:
             self.posicion_columna -= 1
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna +1] = 1
             self.mapa[self.posicion_fila][self.posicion_columna -1] = 3

        elif self.mapa[self.posicion_fila][self.posicion_columna -1] == 3 and self.mapa[self.posicion_fila][self.posicion_columna -2] == 4:
             self.posicion_columna -= 1
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna +1] = 1
             self.mapa[self.posicion_fila][self.posicion_columna -1] = 5            
    
    def mover_arriba(self):
        if self.mapa[self.posicion_fila +1][self.posicion_columna] == 3 and self.mapa[self.posicion_fila -1][self.posicion_columna] == 1 and self.jalar == True:
            self.posicion_fila -= 1 
            self.mapa[self.posicion_fila][self.posicion_columna] = 0
            self.mapa[self.posicion_fila +1][self.posicion_columna] = 3
            self.mapa[self.posicion_fila +2][self.posicion_columna] = 1
       
        elif self.mapa[self.posicion_fila +1][self.posicion_columna] == 5 and self.mapa[self.posicion_fila -1][self.posicion_columna] == 1 and self.jalar == True:
            self.posicion_fila -= 1 
            self.mapa[self.posicion_fila][self.posicion_columna] = 0
            self.mapa[self.posicion_fila +1][self.posicion_columna] = 3
            self.mapa[self.posicion_fila +2][self.posicion_columna] = 4

        elif self.mapa[self.posicion_fila -1][self.posicion_columna] == 1:
             self.posicion_fila -= 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila +1][self.posicion_columna] = 1
        
        elif self.mapa[self.posicion_fila -1][self.posicion_columna] == 3 and self.mapa[self.posicion_fila -2][self.posicion_columna] == 1:
             self.posicion_fila -= 1
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila -1][self.posicion_columna] = 3
             self.mapa[self.posicion_fila +1][self.posicion_columna] = 1 

        elif self.mapa[self.posicion_fila -1][self.posicion_columna] == 3 and self.mapa[self.posicion_fila -2][self.posicion_columna] == 4:
             self.posicion_fila -= 1
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila -1][self.posicion_columna] = 5
             self.mapa[self.posicion_fila +1][self.posicion_columna] = 1

    def mover_abajo(self):
        if self.mapa[self.posicion_fila -1][self.posicion_columna] == 3 and self.mapa[self.posicion_fila +1][self.posicion_columna] == 1 and self.jalar == True:
             self.posicion_fila += 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila -1][self.posicion_columna] = 3
             self.mapa[self.posicion_fila -2][self.posicion_columna] = 1
       
        elif self.mapa[self.posicion_fila -1][self.posicion_columna] == 5 and self.mapa[self.posicion_fila +1][self.posicion_columna] == 1 and self.jalar == True:
             self.posicion_fila += 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila -1][self.posicion_columna] = 3
             self.mapa[self.posicion_fila -2][self.posicion_columna] = 4

        elif self.mapa[self.posicion_fila +1][self.posicion_columna] == 1:
            self.posicion_fila += 1 
            self.mapa[self.posicion_fila][self.posicion_columna] = 0
            self.mapa[self.posicion_fila -1][self.posicion_columna] = 1
        
        elif self.mapa[self.posicion_fila +1][self.posicion_columna] == 3 and self.mapa[self.posicion_fila +2][self.posicion_columna] == 1:
            self.posicion_fila += 1
            self.mapa[self.posicion_fila][self.posicion_columna] = 0
            self.mapa[self.posicion_fila +1][self.posicion_columna] = 3
            self.mapa[self.posicion_fila -1][self.posicion_columna] = 1 

        elif self.mapa[self.posicion_fila +1][self.posicion_columna] == 3 and self.mapa[self.posicion_fila +2][self.posicion_columna] == 4:
            self.posicion_fila += 1
            self.mapa[self.posicion_fila][self.posicion_columna] = 0
            self.mapa[self.posicion_fila +1][self.posicion_columna] = 5
            self.mapa[self.posicion_fila -1][self.posicion_columna] = 1 


     


objeto = Sokoban()
objeto.cargar_mapa()
objeto.print_map()
print len(self.mapa)

while True:
    objeto.imprimir_mapa()
    movimiento = raw_input('\nElige direccion W,A,S,D: ')
    if movimiento == 'd' or movimiento == 'D':
        objeto.mover_derecha()
    elif movimiento == 'a' or movimiento == 'A':
        objeto.mover_izquierda()
    elif movimiento == 'w' or movimiento == 'W':
        objeto.mover_arriba()
    elif movimiento == 's' or movimiento == 'S':
        objeto.mover_abajo()
    elif movimiento == 'l':
        objeto.jalar = True
    elif movimiento == 'k':
        objeto.jalar = False