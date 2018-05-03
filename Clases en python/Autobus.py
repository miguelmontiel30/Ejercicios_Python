"""
Nombre: Miguel Angel Ortega Montiel
Matricula: 1716110490
Fecha: 7/01/2017
Descripcion: Imprime caracteristicas de un Autobus
"""
class Autobus:
	Compania=""
	Color=""
	No_LLantas=""
	Capacidad=""
	Marca=""
	No_Ventana=""
	def __init__ (self):
		pass

objeto_autobus=Autobus()
objeto_autobus.Compania="ADO"
objeto_autobus.Color="Gris"
objeto_autobus.No_LLantas="10"
objeto_autobus.Capacidad="50"
objeto_autobus.Marca="Mercedes Benz"
objeto_autobus.No_Ventanas="40"

print objeto_autobus.Compania
print objeto_autobus.Color
print objeto_autobus.No_LLantas
print objeto_autobus.Capacidad
print objeto_autobus.Marca
print objeto_autobus.No_Ventana

objeto_autobus2=Autobus()
objeto_autobus2.Compania="Futura"
objeto_autobus2.Color="Blanco"
objeto_autobus2.No_LLantas="10"
objeto_autobus2.Capacidad="60"
objeto_autobus2.Marca="Volvo"
objeto_autobus2.No_Ventana="30"

print objeto_autobus2.Compania
print objeto_autobus2.Color
print objeto_autobus2.No_LLantas
print objeto_autobus2.Capacidad
print objeto_autobus2.Marca
print objeto_autobus2.No_Ventana