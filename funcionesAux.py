from claseEmpleado import *

# TODO: Podriamos separar entre funciones para crear estructuras y 
# ..funciones de acciones. ANALIZAR
# TODO: Funciones del Menu principal
    # 1- Ver Lista Empleados > Simplemente imprimir la lista de todos los empleados
    # 2- Asignar turno Noche > OK
    # 3- Ver Empleado turno Noche > devolver el empleado en cuestion.
    # 4- Asignar Francos > OK Ver
    # 5- Ver Francos asignados > 
    # 6- Asignar turnos
    # 7- Ver turnos asignados
    # 8- Asignar vacaciones
    # 9- Ver vacaciones > devolver el empleado con vacaciones para esta semana.

def crear_dict_empleados(lista: str):
    '''
    Recibe una lista de nombres:str y retorna un diccionario
    con el Nombre como key y Objecto como valor > {'Nombre': 'Obj'}
    '''
    d = {}
    for nombre in lista:
        emp = Empleado(nombre)
        d[emp.__str__()] = emp
    return d

def lista_nombre_hs(diccionario):
    ''' 
    Recibe un diccionario {'Nombre': 'Obj'} y retorna una lista de listas: [Nombre, Horas_trabajadas]
    '''
    lista = []
    for nombre, empleado in diccionario.items():
        lista.append([nombre, empleado.obtener_horas_trabajadas()])
    return lista

def ver_lista_empleados(LISTA_EMPLEADOS):
    '''
    Recibe una lista de empleados e imprime la lista compleata de empleados.
    '''
    print(f'----------------------------------\n        Lista de empleados\n----------------------------------')
    for count, empleado in enumerate(LISTA_EMPLEADOS, start=1):
        print('    ', count, '-', empleado)
    print('----------------------------------')
    

def asignar_empleado_noche(d, LISTA_EMPLEADOS, turnos):
    '''Asigna empleado al turno noche, actualiza TURNOS para el empleado Noche
    y actualiza sus atributos de horas trabajadas.
    '''
    print('Seleccione un empleado de la lista para asignarlo al Turno Noche > ')
    ver_lista_empleados(LISTA_EMPLEADOS)
    while True:
        try:
            empleado_noche = int(input('Selecccione un empleado para el turno Noche? Ingrese un número (1-9) > '))
            if not (1 <= empleado_noche <= 9):
                print(f'Por favor, ingrese una respuesta válida. "{empleado_noche}" no es una respuesta válida.')
            else:
                print(f'El empleado No. {empleado_noche} - "{LISTA_EMPLEADOS[empleado_noche-1]}" está asignado para el turno Noche.')
                break
        except ValueError:
            print('Por favor, ingrese un número válido.')
            
    nombre_empleado = LISTA_EMPLEADOS[empleado_noche - 1]
        
    for dia in turnos.keys():
        turnos[dia]['Noche'].append(nombre_empleado)
    d[nombre_empleado].actualizar_horas_trabajadas(56)
    return turnos

def reemplazar_empleado_noche(d, LISTA_EMPLEADOS, turnos):
    '''
    Reemplaza el empleado asignado para el turno noche.'''

    print('Seleccione un empleado de la lista para reasignar el Turno Noche > ')
    ver_lista_empleados(LISTA_EMPLEADOS)
    while True:
        try:
            empleado_noche = int(input('Selecccione un empleado para reemplazar al empleado existente? Ingrese un número (1-9) > '))
            if not (1 <= empleado_noche <= 9):
                print(f'Por favor, ingrese una respuesta válida. "{empleado_noche}" no es una respuesta válida.')
            else:
                print(f'El empleado No. {empleado_noche} - "{LISTA_EMPLEADOS[empleado_noche-1]}" está asignado para el turno Noche.')
                break
        except ValueError:
            print('Por favor, ingrese un número válido.')
            
    nombre_empleado = LISTA_EMPLEADOS[empleado_noche - 1]
        
    for dia in turnos.keys():
        turnos[dia]['Noche'][0] = nombre_empleado
    d[nombre_empleado].actualizar_horas_trabajadas(56)
    return turnos

def ver_empleado_noche(turnos):
    '''
    Imprime en consola el empleado asignado para el turno Noche de toda la semana
    '''
    try:
        if len(turnos['Lunes']['Noche'][0]) > 0:
            empleado_noche = turnos['Lunes']['Noche'][0]
            print(f'El empleado asignado a turno Noche es: {empleado_noche}')
    except IndexError:
        print('No hay empleado asignado para el turno Noche.')

def asignar_francos(SEMANA, LISTA_EMPLEADOS, dict_objetos, francos, turnos):
    '''
    Recibe una semana, lista de empleados, diccionario con objectos, diccionario
    francos y diccionario turnos.
    Devuelve el diccionario francos con los datos actualizados > {'Dia': 'Nombre'}.
    Cuando pregunta para asignar el empleado de franco para el dia deberiamos
    mostrar la lista de empleados disponibles para elegir.
    VER: Mas o menos funciona. Ver cuando se ingresan caracteres no deseados.
    '''
    # Primero debo quitar de la lista al empleado del turno noche.
    try:
        empleado_turno_noche = turnos['Lunes']['Noche'][0]
    except IndexError:
        print('Aparentemente no hay un empleado asignado para el turno noche.\n'
              'Regrese al Menú Principal y asigne un empleado para el turno noche.')
        return
    LISTA_EMPLEADOS.remove(empleado_turno_noche)
    print('Ahora asignaremos los francos para la semana:')
    flag = True
    while flag == True: 
        for dia in SEMANA:
            if len(LISTA_EMPLEADOS) > 0:
                print('----------------------------------')
                for count, empleado in enumerate(LISTA_EMPLEADOS, start=1):
                    print('    ', count, empleado)
                print('----------------------------------')
                emp = input(f'Asignar franco para el dia: {dia}.\n' 
                            'Seleccione un número de empleado y presione "Enter" o '
                            'presione "c(continuar) + Enter" si no quiere otorgar franco para este dia > ')
                if emp == 'c' or emp == 'C':
                    continue
                else:
                    emp = int(emp)
                    francos[dia].append(LISTA_EMPLEADOS[emp - 1])
                    franco = LISTA_EMPLEADOS.pop(emp -1 )
                    print(f'El empleado de franco para el dia {dia} es: {franco}')
                    continue
            flag = False
    return francos


def ver_francos_asignados(francos):
    print(f'Francos para cada día:')
    for dia, empleados in francos.items():
        if len(empleados) > 0:
            print(f'{dia}: ', end='')
            for i, empleado in enumerate(empleados):
                if i > 0:
                    print(' - ', end='')
                print(empleado, end='')
            print()

# TODO:
'''def asignar_turnos(DIA, lista_id_hs, dict_francos, DICCIONARIO_OBJETOS):
    
    Recibe lista de empleados, un dia, diccionario con francos, y el diccionario 
    con objetos de la clase empleado.
    Lo primero que tenemos que hacer es quitar el empleado de turno noche y el 
    empleado de franco para el dia.
    
    # Esta funcion deberia ser mas simple, otorgar turnos para un dia, y luego en el Main iterar
    # sobre la semana invocando la funcion para cada dia.
        # Creo una copia de la lista para el dia, asi el proximo dia esta completa (no es necesario
        ya que si modifico la lista en la funcion solo tendra alcance local y no se
        modificara la lista original. CHEQUEAR)
    lista_copia = copy.deepcopy(LISTA_EMPLEADOS)
    # Quito empleado de franco
    franco = dict_francos[day]
    del lista_copia[franco]'''