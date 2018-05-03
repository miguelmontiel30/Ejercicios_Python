class Sokoban:
    #variables globales
    mapa = []
    posicion_columna = 0
    posicion_fila = 0
    jalar = False
    nivel = 1
    metas = 0
    def __init__(self):
        print '\n**** SOKOBAN ****\n'

    def Next_level(self):
        print "\n***** Excelente Nivel superado ****\n"
        self.nivel += 1
        self.iniciar_juego()

    def iniciar_juego(self):
        self.cargar_mapa()
        self.encontrar_posicion()
        self.contar_metas()
    
    def cargar_mapa(self):
        file = open(str(self.nivel)+('.txt'),'r')
        for line in file:
            fila = []
            for columna in line [:-1]:
                fila.append(int(columna))
            self.mapa.append(fila)
        
    def print_map(self):
        for fila in range(len(self.mapa)):
            line = ' '
            for c in range (len(self.mapa[fila])):
                line += str(self.mapa[fila][c]) + ' '
            print line   
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
             self.metas +=1

        elif self.mapa[self.posicion_fila][self.posicion_columna +1] == 1:
             self.posicion_columna += 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna -1] = 1
        
        elif self.mapa[self.posicion_fila][self.posicion_columna +1] == 4:
             self.posicion_columna += 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna -1] = 4
        
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
             self.metas -= 1
    
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
             self.metas += 1
        
        elif self.mapa[self.posicion_fila][self.posicion_columna -1] == 1:
             self.posicion_columna -= 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna +1] = 1
        
        elif self.mapa[self.posicion_fila][self.posicion_columna -1] == 3 and self.mapa[self.posicion_fila][self.posicion_columna -2] == 1:
             self.posicion_columna -= 1
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna +1] = 1
             self.mapa[self.posicion_fila][self.posicion_columna -1] = 3
        
        elif self.mapa[self.posicion_fila][self.posicion_columna -1] == 4:
             self.posicion_columna -= 1 
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna +1] = 4

        elif self.mapa[self.posicion_fila][self.posicion_columna -1] == 3 and self.mapa[self.posicion_fila][self.posicion_columna -2] == 4:
             self.posicion_columna -= 1
             self.mapa[self.posicion_fila][self.posicion_columna] = 0
             self.mapa[self.posicion_fila][self.posicion_columna +1] = 1
             self.mapa[self.posicion_fila][self.posicion_columna -1] = 5
             self.metas -= 1            
    
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
            self.metas +=1

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
             self.metas -= 1

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
             self.metas += 1

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
            self.metas -= 1
   
    def encontrar_posicion(self):
        for fila in range(len(self.mapa)):
            for c in range (len(self.mapa[fila])):
                if self.mapa[fila][c] == 0:
                    self.posicion_columna = c
                    self.posicion_fila = fila
    def contar_metas(self):
        for fila in range(len(self.mapa)):
            for c in range (len(self.mapa[fila])):
                if self.mapa[fila][c] == 4:
                    self.metas += 1
                    


objeto = Sokoban()
objeto.iniciar_juego()
while True:
    if objeto.metas == 0:
        objeto.Next_level()
    objeto.print_map()
    print '\nElige direccion W,A,S,D: ' 
    movimiento = readchar.readchar()
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

os.system('cls')
print " "
print " "

