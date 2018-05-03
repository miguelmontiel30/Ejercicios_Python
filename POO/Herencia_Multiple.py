class Transporte:
    def __init__(self,tamanio,capacidad,velocidad,color,estado):
        self.tamanio = tamanio
        self.capacidad = capacidad
        self.velocidad = velocidad
        self.color = color
        self.estado = estado
        print ' \n\n***** Tipos de Transportes  *****'
        print '\nEl transporte es de tamanio',self.tamanio,'su capacidad es de',self.capacidad,'va a',self.velocidad
        print 'es de color',self.color,'esta',self.estado

    def andar (self):
        print 'Voy a marcha veloz'

    def transportar (self):
        print 'Tengo pasajeros abordo'

    def cargar(self):
        print 'Necesito combustible'

class TransporteTerrestre(Transporte):
    def propiedades1 (self,marca,no_ruedas):
        self.marca = marca
        self.no_ruedas = no_ruedas
        print 'El transporte es de la marca',self.marca,'Tiene',self.no_ruedas

    def verificar (self,objeto):
        print 'Necesito revisar el ', objeto

    def derrapar (self,derrape):
        print 'Estoy derrapando en',derrape

class TransporteAereo(Transporte):
    def propiedades2 (self,helices,alas,turbinas):
        self.helices = helices
        self.alas = alas
        self.turbinas = turbinas
        print 'El Transporte aereo tiene',self.helices,'y',self.alas,'con',self.turbinas

    def volar (self):
        print 'Estoy volando muy rapido'

    def turbulencia (self):
        print 'Tengo turbulencia en el viaje'

class TransporteMarino(Transporte):
    def propiedades3 (self,no_velas,ancla,no_trip,):
        self.no_velas = no_velas
        self.ancla = ancla
        self.no_trip = no_trip
        print 'El transporte tiene',self.no_velas,'tiene una ancla',self.ancla,'lleva',self.no_trip

    def navegar (self):
            print 'Estoy navegando en altamar'

    def tripular (self):
            print 'Tengo muchos tripulantes'

class Aerodeslizador(TransporteTerrestre,TransporteMarino):      #Declaro la herencia multiple
    def propiedades4 (self,aire,combustible):
        self.aire =aire
        self.combustible = combustible
        print 'La camara del Aerodeslizador esta',self.aire,'Tiene el tanque',self.combustible
    
    def flotando (self):
        print 'Estoy navegando'

    def floto (self,flotar):
        print 'Estoy flotando sobre',flotar


deslizador = Aerodeslizador('Grande\n', '40 Pasajeros\n', '70 Km/hr\n','Verde\n','Encendido')
deslizador.propiedades1('Aero','sin llantas\n')
deslizador.propiedades3('Sin velas','Pequenio','5 Pasajeros')
deslizador.propiedades4('muy inflada','Vacio')
deslizador.verificar('el timon')
deslizador.derrapar('la arena')
deslizador.flotando()
deslizador.floto('El agua')
deslizador.navegar()
deslizador.tripular()

metrobus = TransporteTerrestre('Grande\n', '40 Pasajeros\n', '70 Km/hr\n','Verde\n','Encendido')
metrobus.propiedades1('Audi','20 ruedas\n')
metrobus.andar()
metrobus.transportar()
metrobus.cargar()
metrobus.verificar('cofre')
metrobus.derrapar('la tierra')

avion = TransporteAereo('Gigante\n','200 Pasajeros\n','200 Km/hr\n','Azul\n','Encendido')
avion.propiedades2('0 helices','2 alas','4 turbinas')
avion.andar()
avion.transportar()
avion.cargar()
avion.volar()
avion.turbulencia()

barco = TransporteMarino('Gigante\n','300 Pasajeros\n','60Km/hr\n','Gris\n','Encendido')
barco.propiedades3('5 velas','grande','300 tripulantes')
barco.andar()
barco.transportar()
barco.cargar()
barco.navegar()
barco.tripular()


