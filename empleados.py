from claseEmpleado import *
from funcionesAux import *
import copy

# CONSTANTES
SEMANA = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'] 
LISTA_EMPLEADOS = ['Juan', 'Nito1', 'Nito2', 'Pocho', 'Matias', 'Diego', 'Marcelo', 'Paco', 'David']


#------------------------------------------------------------------------------------------------------
#                                          Programa Principal
#------------------------------------------------------------------------------------------------------

# En principio deberiamos crear un menu con opciones donde el usuario puede elegir las accion a realizar:
    # Ver lista de empleados completa.
    # Ver empleado turno noche.
    # Asignar empleado turno noche
    # Ver francos
    # Asignar francos
    # Ver disponibilidad
    # Asignar vacaciones

# MENU
while True:
    print('               ------------------------------------')    
    print('                               MENU ')
    print('               ------------------------------------')
    print()
    print('                    1 - Ver Lista de Empleados')
    print('                    2 - Asignar Empleado Turno Noche')
    print('                    3 - Ver Empleado asignado para Turno Noche ')
    print('                    4 - Asignar Francos')
    print('                    5 - Ver Francos asignados')
    print('                    6 - Asignar Turnos')
    print('                    7 - Ver Turnos Asignados')
    print('                    8 - Asignar Vacaciones')
    print('                    9 - Ver Vacaciones')
    print('                    10 - Salir')
    print('               ------------------------------------')
    
    accion = input('Que tarea desea realizar? (1-10) >')
    try:
        accion = int(accion)
        if not (1 <= accion <= 10):
            print(f'Por favor, ingrese una respuesta válida. "{accion}" no es una respuesta válida.')
        else:
            continue
    except ValueError:
        print(f'Por favor, ingrese una respuesta válida. "{accion}" no es una respuesta válida.')

DICCIONARIO_OBJETOS = crear_dict_empleados(LISTA_EMPLEADOS)
'''
lista__ = lista_nombre_hs(DICCIONARIO_OBJETOS)
print(lista__)
# Como interactuar con los objectos:
DICCIONARIO_OBJETOS['Pocho'].actualizar_horas_trabajadas(8)
print(DICCIONARIO_OBJETOS['Pocho'].horas_trabajadas)
DICCIONARIO_OBJETOS['Juan'].asignar_franco_semanal('Lunes')
print(DICCIONARIO_OBJETOS['Juan'].obtener_franco_semanal())
'''

print(f'----------------------------------\n        Lista de empleados\n----------------------------------')
for count, empleado in enumerate(LISTA_EMPLEADOS, start=1):
    print('    ', count, '-', empleado)
print('----------------------------------')

# Todo lo siguiente deberia estar dentro de la funcion quitar_empleado_noche
# y la funcion deberia llamarse asignar_empleado_noche.


lista_empleados_copia = copy.deepcopy(LISTA_EMPLEADOS)
lista_empleados_copia= asignar_empleado_noche(empleado_noche, lista_empleados_copia, DICCIONARIO_OBJETOS, LISTA_EMPLEADOS)

# print(f'----------------------------------\nLista de empleados sin Empleado del Turno Noche\n----------------------------------')
'''for count, empleado in enumerate(lista_empleados_copia, start=1):
    print('    ', count, empleado)
'''    
# TODO: Asignar Francos OK
dict_francos = asignar_francos(SEMANA, lista_empleados_copia)
print(dict_francos)

# Una vez que tenemos el diccionario de francos armado podemos proceder a asignar turnos,
# lo que deberiamos hacer es, para cada dia consultar este diccionario y quitar de la lista
# al empleado que este de franco.

# TODO: Asignar turnos
 
# Preparar la lista sin el empleado de franco del dia
# Esto lo debo hacer dentro de la funcion que itere sobre cada dia para asignar los turnos

