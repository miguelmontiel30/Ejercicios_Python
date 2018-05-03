a = []
tam = input('Ingresa tamanio del arreglo: ')
suma = 0

for i in range (tam):
    a.append(input('\nvalores: '))
    suma = suma + a[i]

for i in range (tam):
    for p in range (tam -1):
        if a[p] > a[p+1]:
            tmp = a[p]
            a[p] = a[p+1]
            a[p+1] = tmp

print '\nEl valor minimo es: ',a[0]
print '\nEl valor maximo es: ',a[p+1]
print '\nEl promedio es: {0}'.format(suma/tam)
