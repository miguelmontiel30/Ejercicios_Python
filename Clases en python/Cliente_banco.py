"""
Nombre: Miguel Angel Ortega Montiel
Matricula: 1716110490
Fecha: 7/01/2017
Descripcion: Imprime caracteristicas de un Cliente de Bancos
"""

class Cliente:
	Nombre=""
	Edad=""
	Domicilio="" 
	Telefono=""
	RFC=""
	Concepto=""

	def __init__ (self):
		pass

objeto_cliente=Cliente()
objeto_cliente.Nombre="Miguel"
objeto_cliente.Edad="18"
objeto_cliente.Domicilio="Nuevo Tulancingo"
objeto_cliente.Telefono="77511717"
objeto_cliente.RFC="7843747329847320948320"
objeto_cliente.Concepto="Deposito"

print objeto_cliente.Nombre
print objeto_cliente.Edad
print objeto_cliente.Domicilio
print objeto_cliente.Telefono
print objeto_cliente.RFC
print objeto_cliente.Concepto

objeto_cliente2=Cliente()
objeto_cliente2.Nombre="Angel"
objeto_cliente2.Edad="20"
objeto_cliente2.Domicilio="Singuilucan"
objeto_cliente2.Telefono="7752627282"
objeto_cliente2.RFC="743678463463297392"
objeto_cliente2.Concepto="Pago de servicios"

print objeto_cliente2.Nombre
print objeto_cliente2.Edad
print objeto_cliente2.Domicilio
print objeto_cliente2.Telefono
print objeto_cliente2.RFC
print objeto_cliente2.Concepto
