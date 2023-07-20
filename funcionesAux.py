from claseEmpleado import *
import random

# TODO: Funciones del Menu principal
    # 1- Ver Lista Empleados > Simplemente imprimir la lista de todos los empleados
    # 2- Asignar turno Noche > OK
    # 3- Ver Empleado turno Noche > devolver el empleado en cuestion.
    # 4- Asignar Francos > OK Ver
    # 5- Ver Francos asignados > OK
    # 6- Asignar turnos
    # 7- Ver turnos asignados
    # 8- Asignar vacaciones
    # 9- Ver vacaciones > devolver el empleado con vacaciones para esta semana.
# TODO: Podriamos separar entre funciones para crear estructuras y funciones de acciones. ANALIZAR
# TODO: La validacion de input podria ser una funcion.

# Ejemplo de como estructurar una funcion:
'''
def ejemplo(param1: int, param2: str):
    """
    [BRIEF]
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter
    Returns:
        bool: The return value. True for success, False otherwise.
    """
'''

def crear_dict_empleados(lista: str):
    '''
    Transforma una lista de strings en un diccionario, relacionando
    los nombres en la lista con las instancias de la clase Empleado.
    Args:
        lista (str): Lista de nombres.
    Returns:
        d: Diccionario : {'Nombre': 'Obj'}
    '''
    d = {}
    for nombre in lista:
        emp = Empleado(nombre)
        d[emp.__str__()] = emp
    return d

def lista_nombre_hs(dict_objetos: dict):
    ''' 
    Crea una lista de listas a partir del diccionario con las instancias de la
    clase Empleado.
    Args:
        diccionario (dict): Toma los nombres de empleados de este diccionario.
    Returns:
        Lista (list) : Lista de listas [Nombre, Horas trabajadas] 
    '''
    lista = []
    for nombre, empleado in dict_objetos.items():
        lista.append([nombre, empleado.obtener_horas_trabajadas()])
    return lista

def ver_lista_empleados(lista_empleados):
    '''
    Recibe una lista de empleados e imprime la lista completa de empleados formateada
    adecuadamente y consulta para agregar o quitar empleados.
    Args:
        lista_empleados (list): Lista de nombres de empleados.
    Returns:
        str: Visualizacion mejorada.
    '''
    print(f'----------------------------------\n        Lista de empleados\n----------------------------------')
    for count, empleado in enumerate(lista_empleados, start=1):
        print('    ', count, '-', empleado)
    print('----------------------------------')
    
        
def modificar_lista_empleados(lista_empleados):
    '''
    Agrega o quita empleados de la lista de empleados existente
    
    Args:
        lista_empleados (list): Lista existente
    Returns:
        lista_empleados (list): Lista modificada    
    '''
    flag = True
    ver_lista_empleados(lista_empleados)
    while True:
        cambiar = input('Desea agregar o quitar algun empleado? (S/N) > ')
        if cambiar == 's' or cambiar == 'S':
            que_hacer = input('Desea Agregar o Quitar un empleado? (A/Q) > ')
            if que_hacer == 'a' or que_hacer == 'A':
                nombre_nuevo_empleado = input('Escriba el nombre del empleado a agregar: > ')
                nombre_nuevo_empleado = nombre_nuevo_empleado.capitalize()
                lista_empleados.append(nombre_nuevo_empleado)
                print('Lista de empleados modificada: ')
                ver_lista_empleados(lista_empleados)
                flag = False
                return lista_empleados
            elif que_hacer == 'q' or que_hacer == 'Q':
                ver_lista_empleados(lista_empleados)
                while True:
                    try:
                        empleado_quitar = int(input(f'Selecccione un empleado para quitar? Ingrese un número (1-{len(lista_empleados)}) > '))
                        if empleado_quitar not in range(len(lista_empleados) + 1):
                            print(f'Por favor, ingrese una respuesta válida. "{empleado_quitar}" no es una respuesta válida.')
                        else:
                            empleado_quitado = lista_empleados.pop(empleado_quitar - 1)
                            print(f'El empleado "{empleado_quitado}" fue quitado de la lista de empleados.')
                            print('Lista de empleados modificada: ')
                            ver_lista_empleados(lista_empleados)
                            flag = False
                            return lista_empleados
                    except ValueError as error:
                        flag = False
                        print('Error: {}'.format(str(error)))            
        elif cambiar == 'n' or cambiar == 'N':
            return
        else: 
            print(f'Por favor, ingrese una respuesta válida. "{cambiar}" no es una respuesta válida.')
            return

