# Pasos del proyecto

# 1) Definir Lista de empleados
    # Hay que pensar si nos conviene hacer OOP o funcional. Que ventajas nos da?
# 2) Definir turnos
    # Mañana, Tarde, Noche
    # Ver cuando turnos son cortados.
# 3) Definir periodo de turnos a asignar: ie semanal, mensual
    # Semanal en principio
# 4) Base de datos
    # Ver Postgresql
# 5) Condiciones
    # Como es la cantidad de empleados segun dia. Fines de semana entiendo que se necesitan mas playeros que los dias semanales
    # Mismas horas trabajadas
    # Francos
    # Vacaciones
    # Que empleados no van juntos. Sistema de confiabilidad
# 6) Asignar
    # Aca vamos a tener por un lado la lista de empleados y por otro una determinada cantidad
    # de turnos. 
# 7) Testing


import random
import copy
from datetime import datetime, timedelta, time

#//////////////////////////////////////////////////////////////////////////////////////////////////////


class Empleado:
    ultimo_id = 0

    def __init__(self, nombre: str, horas=0, dias=0, vacaciones=False, disponibilidad=True, confiabilidad=None, turnos=None, franco_semanal=None):
        self.id = Empleado.generar_id()
        self.nombre = nombre
        self.horas_trabajadas = horas
        self.dias_trabajados = dias    
        self.vacaciones = vacaciones
        self.disponibilidad = disponibilidad
        self.confiabilidad = confiabilidad
        self.turnos = turnos
        self.franco_semanal = False
    
    @classmethod
    def generar_id(Empleado):
        Empleado.ultimo_id += 1
        return Empleado.ultimo_id
     
    def obtener_id(self):
        return self.id
    
    def obtener_nombre(self):
        return self.nombre

    def __str__(self):
        return f"--------------------------\nEmpleado ID: {self.id} \nNombre: {self.nombre} \nHoras Trabajadas: {self.horas_trabajadas} \nDias Trabajados: {self.dias_trabajados}\n--------------------------"
    
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

    def asignar_franco_semanal(self):
        self.asignar_franco_semanal = True

    def tiene_franco_semanal(self):
        return self.tiene_franco_semanal
    


#//////////////////////////////////////////////////////////////////////////////////////////////////////

semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'] 
lista_empleados = ['juan', 'nito1', 'nito2', 'pocho', 'matias', 'diego', 'marcelo', 'paco', 'david']

# Crear una instancia de Empleado para cada nombre en la lista y almacenarlas en un diccionario
# Esto tiene que ser una funcion:
    # def CrearEmpleado(lista: str) > (dict: ID:Instancia)

def crear_dict_empleados(lista: str):
    """
    Recibe una lista de nombres:str y retorna un diccionario
    con el ID como key y la instancia(objecto) como valor"""

    dict_empleados = {}
    for nombre in lista:
        emp = Empleado(nombre)
        dict_empleados[emp.obtener_id()] = emp
    return dict_empleados
    
def lista_id_hs(diccionario):
    """
    Recibe un diccionario y retorna una lista de tuplas (ID, Horas_trabajadas)
    [ La idea es que de ésta lista vayamos pickeando para otorgar el turno ]
    """

    lista_id_hs = []
    for id, empleado in diccionario.items():
        tupla = (id, empleado.obtener_horas_trabajadas())
        lista_id_hs.append(tupla)
    return lista_id_hs



#//////////////////////////////////////////////////////////////////////////////////////////////////////
# TESTING / TESTING / TESTING / TESTING / TESTING / TESTING /  
#//////////////////////////////////////////////////////////////////////////////////////////////////////

diccionario = crear_dict_empleados(lista_empleados)
lista_id_hs = lista_id_hs(diccionario)
print(lista_id_hs)
print(diccionario)
empleado = diccionario[2]
empleado.actualizar_horas_trabajadas(10)
empleado.actualizar_horas_trabajadas(10)
empleado.actualizar_horas_trabajadas(8)

print(diccionario[2])
# Funcion otorgar_turnos: recibe una semana y una lista de objectos de empleados
# retorna semana con turnos mañana y tarde otorgados VER


'''
# Una vez tengo esta lista puedo empezar a repartir turnos
elegidos = set()
turno_mañana = []

for index in range(len(lista_emp_id_hs)):
    if len(turno_mañana) >= 3:
        break
    if index in elegidos:
        continue
    turno_mañana.append(lista_emp_id_hs[index][0])
    elegidos.add(index)

    empleado_id = lista_emp_id_hs[index][0]
    horas_trabajadas = 8 
    empleado = dict_empleados.get(empleado_id)
    if empleado:
        empleado.actualizar_horas_trabajadas(horas_trabajadas)

    # Actualizar horas trabajadas en lista_emp_id_hs
    lista_emp_id_hs[index][1] = empleado.obtener_horas_trabajadas()
    
print(turno_mañana)
print(f"--------------------------\nLista_emp_id_hs:\n{lista_emp_id_hs}")
print(elegidos)

'''
        
        

# Pasos:
    # 1) Conseguir la semana que quiero.
    # 2) Chequear la lista de empleados a distribuir
    # 3) Distribuir turnos equitativamente.
        # 4) Generar sistema para seleccionar empleado:
            # Podemos pensar en generar una estructura donde tengamos dos datos para cada empleado
            # ..por un lado el ID, y por otro la cantidad de horas trabajadas. DONE!

# Esta lista deberia ser creada a partir de los objectos. DONE
# Seguramente deberia iterar sobre el diccionario directamente y no crear un nueva lista
#lista_emp_id_hs = [[1, 8], [2, 8], [3, 16], [4, 24], [5, 19], [6, 12],  [7, 12],  [8, 32],  [9, 20]]
#lista_ordenada = sorted(lista_emp_id_hs, key=lambda x: x[1])
#print(f"--------------------------\nLista Ordenada:\n{lista_ordenada}")
# Output: [[1, 8], [2, 8], [6, 12], [7, 12], [3, 16], [5, 19], [9, 20], [4, 24], [8, 32]] Ordenada segun hs trabajadas, el que menos primero.
# De la lista_ordenada voy tomando el empleado en el indice 0 y luego actualizo su numero de hs trabajadas.

# Para asignar los turnos, mi idea es hacerlo dia a dia.
# Establecer el empleado de Turno Noche asi lo borramos de las opciones.
# Establecer el franco para cada empleado.
# Generar una lista para el dia con los empleados disponibles o directamente podemos de antemano 
# ..ortorgarle franco, noche, vacaciones, disponibilidad en los atributos de empleado.
# ..a la hora de repartir chequear los atributos y a partir de ahi generar una lista para el dia.
# Para el Lunes, repartir Turno Mañana y Turno Tarde. 
    # La lista que necesitamos es : [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0],  [7, 0],  [8, 0],  [9, 0]]
    # A medida que vamos otorgando turno actualizar las horas trabajadas.
    # ..ej(lista_ordenada): [[4, 0], [5, 0], [6, 0],  [7, 0],  [8, 0],  [9, 0], [1, 8], [2, 8], [3, 8]]
