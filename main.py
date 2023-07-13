from claseEmpleado import *
from funcionesAux import *
import copy

# CONSTANTES
SEMANA = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'] 
# Uso una lista para la siguiente estructura porq es mutable, y algun dia se 
# ..puede incorporar o darse de baja algun empleado.
LISTA_EMPLEADOS = ['David', 'Diego', 'Juan', 'Marcelo', 'Matias', 'Nito', 'Paco', 'Pocho', 'Ruben']

# VARIABLES GOBLALES
turnos = {'Lunes': {'Mañana': [], 'Tarde': [], 'Noche': []}, 'Martes': {'Mañana': [], 'Tarde': [], 'Noche': []},
          'Miercoles': {'Mañana': [], 'Tarde': [], 'Noche': []}, 'Jueves': {'Mañana': [], 'Tarde': [], 'Noche': []},
          'Viernes': {'Mañana': [], 'Tarde': [], 'Noche': []}, 'Sabado': {'Mañana': [], 'Tarde': [], 'Noche': []},
          'Domingo': {'Mañana': [], 'Tarde': [], 'Noche': []}}


#------------------------------------------------------------------------------------------------------
#                                          Programa Principal
#------------------------------------------------------------------------------------------------------
d = crear_dict_empleados(LISTA_EMPLEADOS)

# En principio deberiamos crear un menu con opciones donde el usuario puede elegir las accion a realizar:
    # 1 - Ver lista de empleados. OK
    # 2 - Asignar empleado turno noche. OK
    # 3 - Ver empleado turno noche. OK
    # 4 - Asignar francos.
    # 5 - Ver francos asignados.
    # 6 - Asignar turnos.
    # 7 - Ver turnos asignados.
    # 8 - Asignar vacaciones.
    # 7 - Ver vacaciones.
    # 8 - Salir.

# MENU PRINCIPAL
while True:
    # Esto puede ser una funcion > muestra_menu VER

    print('----------------------------------')    
    print('              MENU ')
    print('----------------------------------')
    print()
    print('1 - Ver Lista de empleados')
    print('2 - Asignar Empleado turno noche')
    print('3 - Ver Empleado turno noche ')
    print('4 - Asignar francos')
    print('5 - Ver francos asignados')
    print('6 - Asignar turnos')
    print('7 - Ver turnos Asignados')
    print('8 - Asignar Vacaciones')
    print('9 - Ver Vacaciones')
    print('10 - Salir')
    print('----------------------------------')
    

    accion = input('Que tarea desea realizar? (1-10) > ')
    try:
        accion = int(accion)
        if not (1 <= accion <= 10):
            print(f'Por favor, ingrese una respuesta válida. "{accion}" no es una respuesta válida.')
        elif accion == 1:
            ver_lista_empleados(LISTA_EMPLEADOS)
            accion = input("Presione 'Enter' para continuar > ")
        elif accion == 2:
            if len(turnos['Lunes']['Noche']) == 1:
                print(f"Ya existe un empleado asignado para el turno noche: {turnos['Lunes']['Noche'][0]}")
                cambiar = input('Desea reemplazar el empleado asignado? (S/N) > ')
                if cambiar == 's' or cambiar =='S':
                    reemplazar_empleado_noche(d, LISTA_EMPLEADOS, turnos)
                    accion = input("Presione 'Enter' para continuar > ")
                else:
                    continue
            else:
                asignar_empleado_noche(d, LISTA_EMPLEADOS, turnos)
                accion = input("Presione 'Enter' para continuar > ")

        elif accion == 3:
            ver_empleado_noche(turnos)
            accion = input("Presione 'Enter' para continuar > ")
        #elif accion ==4:
        #elif accion ==5:
        #elif accion ==6:
        #elif accion ==7:
        #elif accion ==8:
        #elif accion ==9:
        elif accion == 10:
            print('El programa finalizará. Hasta pronto!')
            break
    except ValueError:
        print(f'Por favor, ingrese una respuesta válida. "{accion}" no es una respuesta válida.')


# TODO: Asignar francos
# TODO: Ver francos asignados 
#print(turnos)