print " "
print ' *** Calculador de area de circulo ***'
print " "
opcion=raw_input('Desea calcular el area [s/n].  ')
print ' '
print ' *** Gracias por usar el programa ***'
while opcion == 's' or opcion == 'S' :
    print " " 
    radio=int(raw_input('Introduzca radio  '))
    area=3.1416*radio*radio
    print ' ' 
    print 'El area es: ',area
    print ' '
    opcion=raw_input('Deseas repetir el proceso [s/n]  ')
    print ' '
    print ' *** Gracias por usar el programa ***'