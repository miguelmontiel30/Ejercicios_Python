print " "
print ' **** Programa calculador de edad ****'
print " "
opcion=raw_input('Desea saber su edad [s/n].  ')
while opcion == 's' or opcion == 'S' :
    print " " 
    anio=int(raw_input('Introduzca su anio de nacimiento  '))
    edad=2016-anio
    print ' ' 
    print 'Su edad es: ',edad
    print ' '
    opcion=raw_input('Deseas repetir el proceso [s/n]  ')