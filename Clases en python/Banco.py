"""
Nombre: Miguel Angel Ortega Montiel
Matricula: 1716110490
Fecha: 7/01/2017
Descripcion: Imprime caracteristicas de un Banco
"""
class Banco:
	Nombre=""
	Domicilio=""
	No_Empleados=""
	No_ventanillas=""
	No_Cajeros=""
	No_Oficinas=""
	
	def __init__ (self):
		pass

objeto_banco=Banco()
objeto_banco.Nombre="Banamex"
objeto_banco.Domicilio="Tulancingo"
objeto_banco.No_empleados="40"
objeto_banco.No_ventanilas="15"
objeto_banco.No_Cajeros="4"
objeto_banco.No_Oficinas="7"

print objeto_banco.Nombre
print objeto_banco.Domicilio
print objeto_banco.No_empleados
print objeto_banco.No_ventanillas
print objeto_banco.No_Cajeros
print objeto_banco.No_Oficinas

objeto_banco2=Banco()
objeto_banco2.Nombre="HSBC"
objeto_banco2.Domicilio="Santiago"
objeto_banco2.No_empleados="25"
objeto_banco2.No_ventanillas="9"
objeto_banco2.No_Cajeros="5"
objeto_banco2.No_Oficinas="5"

print objeto_banco2.Nombre
print objeto_banco2.Domicilio
print objeto_banco2.No_empleados
print objeto_banco2.No_ventanillas
print objeto_banco2.No_Cajeros
print objeto_banco2.No_Oficinas
