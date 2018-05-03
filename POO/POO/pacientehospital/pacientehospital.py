"""
Nombre: Jorge Luic Joce Aguilar
Matricula: 1716110232
Fecha: 6/Enero/2017
Deccripcion: Muestra las caracteristicas de un paciente de un hospital
"""

class PacienteH:
	nombre=""
	telefono=""
	direccion=""
	tiposangre=""
	genero=""
	edad=""
	def __init__ (self):
		pass
objeto_pacienteh_paciente1=PacienteH()
objeto_pacienteh_paciente1.nombre="Jorge Luis"
objeto_pacienteh_paciente1.telefono="7751015289"
objeto_pacienteh_paciente1.direccion="Cuautepec"
objeto_pacienteh_paciente1.tiposangre="O positivo"
objeto_pacienteh_paciente1.genero="Masculino"
objeto_pacienteh_paciente1.edad="18"

print objeto_pacienteh_paciente1.nombre
print objeto_pacienteh_paciente1.telefono
print objeto_pacienteh_paciente1.direccion
print objeto_pacienteh_paciente1.tiposangre
print objeto_pacienteh_paciente1.genero
print objeto_pacienteh_paciente1.edad

print "/////////////////////////////"

objeto_pacienteh_paciente2=PacienteH()
objeto_pacienteh_paciente2.nombre="Teresa soto"
objeto_pacienteh_paciente2.telefono="7751458922"
objeto_pacienteh_paciente2.direccion="La lagunilla"
objeto_pacienteh_paciente2.tiposangre="O negativo"
objeto_pacienteh_paciente2.genero="Femenina"
objeto_pacienteh_paciente2.edad="18"

print objeto_pacienteh_paciente2.nombre
print objeto_pacienteh_paciente2.telefono
print objeto_pacienteh_paciente2.direccion
print objeto_pacienteh_paciente2.tiposangre
print objeto_pacienteh_paciente2.genero
print objeto_pacienteh_paciente2.edad

"""
print "/////////////////////////////"

objeto_pacienteh_paciente3=PacienteH()
objeto_pacienteh_paciente3.nombre="Daniela Jimenez"
objeto_pacienteh_paciente3.telefono="7751254322"
objeto_pacienteh_paciente3.direccion="El paraiso"
objeto_pacienteh_paciente3.tiposangre="a positivo"
objeto_pacienteh_paciente3.genero="Femenina"
objeto_pacienteh_paciente3.edad="19"

print objeto_pacienteh_paciente3.nombre
print objeto_pacienteh_paciente3.telefono
print objeto_pacienteh_paciente3.direccion
print objeto_pacienteh_paciente3.tiposangre
print objeto_pacienteh_paciente3.genero
print objeto_pacienteh_paciente3.edad
"""