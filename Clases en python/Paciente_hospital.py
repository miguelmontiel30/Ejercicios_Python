"""
Nombre: Miguel Angel Ortega Montiel
Matricula: 1716110490
Fecha: 7/01/2017
Descripcion: Imprime caracteristicas de un Paciente de hospital
"""

class Paciente:
	nombre=""
	enfermedad=""
	edad=""
	tipo_sangre=""
	estado=""
	sexo=""
	def __init__ (self):
		pass

objeto_paciente=Paciente()
objeto_paciente.nombre="Miguel"
objeto_paciente.enfermedad="tos"
objeto_paciente.edad="18"
objeto_paciente.tipo_sangre="A+"
objeto_paciente.estado="normal"
objeto_paciente.sexo="hombre"

print objeto_paciente.nombre
print objeto_paciente.enfermedad
print objeto_paciente.edad
print objeto_paciente.tipo_sangre
print objeto_paciente.estado
print objeto_paciente.sexo

objeto_paciente_paciente2=Paciente()
objeto_paciente_paciente2.nombre="Pedro"
objeto_paciente_paciente2.enfermedad="Choque"
objeto_paciente_paciente2.edad="22"
objeto_paciente_paciente2.tipo_sangre="O+"
objeto_paciente_paciente2.estado="Grave"
objeto_paciente_paciente2.sexo="hombre"

print objeto_paciente_paciente2.nombre
print objeto_paciente_paciente2.enfermedad
print objeto_paciente_paciente2.edad
print objeto_paciente_paciente2.tipo_sangre
print objeto_paciente_paciente2.estado
print objeto_paciente_paciente2.sexo

