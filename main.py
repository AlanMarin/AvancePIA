# Se importa modulo para trabajar con el sistema operativo
import os
# Se importa módulo para trabajar con archivos csv
import csv
# Se importa módulo para trabajar con expresiones regulares
import re
# Se importa módulo para trabajar con datos tipo datetime
import datetime

captura = ""
Contactos = []
LimpiarPantalla = lambda: os.system('cls')
nickname = ""
nombre = ""
correo = ""
telefono = ""
fechaNac = ""
gasto = ""

# Acceso de datos a la clase <<Contacto>>
# Se importa clase <<Contacto>> de: clasepia
from clasepia import Contacto


# Función para validar los datos
def pregunta(_formato, _pregunta="Datos: "):
    # Se especifica que "_captura" es global
    global _captura
    while True:
        _dato = input(_pregunta)
        valido = re.search(_formato, _dato)
        if (valido):
            _captura = _dato
            break
        else:
            print("Dato no válido. Intente de nuevo")


# Función para convertir cadena a datetime
def cadenafecha(_dtDato):
    return datetime.datetime(
        int(_dtDato[0:4]), int(_dtDato[5:7]), int(_dtDato[-2:]))


# Función para captura de datos
def ingresoDatos():
    global nickname
    global nombre
    global correo
    global telefono
    global fechaNac
    global gasto
    # Se pide el nickname
    pregunta("^[A-Z ]{1,15}$", "Ingrese nickname en mayusculas: ")
    nickname = _captura
    # Se pide el nombre completo
    pregunta("^[A-Z ]{1,35}$", "Ingrese nombre completo en mayusculas: ")
    nombre = _captura
    # Se pide el correo electrónico
    pregunta("[\w\.-]+@[\w\.-]+(\.[\w]+)+", "Ingrese correo electronico: ")
    correo = _captura
    # Se pide el número telefónico
    pregunta("^(\d{2} \d{4}-\d{4})",
             "Ingrese numero telefonico (99 9999-9999): ")
    telefono = _captura
    # Se pide la fecha de nacimiento
    pregunta("^[0-9]{4}-[0-9]{2}-[0-9]{2}",
             "Ingrese fecha de nacimiento (YYYY-MM-DD): ")
    fechaNac = _captura
    # Se pide el gasto mensual
    #pregunta("^([0-9]){1,7}$", "Ingrese gasto mensual: ")
    pregunta("^[0-9]+(\.[0-9]{1,2})?$", "Ingrese gasto mensual: ")
    gasto = _captura

    Contactos.append(
        Contacto(nickname, nombre, correo, telefono, fechaNac, gasto))
    ruta = os.path.abspath(os.getcwd())
    archivo_trabajo = ruta + "\\contactos_mobil.csv"
    archivo_respaldo = ruta + "\\contactos_mobil.bak"

    # Se determina si el archivo de trabajo ya existe
    if os.path.exists(archivo_trabajo):
        # Si el archivo existe, entonces verifica si hay respaldo y lo borra
        if os.path.exists(archivo_respaldo):
            os.remove(archivo_respaldo)

        # Establece el achivo de datos, como respaldo
        os.rename(archivo_trabajo, archivo_respaldo)

    # Se genera archivo csv
    f = open(archivo_trabajo, "w+")

    # Escritura de encabezados de archivo csv
    f.write("USUARIO|NOMBRE|CORREO|TELEFONO|FECHANACIMIENYO|GASTOS\n")
    # Se escribe en el archivo csv, a partir de la lista de objetos
    for elemento in Contactos:
        f.write(
            f'{elemento.NICKNAME}|{elemento.NOMBRE}|{elemento.CORREO}|{elemento.TELEFONO}|{elemento.FECHANACIMIENTO}|{elemento.GASTO}\n'
        )

    return (nickname, nombre, correo, telefono, fechaNac, gasto)


