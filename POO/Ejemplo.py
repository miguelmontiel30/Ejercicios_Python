class Objeto(): 
    color = "verde" 
    tamanio = "grande" 
    aspecto = "feo" 
    
    def flotar(self): 
        print 12 
 
et = Objeto() 
print et.color 
print et.tamanio 
print et.aspecto 
et.color = "rosa" 
print et.color