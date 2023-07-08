import random
import copy

# Clase Empleado
class Empleado:
    ultimo_id = 0

    def __init__(self, nombre: str, horas=0, dias=0, vacaciones=False, disponibilidad=True, confiabilidad=None, turnos=None, franco_semanal=''):
        self.id = Empleado.generar_id()
        self.nombre = nombre
        self.horas_trabajadas = horas
        self.dias_trabajados = dias    
        self.vacaciones = vacaciones
        self.disponibilidad = disponibilidad
        self.confiabilidad = confiabilidad
        self.turnos = turnos
        self.franco_semanal = franco_semanal
    
    @classmethod
    def generar_id(Empleado):
        Empleado.ultimo_id += 1
        return Empleado.ultimo_id
     
    def obtener_id(self):
        return self.id
    
    def obtener_nombre(self):
        return self.nombre

    def __str__(self):
        return self.nombre
    
    def obtener_horas_trabajadas(self):
        return self.horas_trabajadas
    
    def actualizar_horas_trabajadas(self, horas):
        self.horas_trabajadas += horas
    
    def obtener_vacaciones(self):
        return self.vacaciones
    
    def obtener_disponibilidad(self):
        return self.disponibilidad
    
    def obtener_confiabilidad(self):
        return self.confiabilidad

    def obtener_turnos(self):
        return self.turnos

    def obtener_dias_trabajados(self):
        return self.dias_trabajados

    def asignar_franco_semanal(self, dia: str):
        self.franco_semanal = dia

    def obtener_franco_semanal(self):
        return self.franco_semanal



#------------------------------------------------------------------------------------------------------
#                                          Funciones auxiliares
#------------------------------------------------------------------------------------------------------


def crear_dict_empleados(lista: str):
    """
    Recibe una lista de nombres:str y retorna un diccionario
    con el ID como key y la instancia(objecto) como valor
    {'ID': 'Obj'}
    Quiza sea mejor tenes el nombre de cada empleado como key en vez del ID
    """
    dict_empleados = {}
    for nombre in lista:
        emp = Empleado(nombre)
        dict_empleados[emp.obtener_nombre()] = emp
    return dict_empleados

def lista_nombre_hs(diccionario):
    """
    Recibe un diccionario {'Nombre': 'Obj'} y retorna una lista de listas: [ID, Horas_trabajadas]
    La idea es que de ésta lista vayamos pickeando para otorgar el turno, la ventaja
    es que podemos ordenar la lista de listas segun hs trabajadas y seleccionar el empleado
    con menos horas asi de esta manera podemos ir equiparandolos. El empleado con menos hs
    trabajadas primero.
    """
    lista_id_hs = []
    for nombre, empleado in diccionario.items():
        lista_id_hs.append([nombre, empleado.obtener_horas_trabajadas()])
    return lista_id_hs

def quitar_empleado_noche(empleado_noche, lista_empleados_copia, DICCIONARIO_OBJECTOS, LISTA_EMPLEADOS):
    '''Quita el empleado de Turno noche de la lista de empleados y actualiza su
    atributo horas trabajadas 
    '''
    del lista_empleados_copia[empleado_noche - 1]
    nombre_empleado = LISTA_EMPLEADOS[empleado_noche - 1]
    DICCIONARIO_OBJECTOS[nombre_empleado].actualizar_horas_trabajadas(56)
    return lista_empleados_copia

def asignar_francos(SEMANA, lista_empleados_copia):
    '''
    Recibe una semana de dias y devuelve un diccionario DIA:NOMBRE
    Cuando pregunta para asignar el empleado de franco para el dia deberiamos
    mostrar la lista de empleados disponibles para elegir.
    '''
    dict_francos = {}
    for day in SEMANA:
        for count, empleado in enumerate(lista_empleados_copia, start=1):
            print('    ', count, empleado)
        emp = int(input(f'Franco para el dia: {day}. Ingrese un número.\n'))
        dict_francos[day] = lista_empleados_copia[emp - 1]
        del lista_empleados_copia[emp - 1]
    return dict_francos

def asignar_turnos(DIA, lista_empleados_copia, lista_id_hs, dict_francos):
    '''
    Recibe lista de empleados sin el de turno noche. 
    Lo primero que tenemos que hacer es quitar el empleado de franco, por lo que necesitamos el dict_francos
    Luego si puedo proceder a iterar sobre los dias de la semana
    '''
    # Esta funcion deberia ser mas simple, otorgar turnos para un dia, y luego en el Main iterar
    # sobre la semana invocando la funcion para cada dia.
        # Creo una copia de la lista para el dia, asi el proximo dia esta completa
    lista_copia = copy.deepcopy(LISTA_EMPLEADOS)
    # Quito empleado de franco
    franco = dict_francos[day]
    del lista_copia[franco]
    # SIN TERMINAR ??????????????????????????????????????????????????????????????????????????????????????????????


# CONSTANTES
SEMANA = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'] 
LISTA_EMPLEADOS = ['Juan', 'Nito1', 'Nito2', 'Pocho', 'Matias', 'Diego', 'Marcelo', 'Paco', 'David']


#------------------------------------------------------------------------------------------------------
#                                          Programa principal
#------------------------------------------------------------------------------------------------------
DICCIONARIO_OBJECTOS = crear_dict_empleados(LISTA_EMPLEADOS)
print(DICCIONARIO_OBJECTOS)
lista__ = lista_nombre_hs(DICCIONARIO_OBJECTOS)
print(lista__)
# Como interactuar con los objectos:
'''
DICCIONARIO_OBJECTOS['Pocho'].actualizar_horas_trabajadas(8)
print(DICCIONARIO_OBJECTOS['Pocho'].horas_trabajadas)
DICCIONARIO_OBJECTOS['Juan'].asignar_franco_semanal('Lunes')
print(DICCIONARIO_OBJECTOS['Juan'].obtener_franco_semanal())
'''

print(f'----------------------------------\nLista de empleados\n----------------------------------')
for count, empleado in enumerate(LISTA_EMPLEADOS, start=1):
    print('    ', count, '-', empleado)
print('----------------------------------')

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

lista_empleados_copia = copy.deepcopy(LISTA_EMPLEADOS)
lista_empleados_copia= quitar_empleado_noche(empleado_noche, lista_empleados_copia, DICCIONARIO_OBJECTOS, LISTA_EMPLEADOS)
print(DICCIONARIO_OBJECTOS['Marcelo'].horas_trabajadas)

print(f'----------------------------------\nLista de empleados sin Empleado del Turno Noche\n----------------------------------')

for count, empleado in enumerate(lista_empleados_copia, start=1):
    print('    ', count, empleado)
    
# TODO: Asignar Francos OK
# Ya tenemos la lista sin el empleado asignado para turno Noche. Ahora tenemos que ver como organizamos 
# los francos y regenerar la lista para cada dia sacando el empleado de franco.
print('Ahora asignaremos los francos para la semana:')
# Donde guardamos los datos? Puede ser un diccionario DIA:NOMBRE
# Esto deberia ser una funcion
dict_francos = asignar_francos(SEMANA, lista_empleados_copia)
print(dict_francos)

# Una vez que tenemos el diccionario de francos armado podemos proceder a asignar turnos,
# lo que deberiamos hacer es, para cada dia consultar este diccionario y quitar de la lista
# al empleado que este de franco.

# TODO: Asignar turnos
 
# Preparar la lista sin el empleado de franco del dia
# Esto lo debo hacer dentro de la funcion que itere sobre cada dia para asignar los turnos




# Escribo algo para hacer nuevo commit, probando.