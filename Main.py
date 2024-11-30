from Vehiculo import *   #importamos todo desde vehiculo
import csv              #importamos la función CSV
import ast              #importamos la funccion ast para convertir strings a diccionarios

def guardar_datos_csv(vehiculos, nombre_archivo):           #creamoss la función para guardar los datos en CSV, recibiendo una lista de vehículos y el nombre del archivo
    try:                                                    #insertamos un try para manejar posibles errores
        with open(nombre_archivo, 'w', newline='') as archivo:  #abrimos el archivo en modo escritura y añadimos una nueva línea
            archivo_csv = csv.writer(archivo)                   #creamos un objeto csv.writer para escribir en el archivo
            for vehiculo in vehiculos:                          #iteramos sobre los vehículos
                archivo_csv.writerow([vehiculo.__class__, vehiculo.__dict__])   #escribimos cada vehículo en una línea separada
    except Exception as e:                                      #en caso de error
        print(f"Error al guardar los datos: {e}")               #imprimimos el error al guardar los datos


vehiculos = [particular, carga, bicicleta, motocicleta]         #creamos una lista de vehículos con las insstancias creadas en vehiculo
guardar_datos_csv(vehiculos, "vehiculos.csv")                   #llamamos la función para guardar los datos en CSV

def leer_datos_csv(nombre_archivo):                             #creamos la función para leer los datos desde el archivo CSV
    vehiculos = {"Particular": [], "Carga": [], "Bicicleta": [], "Motocicleta": []} #creamos un diccionario para almacenar los vehículos leidos separados por clase y datos
    try:                                                        #ponemos un try para manejar posibles errores
        with open(nombre_archivo, 'r') as archivo:              #abrimos el archivo en modo lectura
            archivo_csv = csv.reader(archivo)                   #creamos un objeto csv.reader para leer el archivo y el resultado lo guardamos en archivo_csv
            for vehiculo in archivo_csv:                        #iteramos sobre cada línea del archivo
                clase = vehiculo[0].split("'")[1].split('.')[-1]    #obtenemos la clase del vehículo seprando los valores y extraemos el último elemento (clase)
                datos = ast.literal_eval(vehiculo[1])               #convertimos el string de datos a un diccionario utilizando ast.literal_eval
                vehiculos[clase].append(datos)                      #agregamos el vehículo al diccionario correspondiente según la clase
    except Exception as e:                                          #y en caso de error
        print(f"Error al leer los datos: {e}")                      #imprimimos el error al leer los datos
    return vehiculos                                            #devolvemos el diccionario con los vehículos leidos separados por clase y datos


vehiculos_leidos = leer_datos_csv("vehiculos.csv")              #llamamos la función para leer los datos desde CSV y almacenamos los vehículos leidos en vehiculos_leidos
for tipo, lista_vehiculos in vehiculos_leidos.items():          #iteramos sobre cada tipo de vehiculo y sus vehículos
    print()                                 # Separador para cada tipo de vehiculo
    print(f"Lista de Vehiculos {tipo}")                         #imprimimos el nombre del tipo de vehiculo
    for vehiculo in lista_vehiculos:                            #iteramos sobre cada vehículo
        print(vehiculo)                                         #imprimimos el vehículo


