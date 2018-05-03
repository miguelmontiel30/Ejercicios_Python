class Matriz:    

    #Variables Globales:
    longitud = 0
    matriz = []
    fila = 0
    columna = 0


    def __init__(self):
        print "***** Matriz ***** \n"

    def menu(self):
        print "************************************************"
        print "*            *****  Menu  *****                *"
        print "* 1.- Crear Matriz                             *"
        print "* 2.- Calcular tamanio de la matriz            *"
        print "* 3.- Ultimo numero de matriz                  *"
        print "* 4.- Comprobar llenado de matriz              *"        
        print "* 5.- Insertar datos en matriz                 *"
        print "* 6.- Buscar dato                              *"
        print "* 7.- Eliminar dato                            *"
        print "* 8.- Actualizar dato                          *"
        print "************************************************"

    def crear_matriz(self):
        self.matriz = []
        self.fila = 0
        self.columna = 0                 
        print '\n***** Tamanio del arreglo *****\n'
        self.fila = input ('Filas: ')
        self.columna = input ('\nColumnas:')                 
        for i in range (self.fila):            
            self.matriz.append([0] * self.columna) 
        print self.matriz, " \n" 
            
    
    def calcular_tamanio(self):
        self.longitud = 0
        print "\nEl tamanio de la matriz es de: ",  len(self.matriz), " X ", len(self.matriz)
        for i in range (self.fila):
            for j in range (self.columna):
                self.longitud += 1
        print "\nLa longitud de la matriz es de: ", self.longitud

    def ultimo_numero(self):        
        print "\nEl ultimo numero de la matriz es: ", self.matriz[self.fila -1][self.columna -1] 

    def insertar_dato(self):
        self.fila = 0
        self.columna = 0   
        print "Elige la posicion en la matriz para insertar dato" 
        self.fila = input ('Posicion en fila: ')
        self.columna = input ('\nPosicion en columna: ')
        self.matriz[self.fila][self.columna] = input ("Dato a ingresar: ")
    
    def comprobar(self):
        for i in range (self.fila):
            for j in range (self.columna):                
                if (self.matriz[i][j] == 0):
                    print "La matriz no esta completamente llena\n"
                    print self.matriz
    
    def buscar(self):
        busqueda = raw_input("Elige dato a buscar en la matriz: ")
        for i in range (self.fila):
            for j in range (self.columna):
                if (self.matriz[i][j] == busqueda):
                    print "La posicion del dato se encuenta en: ", i, j                

    def eliminar(self):
        busqueda = raw_input("Elige dato a eliminar en la matriz: ")
        for i in range (self.fila):
            for j in range (self.columna):
                if (self.matriz[i][j] == busqueda):
                    self.matriz[i][j] = 0                 

    def actualizar_dato(self):
        self.fila = 0
        self.columna = 0   
        print "Elige la posicion en la matriz para actualizar dato" 
        self.fila = input ('Posicion en fila: ')
        self.columna = input ('\nPosicion en columna: ')
        self.matriz[self.fila][self.columna] = input ("Dato a actualizar: ")                

objeto = Matriz()

while(True): 
    objeto.menu()
    opcion = raw_input('\nElige una opcion del menu: ')
    if (opcion != "1" and objeto.matriz == []):
        print "Cree una Matriz para poder operarla\n"
    elif (opcion == "1"):
        objeto.crear_matriz()
    elif (opcion == "2"):
        objeto.calcular_tamanio()
    elif (opcion == "3"):
        objeto.ultimo_numero()
    elif (opcion == "4"):
        objeto.comprobar()
    elif (opcion == "5"):
        objeto.insertar_dato()
    elif (opcion == "6"):
        objeto.buscar()    
    elif (opcion == "7"):
        objeto.eliminar()
    elif (opcion == "8"):
        objeto.actualizar_dato()
    else:
        print "Ha escogido una opcion invalida" 


