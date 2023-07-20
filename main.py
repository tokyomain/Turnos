import copy
import logging
from claseEmpleado import *
from funcionesAux import *
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

# CONSTANTES
SEMANA = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'] 

# VARIABLES GOBLALES
lista_acciones = ['ver_lista_empleados', 'modificar_lista_empleados', 'asignar_empleado_turno_noche', 'ver_empleado_turno_noche',
                  'asignar_francos', 'ver_francos_asignados', 'asignar_turnos', 'ver_turnos_asignados',
                  'ver_horas_trabajadas', 'salir']
lista_empleados = ['David', 'Diego', 'Juan', 'Marcelo', 'Matias', 'Nito', 'Paco', 'Pocho', 'Ruben']
turnos = {'Lunes': {'Mañana': [], 'Tarde': [], 'Noche': []}, 'Martes': {'Mañana': [], 'Tarde': [], 'Noche': []},
          'Miercoles': {'Mañana': [], 'Tarde': [], 'Noche': []}, 'Jueves': {'Mañana': [], 'Tarde': [], 'Noche': []},
          'Viernes': {'Mañana': [], 'Tarde': [], 'Noche': []}, 'Sabado': {'Mañana': [], 'Tarde': [], 'Noche': []},
          'Domingo': {'Mañana': [], 'Tarde': [], 'Noche': []}}

francos = {'Lunes': [], 'Martes': [], 'Miercoles': [], 'Jueves': [], 'Viernes': [], 'Sabado': [], 'Domingo': []}

#------------------------------------------------------------------------------------------------------
#                                          Programa Principal
#------------------------------------------------------------------------------------------------------
logging.debug('Comienzo de programa.')
dict_objetos = crear_dict_empleados(lista_empleados)
logging.debug('Diccionario de Objetos Empleados: %s' % dict_objetos)
# En principio deberiamos crear un menu con opciones donde el usuario puede elegir las accion a realizar:
    # 1 - Ver lista de empleados. OK
    # 2 - Asignar empleado turno noche. OK
    # 3 - Ver empleado turno noche. OK
    # 4 - Asignar francos. OK
    # 5 - Ver francos asignados. OK
    # 6 - Asignar turnos. OK
    # 7 - Ver turnos Asignados
    # 8 - Ver horas trabajadas de cada empleado.
    # 9 - Salir.

# MENU PRINCIPAL
while True:
    # Esto puede ser una funcion > muestra_menu VER

    print('----------------------------------')    
    print('              MENU ')
    print('----------------------------------')
    print()
    print('1 - Ver Lista de empleados')
    print('2 - Modificar lista de empleados ')
    print('3 - Asignar Empleado turno noche')
    print('4 - Ver Empleado turno noche ')
    print('5 - Asignar francos')
    print('6 - Ver francos asignados')
    print('7 - Asignar turnos')
    print('8 - Ver turnos Asignados')
    print('9 - Ver Horas Trabajadas de cada empleado')
    print('10 - Salir')
    print('----------------------------------')
    

    accion = input(f'Que tarea desea realizar? Ingrese un número (1-{len(lista_acciones)}) y luego "Enter" > ')
    try:
        accion = int(accion)
        if not (1 <= accion <= 10):
            print(f'Por favor, ingrese una respuesta válida. "{accion}" no es una respuesta válida.')

        # Ver lista de empleados
        elif accion == 1:
            logging.debug('Ver lista Empleados')
            ver_lista_empleados(lista_empleados)
            continuar = input("Presione 'Enter' para continuar y volver al Menu Principal > ")
        # Modificar lista de empleados
        elif accion == 2:
            modificar_lista_empleados(lista_empleados)
            continuar = input("Presione 'Enter' para continuar y volver al Menu Principal > ")
        # Asignar empleado turno noche
        elif accion == 3:
            if len(turnos['Lunes']['Noche']) == 1:
                print(f"Ya existe un empleado asignado para el turno noche: {turnos['Lunes']['Noche'][0]}")
                cambiar = input('Desea reemplazar el empleado asignado? (S/N) > ')
                if cambiar == 's' or cambiar =='S':
                    logging.debug('Reemplazando empleado turno Noche.')
                    reemplazar_empleado_noche(dict_objetos, lista_empleados.copy(), turnos)
                    continuar = input("Presione 'Enter' para continuar y volver al Menu Principal > ")
                else:
                    continue
            else:
                logging.debug('Asignando empleado turno Noche.')
                asignar_empleado_noche(dict_objetos, lista_empleados.copy(), turnos)
                continuar = input("Presione 'Enter' para continuar y volver al Menu Principal > ")

            logging.debug('Empleado turno noche: %s' % turnos['Lunes']['Noche'][0])

        # Ver Empleado turno noche
        elif accion == 4:
            logging.debug('Viendo empleado turno Noche.')
            ver_empleado_noche(turnos)
            continuar = input("Presione 'Enter' para continuar y volver al Menu Principal > ")

        # Asignar francos
        elif accion == 5:
            # TODO: Asociar nombres con objetos
            logging.debug('Asignando francos para la semana.')
            asignar_francos(SEMANA, lista_empleados.copy(), dict_objetos, francos, turnos)
            continuar = input("Presione 'Enter' para continuar y volver al Menu Principal > ")
            logging.debug('Francos asignados para esta semana: %s' % francos)

        # Ver francos asignados
        elif accion == 6:
            logging.debug('Viendo francos para la semana.')
            ver_francos_asignados(francos)
            continuar = input("Presione 'Enter' para continuar y volver al Menu Principal > ")

        # Asignar Turnos
        elif accion == 7:
            for dia in SEMANA:
                asignar_turnos(dia, francos, lista_empleados.copy(), dict_objetos, turnos, 'Mañana')
                asignar_turnos(dia, francos, lista_empleados.copy(), dict_objetos, turnos, 'Tarde')
            print(f'Los turnos han sido asignados.')
            continuar = input("Presione 'Enter' para continuar y volver al Menu Principal > ")
            print(turnos)
        # Ver Turnos asignados
        #elif accion == 8:
        # Ver horas trabajadas por cada empleado
        elif accion == 9:
            print('----------------------------------')
            print('Horas trabajadas por cada empleado en esta semana: ')
            for emp in lista_empleados:
                print(f'{emp} : {dict_objetos[emp].horas_trabajadas}')
            print('----------------------------------')
        elif accion == 10:
            print('El programa finalizará. Hasta pronto!')
            break
    except ValueError as error:
        print('Error: {}'.format(str(error)))


