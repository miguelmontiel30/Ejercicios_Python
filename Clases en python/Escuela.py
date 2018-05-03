"""
Nombre: Miguel Angel Ortega Montiel
Matricula: 1716110490
Fecha: 7/01/2017
Descripcion: Imprime caracteristicas de una Escuela
"""
class Escuela:
	Nombre=""
	No_Aulas=""
	No_Profesores=""
	No_Alumnos=""
	No_Carreras=""
	Turnos=""
	def __init__ (self):
		pass

objeto_escuela=Escuela()
objeto_escuela.Nombre="UTEC"
objeto_escuela.No_Aulas="30"
objeto_escuela.No_Profesores="100"
objeto_escuela.No_Alumnos="900"
objeto_escuela.No_Carreras="6"
objeto_escuela.Turnos="2"

print objeto_escuela.Nombre
print objeto_escuela.No_Aulas
print objeto_escuela.No_Profesores
print objeto_escuela.No_Alumnos
print objeto_escuela.No_Carreras
print objeto_escuela.Turnos

objeto_escuela_escuela2=Escuela()
objeto_escuela_escuela2.Nombre="UPT"
objeto_escuela_escuela2.No_Aulas="40"
objeto_escuela_escuela2.No_Profesores="100"
objeto_escuela_escuela2.No_Alumnos="1000"
objeto_escuela_escuela2.No_Carreras="9"
objeto_escuela_escuela2.Turnos="2"

print objeto_escuela_escuela2.Nombre
print objeto_escuela_escuela2.No_Aulas
print objeto_escuela_escuela2.No_Profesores
print objeto_escuela_escuela2.No_Alumnos
print objeto_escuela_escuela2.No_Carreras
print objeto_escuela_escuela2.Turnos
