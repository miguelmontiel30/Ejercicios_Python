print (''
)
print ('   **** Calculador de edad *****   ')
print ('')

a=int(raw_input('Introduce tu Anio de nacimiento. '))

print ('')

b=int( raw_input ('Introduce el Anio actual. '))

print ('')

if a>1910 and a<b:
    
	edad=b-a
    
	print ('')
    
	print ('Tu Anio de nacimiento es:'),a, ('Tu edad es: '),edad

else:
    print ('Datos no validos')