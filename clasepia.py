# Estructura de la clase <<Contacto>>

# Se importa módulo: datetime
import datetime

# Se crea la clase <<Contacto>>
class Contacto:
    def __init__(self, NICKNAME, NOMBRE, CORREO, TELEFONO, FECHANACIMIENTO, GASTO):
        # NICKNAME: Nombre a traves del cual el contacto desea ser referido
        # NOMBRE: NOmbre completo del contacto
        # CORREO: Correo electrónico del contacto
        # TELEFONO: Número telefónico del contacto
        # FECHANACIMIENTO: Fecha de nacimiento del contacto
        # GASTO: Gasto mensual del contacto
        self.NICKNAME = NICKNAME
        self.NOMBRE = NOMBRE
        self.CORREO = CORREO
        self.TELEFONO = TELEFONO
        self.FECHANACIMIENTO = FECHANACIMIENTO
        self.GASTO = GASTO