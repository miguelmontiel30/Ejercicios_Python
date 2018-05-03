print ''
print '   **** Programa sumatorio *****   '
print ''
a = int(raw_input('Primer valor para sumar.  '))
b = int(raw_input('Segundo valor para sumar.  '))
if a>0 and b>0:
    suma = a+b
    print 'El resultado de la suma es:',suma
else:  
    print "Solo numeros positivos"
