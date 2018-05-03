class transporte:
    def __init__(self,marca,modelo,color,ventanas,ruedas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ventanas = ventanas
        self.ruedas = ruedas
        print 'El transporte es de la marca',self.marca,'modelo',self.modelo
        print 'Es de color',self.color,'tiene',self.ventanas,'con',self.ruedas

    def soy (self,tr):
        print 'Soy un transporte',tr

    def voy (self,corre):
        print 'voy en',corre

    def capacidad (self,llevo):
        print 'Puedo llevar',llevo

class transporteterrestre(transporte):
    def terrestre (self,tipo,tamanio,apariencia):
        self.tipo = tipo
        self.tamanio = tamanio
        self.apariencia = apariencia
        print 'El transporte es un',self.tipo,'es',self.tamanio,'se ve en',self.apariencia

    def estado (self,es):
        print 'El transporte esta', es

    def voya (self,vy):
        print 'Voy a ',vy

carro = transporteterrestre('Chevrolet', '2015', 'Azul','4 ventanas','4 ruedas')
carro.terrestre('transporte privado','pequenio','Buen estado')
carro.soy('terrestre')
carro.voya('120 Km/hr')
carro.capacidad('5 Pasajeros')
carro.estado('Incomodo')
carro.voy('Sentido contrario\n\n')

autobus = transporteterrestre('Mercedez Benz', '2017', 'Gris','40 ventanas','20 ruedas')
autobus.terrestre('transporte publico','grande','Mal estado')
autobus.soy('terrestre')
autobus.voya('90 Km/hr')
autobus.capacidad('80 Pasajeros')
autobus.estado('Muy comodo')
autobus.voy('Reversa')