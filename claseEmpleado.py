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
    