def asignar_empleado_noche(dict_objetos, lista_empleados, turnos):
    '''Asigna empleado al turno noche, actualiza Turnos para el empleado Noche
    y actualiza sus atributos de horas trabajadas.
    Args:
        dict_objetos (dict): Diccionario para tomar las instancias de la clase Empleado.
        lista_empleados (list): Lista de empleados para poder seleccionar.
        turnos (dict): Estructura donde guardar los datos de empleado seleccionado para turno Noche.
    Returns:
        dict_objetos (dict): Diccionario con el empleado asignado a turno Noche.
    '''
    print('Seleccione un empleado de la lista para asignarlo al Turno Noche > ')
    ver_lista_empleados(lista_empleados)
    while True:
        try:
            empleado_noche = int(input('Selecccione un empleado para el turno Noche? Ingrese un número (1-9) > '))
            if not (1 <= empleado_noche <= 9):
                print(f'Por favor, ingrese una respuesta válida. "{empleado_noche}" no es una respuesta válida.')
            else:
                print(f'El empleado No. {empleado_noche} - "{lista_empleados[empleado_noche-1]}" está asignado para el turno Noche.')
                break
        except ValueError as error:
            print('Error: {}'.format(str(error)))
            
    nombre_empleado = lista_empleados[empleado_noche - 1]
        
    for dia in turnos.keys():
        turnos[dia]['Noche'].append(nombre_empleado)
    dict_objetos[nombre_empleado].actualizar_horas_trabajadas(56)
    dict_objetos[nombre_empleado].turnos = 'Noche'
    return turnos, dict_objetos

def reemplazar_empleado_noche(dict_objetos, lista_empleados, turnos):
    '''
    Reemplaza el empleado asignado para el turno noche.
    Args:
        dict_objetos (dict): Diccionario para tomar las instancias de la clase Empleado.
        lista_empleados (list): Lista de empleados para poder seleccionar.
        turnos (dict): Estructura donde guardar los datos de empleado seleccionado para turno Noche.
    Returns:
        dict_objetos (dict): Diccionario con el empleado reasignado a turno Noche.
    '''

    print('Seleccione un empleado de la lista para reasignar el Turno Noche > ')
    ver_lista_empleados(lista_empleados)
    while True:
        try:
            empleado_noche = int(input('Selecccione un empleado para reemplazar al empleado existente? Ingrese un número (1-9) > '))
            if not (1 <= empleado_noche <= 9):
                print(f'Por favor, ingrese una respuesta válida. "{empleado_noche}" no es una respuesta válida.')
            else:
                print(f'El empleado No. {empleado_noche} - "{lista_empleados[empleado_noche-1]}" está asignado para el turno Noche.')
                break
        except ValueError:
            print('Por favor, ingrese un número válido.')
            
    nombre_empleado = lista_empleados[empleado_noche - 1]
        
    for dia in turnos.keys():
        turnos[dia]['Noche'][0] = nombre_empleado
    dict_objetos[nombre_empleado].actualizar_horas_trabajadas(56)
    dict_objetos[nombre_empleado].turnos = 'Noche'
    return turnos, dict_objetos

def ver_empleado_noche(turnos):
    '''
    Imprime en consola el empleado asignado para el turno Noche de toda la semana
    Args:
        turnos (dict): Estructura con los turnos ya asignados.
    Returns:
        str: Empleado asignado para el turno Noche.
    '''
    try:
        if len(turnos['Lunes']['Noche'][0]) > 0:
            empleado_noche = turnos['Lunes']['Noche'][0]
            print(f'El empleado asignado a turno Noche es: {empleado_noche}')
    except IndexError:
        print('No hay empleado asignado para el turno Noche.')

