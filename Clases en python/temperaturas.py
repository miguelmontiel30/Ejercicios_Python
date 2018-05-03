a = [0,0,0,0,0,0,0,0,0,0]

suma = 0

for i in range (10):
    a[i] = input('Ingresa la temperatura: ')
    suma = suma + a[i]

print '\nEl promedio es: {0}'.format(suma/10)