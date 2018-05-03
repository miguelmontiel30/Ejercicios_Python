mapa = [[2,2,2,2,2],
        [2,1,1,1,2],
        [2,0,3,1,2],
        [2,1,2,4,2],
        [2,2,2,2,2]]
mapa1 = [0,0,0,0,0]
posicion_columna = 1
posicion_fila = 2

def imprimir_mapa():
    for f in range (5):
        for c in range (5):
            mapa1[c] = mapa[f][c]
        print mapa1  

while True:
    metas = mapa.count(4)
    print metas
    print
    imprimir_mapa()
    opcion = raw_input('\nTeclea direccion W,A,S,D: ')
    
    if opcion == 'd' or opcion == 'D':
        if mapa[posicion_fila][posicion_columna +1] == 1:
            posicion_columna += 1 
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila][posicion_columna -1] = 1
        
        elif mapa[posicion_fila][posicion_columna +1] == 3 and mapa[posicion_fila][posicion_columna +2] == 1:
            posicion_columna += 1
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila][posicion_columna -1] = 1
            mapa[posicion_fila][posicion_columna +1] = 3 

        elif mapa[posicion_fila][posicion_columna +1] == 3 and mapa[posicion_fila][posicion_columna +2] == 4:
            posicion_columna += 1
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila][posicion_columna -1] = 1
            mapa[posicion_fila][posicion_columna +1] = 5 
    
    if opcion == 'a' or opcion == 'A':
        if mapa[posicion_fila][posicion_columna -1] == 1:
            posicion_columna -= 1 
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila][posicion_columna +1] = 1
        
        elif mapa[posicion_fila][posicion_columna -1] == 3 and mapa[posicion_fila][posicion_columna -2] == 1:
            posicion_columna -= 1
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila][posicion_columna +1] = 1
            mapa[posicion_fila][posicion_columna -1] = 5

        elif mapa[posicion_fila][posicion_columna -1] == 3 and mapa[posicion_fila][posicion_columna -2] == 4:
            posicion_columna -= 1
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila][posicion_columna +1] = 1
            mapa[posicion_fila][posicion_columna -1] = 3

    if opcion == 'w' or opcion == 'W':
        if mapa[posicion_fila -1][posicion_columna] == 1:
            posicion_fila -= 1 
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila +1][posicion_columna] = 1
        
        elif mapa[posicion_fila -1][posicion_columna] == 3 and mapa[posicion_fila -2][posicion_columna] == 1:
            posicion_fila -= 1
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila -1][posicion_columna] = 3
            mapa[posicion_fila +1][posicion_columna] = 1 

        elif mapa[posicion_fila -1][posicion_columna] == 3 and mapa[posicion_fila -2][posicion_columna] == 4:
            posicion_fila -= 1
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila -1][posicion_columna] = 5
            mapa[posicion_fila +1][posicion_columna] = 1 

    if opcion == 's' or opcion == 'S':
        if mapa[posicion_fila +1][posicion_columna] == 1:
            posicion_fila += 1 
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila -1][posicion_columna] = 1
        
        elif mapa[posicion_fila +1][posicion_columna] == 3 and mapa[posicion_fila +2][posicion_columna] == 1:
            posicion_fila += 1
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila +1][posicion_columna] = 3
            mapa[posicion_fila -1][posicion_columna] = 1 

        elif mapa[posicion_fila +1][posicion_columna] == 3 and mapa[posicion_fila +2][posicion_columna] == 4:
            posicion_fila += 1
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila +1][posicion_columna] = 5
            mapa[posicion_fila -1][posicion_columna] = 1 

    elif opcion != 'd' or opcion != 'a' or opcion != 's' or opcion != 'w':
        print '\nHa eleido una opcion incorrecta, Vuelva a intentarlo\n'

    jalar = False

    if opcion == 'l':
        jalar = True

    elif opcion == 's':
        jalar = False 

    if mapa[posicion_fila +1][posicion_columna] == 3 and mapa[posicion_fila +2][posicion_columna] == 4:
            posicion_fila += 1
            mapa[posicion_fila][posicion_columna] = 0
            mapa[posicion_fila +1][posicion_columna] = 5
            mapa[posicion_fila -1][posicion_columna] = 1 

    