# Función para imprimir contactos registrados
def mostrarContactos():
    # with genera bloque de código con referencia
    # Cuando se escriba archivo_csv se trabajara con el contenido del archivo: contactos_mobil.csv
    with open('contactos_mobil.csv') as archivo_csv:
        # ----------print(nickname,nombre,correo,telefono,fechaNac,gasto)
        # Se habilita objeto que permitira leer de manera secuencial el contenido del archivo csv
        # archivo_csv es el puente entre el programa y el archivo
        # lector_csv es el flujo de datos entre el programa y el archivo
        lector_csv = csv.reader(archivo_csv, delimiter='|')

        # Contador de lineas
        contador_lineas = 0

        # Lee secuencialmente el archivo usando el flujo de datos (lector_csv)
        # La linea se coloca en el elemento linea
        # Al trabajar con <<linea_datos>> se trabaja con la linea del archivo
        # for dejará de leer cuando los datos del archivo se hayan terminado
        for linea_datos in lector_csv:
            # Si el contador es mayor a cero: muestra, dato por dato, los datos obtenidos en linea_datos
            if contador_lineas > 0:
                print(f'\tNICKNAME: {linea_datos[0]}.')
                print(f'\tNOMBRE: {linea_datos[1]}.')
                print(f'\tCORREP: {linea_datos[2]}.')
                print(f'\tTELEFONO: {linea_datos[3]}.')
                print(f'\tFECHA DE NACIMIENTO: {linea_datos[4]}.')
                print(f'\tGASTO: {linea_datos[5]}.')
                print(f'\t----------------------------------------')
            # Se incrementa el número de lineas sin importar la condición
            contador_lineas += 1


# Función para validar la existencia del número telefónico buscado
def buscarContacto(TelefonoBuscar):
    contador = -1
    indice_retorno = -1
    for Contacto in Contactos:
        contador += 1
        if (Contacto.TELEFONO == TelefonoBuscar):
            indice_retorno = contador
            break
    return indice_retorno


# Función para validador de opciones
def RegEx(_txt, _regex):
    coincidencia = re.match(_regex, _txt)
    return bool(coincidencia)


# Funcion que ejecuta el menú, se repite hasta que el usuario ingrese "0"
def principal():
    while (True):
        LimpiarPantalla()
        print("LISTA DE OPCIONES")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida, "^[123450]{1}$"):
            if opcion_elegida == "0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break

            if opcion_elegida == "1":
                print("Llamar procedimiento para la acción")
                ingresoDatos()

            if opcion_elegida == "2":
                print("Llamar procedimiento para la acción")
                VariableTelefono = input(
                    "inserte el numero del contacto formato 99 9999-9999: ")
                indice_obtenido = buscarContacto(VariableTelefono)
                if indice_obtenido == -1:
                    print("No se encontró el objeto")
                else:
                    print(Contactos[indice_obtenido].TELEFONO)
                    print(Contactos[indice_obtenido].NOMBRE)
                    print(Contactos[indice_obtenido].CORREO)
            if opcion_elegida == "3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida == "4":
                print("Llamar procedimiento para la acción")
                mostrarContactos()
            if opcion_elegida == "5":
                print("Llamar procedimiento para la acción")
            input("Pulse enter para continuar...")
        else:
            print("Respuesta no válida.")
            input("Pulse enter para contunuar...")


# Se guarda en la variable la ruta absoluta, del directorio actual de trabajo (cwd)
ruta = os.path.abspath(os.getcwd())
archivo_trabajo = ruta + "\\contactos_mobil.csv"
archivo_respaldo = ruta + "\\contactos_mobil.bak"

# Se determina si el archivo de trabajo ya existe
if os.path.exists(archivo_trabajo):
    # Si el archivo existe, entonces verifica si hay respaldo y lo borra
    if os.path.exists(archivo_respaldo):
        os.remove(archivo_respaldo)

    # Establece el achivo de datos, como respaldo
    os.rename(archivo_trabajo, archivo_respaldo)

# Genera el archivo CSV
f = open(archivo_trabajo, "w+")
# Se escriben los encabezados del archivo csv
f.write("NICKNAME|NOMBRE|CORREO|NUMERO|FECHANACIMIENYO|GASTOS\n")
# Se escribe en el csv, a partir de la lista de objetos
for elemento in Contactos:
    f.write(
        f'{elemento.NICKNAME}|{elemento.NOMBRE}|{elemento.CORREO}|{elemento.TELEFONO}|{elemento.FECHANACIMIENTO}|{elemento.GASTO}\n'
    )

# Se cierra el archivo csv
f.close()

principal()
