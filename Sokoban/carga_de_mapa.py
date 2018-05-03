mapa = []
metas = 0

def cargar_mapa():
        file = open('L_1.txt','r')
        for line in file:
            fila = []
            for columna in line [:-1]:
                fila.append(int(columna))
            mapa.append(fila)
    
def print_map():
    for fila in range(len(mapa)):
        line = ''
        for c in range (len(mapa[fila])):
            line += str(mapa[fila][c]) + ''
        print line

def contar_metas():
    print metas
    for fila in range(len(mapa)):
        for c in range (len(mapa[fila])):
            if mapa[fila][c] == 4:
                metas += 1
    


cargar_mapa()
print_map()
contar_metas()