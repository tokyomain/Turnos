from claseEmpleado import *
from funcionesAux import *

oPedro = Empleado('Pedro')
oJuan = Empleado('Juan')
oMatias = Empleado('Matias')
lista = []
lista.append(oPedro)
lista.append(oJuan)
lista.append(oMatias)
# Lo siguiente funciona correctamente retornando los nombres en formato str de los empleados:
#for empleado in lista:
#    print(empleado.__str__())


SEMANA = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'] 
LISTA_EMPLEADOS = ['Juan', 'Nito1', 'Nito2', 'Pocho', 'Matias', 'Diego', 'Marcelo', 'Paco', 'David']

diccionario = crear_dict_empleados(LISTA_EMPLEADOS)
print(f'Diccionario: {diccionario}')

print(oJuan)