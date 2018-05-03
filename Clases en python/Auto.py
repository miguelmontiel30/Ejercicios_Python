from Transporte import Transporte

ferrari = Transporte()

ferrari.color = 'Rojo'
ferrari.velocidad = 350
ferrari.modelo = 'Enzo Ferrari'
ferrari.no_ruedas = 4

ferrari.avanzar()
print ferrari.color
print ferrari.modelo

ferrari.girar()
print ferrari.acelerar(), 'a 300 Kph'

print ferrari.suma(ferrari.suma(20,15), 15)

n3 = ferrari.suma(20, 10)
n4 = ferrari.suma(n3, 15)
print n4