def asignar_francos(SEMANA, lista_empleados, dict_objetos, francos, turnos):
    '''
    Asigna franco para cada empleado para la semana.
    VER: Implementar chequeo de Input.
    Args:
        SEMANA (list): Dias de la semana.
        lista_empleados (list): Lista de empleados para poder seleccionar.
        dict_objetos (dict): Para tomar las instancias de la clase Empleado.
        turnos (dict): Para saber el empleado asignado para turno noche y sacarlo de la lista.
    Returns:
        francos(dict): Diccionario con los francos de toda la semana para los empleados > {'Dia': 'Nombre'}.
    '''
    # Primero debo quitar de la lista al empleado del turno noche.
    try:
        empleado_turno_noche = turnos['Lunes']['Noche'][0]
    except IndexError:
        print('Aparentemente no hay un empleado asignado para el turno noche.\n'
              'Regrese al Menú Principal y asigne un empleado para el turno noche.')
        return
    lista_empleados.remove(empleado_turno_noche)
    print('Ahora asignaremos los francos para la semana:')
    flag = True
    while flag == True: 
        for dia in SEMANA:
            if len(lista_empleados) > 0:
                print('----------------------------------')
                for count, empleado in enumerate(lista_empleados, start=1):
                    print('    ', count, empleado)
                print('----------------------------------')
                emp = input(f'Asignar franco para el dia: {dia}.\n' 
                            'Seleccione un número de empleado y presione "Enter" o '
                            'presione "c(continuar) + Enter" si no quiere otorgar franco para este dia > ')
                if emp == 'c' or emp == 'C':
                    continue
                else:
                    emp = int(emp)
                    francos[dia].append(lista_empleados[emp - 1])
                    franco = lista_empleados.pop(emp -1 )
                    print(f'El empleado de franco para el dia {dia} es: {franco}')
                    continue
            flag = False
    return francos


def ver_francos_asignados(francos):
    '''
    Imprime en consola los francos asignados de toda la semana.
    Args:
        francos (dict): Estructura con los francos asignados.
    Returns:
        str: Lista de francos formateada.
    '''
    print(f'Francos para cada día:')
    print('----------------------------------')
    for dia, empleados in francos.items():
        if len(empleados) > 0:
            print(f'{dia}: ', end='')
            for i, empleado in enumerate(empleados):
                if i > 0:
                    print(' - ', end='')
                print(empleado, end='')
            print()
    print('----------------------------------')
# TODO:

def asignar_turnos(dia, francos, lista_empleados, dict_objetos, turnos, turno):
    '''
    Asigna turnos para el día y el turno seleccionado, evitando que el mismo empleado esté asignado
    tanto al turno de mañana como al turno de tarde del mismo día.
    
    Args:
        dia (str): Día de la semana.
        francos (dict): Empleados en franco para cada día.
        lista_empleados (list): Lista de empleados para poder seleccionar.
        dict_objetos (dict): Diccionario de objetos de empleados.
        turnos (dict): Diccionario con los turnos asignados de toda la semana.
        turno (str): Mañana o tarde.
        cantidad (int): Cantidad de empleados para el turno.
        
    Returns:
        turnos (dict): Diccionario con los turnos asignados de toda la semana.
    '''
     # Quito empleado turno noche de la lista de empleados
    try:
        empleado_turno_noche = turnos['Lunes']['Noche'][0]
        if empleado_turno_noche in lista_empleados:
            lista_empleados.remove(empleado_turno_noche)
    except IndexError:
        print('Aparentemente no hay un empleado asignado para el turno noche.\n'
              'Regrese al Menú Principal y asigne un empleado para el turno noche.')
        return
    
    # Quito empleado de franco de la lista de empleados
    lista = lista_nombre_hs(dict_objetos)
    lista_ordenada = sorted(lista, key=lambda x: x[1])
    # [['David', 0], ['Diego', 0], ['Juan', 0], ['Marcelo', 0], ['Matias', 0], ['Nito', 0], ['Paco', 0], ['Pocho', 0], ['Ruben', 0]]
    triada = []
    
    for num in range(3):
        if len(triada) < 3:
            # Aca tendriamos que agregar la logica para que si hay cierto empleado no pueda estar cierto otro
            triada.append(lista_ordenada[num][0])
            emp = triada[-1]
            dict_objetos[emp].actualizar_horas_trabajadas(8)
    turnos[dia][turno] = triada
    # MAS O MENOS FUNCIONA
    
    return turnos, dict_objetos
    