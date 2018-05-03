class Transporte:
    def __init__(self,tipo,capacidad,velocidad,color,no_vent):
        self.tipo = tipo
        self.capacidad = capacidad
        self.velocidad = velocidad
        self.color = color
        self.no_vent = no_vent
        print ' \n\n***** Transportes usados *****'
        print '\nEl transporte es de tipo',self.tipo,'su capacidad es de',self.capacidad,'va a',self.velocidad,'es de color',self.color,'tiene',self.no_vent

    def andar (self):
        print 'Voy a marcha veloz'

    def subiendo (self):
        print 'Estoy llenando pasaje'

    def estado(self):
        print 'Estoy totalmente completo'

class TransporteTerrestre(Transporte):
    def propiedades (self,nombre,no_ruedas,tamanio):
        self.nombre = nombre
        self.no_ruedas = no_ruedas
        self.tamanio = tamanio
        print 'El transporte es de la compania',self.nombre,'Tiene',self.no_ruedas,'Su tamanio es',self.tamanio

    def verificar (self,objeto):
        print 'Necesito revisar el ', objeto

    def encendido (self,enc):
        print 'EL Transporte esta ',enc

class TransporteAereo(Transporte):
class TransporteMarino(Transporte):
    def propiedades (self,tipo,no_velas,metros_sum,no_trip,)
        self.tipo = tipo
        self.no_velas = no_velas
        self.metros_sum = metros_sum
        self.no_trip = no_trip
        print 'El transporte es',self.tipo,'tiene',self.no_velas,
class Aerodeslizador(TransporteTerrestre,TransporteMarino):

metrobus = TransporteTerrestre('Metrobus\n', '40 Pasajeros\n', '70 Km/hr\n','Verde\n','30 ventanas\n')
metrobus.propiedades('ADO\n','20 ruedas\n','Grande\n\n')
metrobus.andar()
metrobus.verificar('Cofre')
metrobus.subiendo()
metrobus.estado()
metrobus.encendido('Apagado')

