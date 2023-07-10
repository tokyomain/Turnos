from claseEmpleado import *

# TODO: Funciones del Menu principal
    # 1- Ver Lista Empleados > Simplemente imprimir la lista de todos los empleados
    # 2- Asignar turno Noche > OK
    # 3- Ver Empleado turno Noche > devolver el empleado en cuestion.
    # 4- Asignar Francos > OK Ver
    # 5- Ver turnos asignados > 
    # 6- Asignar turnos
    # 7- Ver turnos asignados
    # 8- Asignar vacaciones
    # 9- Ver vacaciones > devolver el empleado con vacaciones para esta semana.

def crear_dict_empleados(lista: str):
    """
    Recibe una lista de nombres:str y retorna un diccionario
    con el Nombre como key y Objecto como valor > {'Nombre': 'Obj'}
    """
    d = {}
    for nombre in lista:
        emp = Empleado(nombre)
        d[emp.__str__()] = emp
    return d

def lista_nombre_hs(diccionario):
    """
    Recibe un diccionario {'Nombre': 'Obj'} y retorna una lista de listas: [Nombre, Horas_trabajadas]
    """
    lista = []
    for nombre, empleado in diccionario.items():
        lista.append([nombre, empleado.obtener_horas_trabajadas()])
    return lista

def asignar_empleado_noche(empleado_noche, lista_empleados_copia, DICCIONARIO_OBJETOS, LISTA_EMPLEADOS):
    '''Quita el empleado de Turno noche de la lista de empleados y actualiza su
    atributo horas trabajadas 
    VER: En esta funcion creo que no es necesario como parametro la "lista_empleados_copia", puedo modificar
    directamente la LISTA_EMPLEADOS ya que los cambios solo tendran alcance local, no modificara la lista
    original por fuera de esta funcion, si sucederá que devolvere esta lista, pero eso lo puedo guardar en una
    nueva variable.
    '''
    while True:
        try:
            empleado_noche = int(input('Quien es el empleado para el turno Noche? Ingrese un número (1-9)\n'))
            if not (1 <= empleado_noche <= 9):
                print(f'Por favor, ingrese una respuesta válida. "{empleado_noche}" no es una respuesta válida.')
            else:
                print(f'El empleado No. {empleado_noche} - "{LISTA_EMPLEADOS[empleado_noche-1]}" está asignado para el turno Noche.')
                break
        except ValueError:
            print('Por favor, ingrese un número válido.')
            
    del lista_empleados_copia[empleado_noche - 1]
    nombre_empleado = LISTA_EMPLEADOS[empleado_noche - 1]
    DICCIONARIO_OBJETOS[nombre_empleado].actualizar_horas_trabajadas(56)
    return lista_empleados_copia

def asignar_francos(SEMANA, lista_empleados):
    '''
    Recibe una semana de dias y devuelve un diccionario > {'Dia': 'Nombre'}
    Cuando pregunta para asignar el empleado de franco para el dia deberiamos
    mostrar la lista de empleados disponibles para elegir.
    '''
    d = {}
    print('Ahora asignaremos los francos para la semana:')
    for dia in SEMANA:
        for count, empleado in enumerate(lista_empleados, start=1):
            print('    ', count, empleado)
        emp = int(input(f'Franco para el dia: {dia}. \nIngrese un número >'))
        d[dia] = lista_empleados[emp - 1]
        # Si aca uso pop me devuelve el empleado borrado
        # EX: ultima_fruta = frutas.pop()
        franco = lista_empleados.pop(emp -1 )
        print(f'El empleado de franco para el dia {dia} es: {franco}')
        # del lista_empleados[emp - 1]
    return d

# TODO:
'''def asignar_turnos(DIA, lista_empleados_copia, lista_id_hs, dict_francos):
    
    Recibe lista de empleados sin el de turno noche. 
    Lo primero que tenemos que hacer es quitar el empleado de franco, por lo que necesitamos el dict_francos
    Luego si puedo proceder a iterar sobre los dias de la semana
    
    # Esta funcion deberia ser mas simple, otorgar turnos para un dia, y luego en el Main iterar
    # sobre la semana invocando la funcion para cada dia.
        # Creo una copia de la lista para el dia, asi el proximo dia esta completa
    lista_copia = copy.deepcopy(LISTA_EMPLEADOS)
    # Quito empleado de franco
    franco = dict_francos[day]
    del lista_copia[franco]'''
   