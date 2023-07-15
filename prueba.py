from claseEmpleado import *
from funcionesAux import *
'''
oPedro = Empleado('Pedro')
oJuan = Empleado('Juan')
oMatias = Empleado('Matias')
lista = []
lista.append(oPedro)
lista.append(oJuan)
lista.append(oMatias)'''
# Lo siguiente funciona correctamente retornando los nombres en formato str de los empleados:
#for empleado in lista:
#    print(empleado.__str__())


SEMANA = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'] 
LISTA_EMPLEADOS = ['Juan', 'Nito', 'Ruben', 'Pocho', 'Matias', 'Diego', 'Marcelo', 'Paco', 'David']
lista2 = sorted(LISTA_EMPLEADOS)
print(lista2)

'''
diccionario = crear_dict_empleados(LISTA_EMPLEADOS)
print(f'Diccionario: {diccionario}')
'''
DICCIONARIO_OBJETOS = crear_dict_empleados(LISTA_EMPLEADOS)
'''
lista__ = lista_nombre_hs(DICCIONARIO_OBJETOS)
print(lista__)
# Como interactuar con los objectos:
DICCIONARIO_OBJETOS['Pocho'].actualizar_horas_trabajadas(8)
print(DICCIONARIO_OBJETOS['Pocho'].horas_trabajadas)
DICCIONARIO_OBJETOS['Juan'].asignar_franco_semanal('Lunes')
print(DICCIONARIO_OBJETOS['Juan'].obtener_franco_semanal())

lista_empleados_copia = copy.deepcopy(LISTA_EMPLEADOS)
'''

# Cambios 14/7
#   - Agregado modulo 'logging' para debugear.
#   - Agregada estructura para alojar francos. Diccionario
#   - Agregada la funcion asignar_francos.
#   - Agregada la funcion ver_francos_asignados
