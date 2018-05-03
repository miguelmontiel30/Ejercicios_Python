"""
Nombre: Miguel Angel Ortega Montiel
Matricula: 1716110490
Fecha: 7/01/2017
Descripcion: Imprime caracteristicas de un Conejo
"""
class Conejo:
	color=""
	edad=""
	peso=""
	pelaje=""
	sexo=""
	estado=""
	def __init__ (self):
		pass

objeto_conejo=Conejo()
objeto_conejo.color="Gris"
objeto_conejo.edad="3 Meses"
objeto_conejo.peso="4 kg"
objeto_conejo.pelaje="Mucho"
objeto_conejo.sexo="Macho"
objeto_conejo.estado="Bueno"

print objeto_conejo.color
print objeto_conejo.edad
print objeto_conejo.peso
print objeto_conejo.pelaje
print objeto_conejo.sexo
print objeto_conejo.estado

objeto_conejo2=Conejo()
objeto_conejo2.color="Blanco"
objeto_conejo2.edad="1 mes"
objeto_conejo2.peso="2 kg"
objeto_conejo2.pelaje="Mucho"
objeto_conejo2.sexo="Macho"
objeto_conejo2.estado="Enfermo"

print objeto_conejo2.color
print objeto_conejo2.edad
print objeto_conejo2.peso
print objeto_conejo2.pelaje
print objeto_conejo2.sexo
print objeto_conejo2.estado
