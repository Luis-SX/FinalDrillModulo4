#########   Parte 1

class Vehiculo:                                                         #clase base que representa un vehículo genérico
    def __init__(self, marca, modelo, numero_ruedas):                   #iniciamos los atributos de la clase Vehiculo
        self.marca = marca                                              #inicializamos eel atributo marca
        self.modelo = modelo                                            #inicializamos el atributo modelo
        self.numero_ruedas = numero_ruedas                              #inicializamos el atributo número de ruedas

    def __str__(self):                                                  # método que retorna en una cadena con los datos del vehículo
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas" #entrega el string "Marca , Modelo, número de ruedas"

class Automovil(Vehiculo):                                              # clase hija que hereda de la clase Vehiculo
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):    #iniciamos los aatributos de la clase Automovil que hereda tambien de la clase Vehiculo
        super().__init__(marca, modelo, numero_ruedas)                  #llamamos al constructor de la clase padre
        self.velocidad = velocidad                                      #agrega velocidad al objeto
        self.cilindrada = cilindrada                                    #agrega cilindrada al objeto

    def __str__(self):                                                    # método que retorna en una cadena con los datos del vehículo y del automóvil
        return super().__str__() + f", {self.velocidad} Km/h, {self.cilindrada} cc"  #entrega el string "Marca, Modelo, número de ruedas, velocidad, cilindrada"

#### Lista de pruebas para no escribir a cara rato ####
"""vehiculos = [ 
    Automovil("Toyota", "Yaris", 4, 120, 800), 
    Automovil("Fiat", "Palio", 4, 95, 1200), 
    Automovil("Ford", "Fiesta", 4, 125, 1500)
]"""

vehiculos = []                                                              # creamos la lista de vehiculos
for i in range(3):                                                          #Alimentamos la lista de vehículos
    print()
    marca = input(f"Datos del automóvil {i+1}\nInserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    numero_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindrada = int(input("Inserte el cilindraje en cc: "))
    vehiculos.append(Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada))    #con esto agregamos todos los detalles a la lista vehiculos

print("\nImprimiendo por pantalla los Vehículos:")  # Mostramos los datos de los vehículos guardados en la lista vehiculos
for i, vehiculo in enumerate(vehiculos, start=1):       #con el enumerate imprimimos el número de vehículo y los datos del mismo
    print(f"Datos del automóvil {i}: {vehiculo}")       #imprimimos el número de vehículo y los datos del mismo


#########                      Parte 2


class Particular(Automovil):                                                                    #clase Particular que hereda de Automovil
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puestos):    #constructor de la clase Particular
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)                   #llamamos al constructor de la clase Automovil
        self.numero_puestos = numero_puestos                                                    #agregamos el número de puestos al objeto

    def __str__(self):                                                                          #metodo para representar el objeto como cadena de texto
        return super().__str__() + f", Puestos: {self.numero_puestos}"                           #retorna el string "Marca, Modelo, número de ruedas, velocidad, cilindrada, Puestos: {self.numero_puestos}""

class Carga(Automovil):                                                                         #clase Carga que hereda de Automovil
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso_carga):        #constructor de la clase Carga
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)                   #llamamos al constructor de la clase Automovil
        self.peso_carga = peso_carga                                                            #agregamos el peso de la carga al objeto

    def __str__(self):                                                                          #metodo para representar el objeto como cadena de texto
        return super().__str__() + f", Carga: {self.peso_carga} Kg"                              #devuelvee el string "Marca, Modelo, número de ruedas, velocidad, cilindrada, Carga: {self.peso_carga} Kg"

class Bicicleta(Vehiculo):                                                                      #clase Bicicleta que hereda de Vehiculo
    def __init__(self, marca, modelo, numero_ruedas, tipo_bicicleta):                           #constructor de la clase Bicicleta
        super().__init__(marca, modelo, numero_ruedas)                                          #llamamos al constructor de la clase Automovil
        self.tipo_bicicleta = tipo_bicicleta                                                    #agregamos el tipo de bicicleta al objeto

    def __str__(self):                                                                          #metodo para representar el objeto como cadena de texto
        return super().__str__() + f", Tipo: {self.tipo_bicicleta}"                              #devuelve el string "Marca, Modelo, número de ruedas, Tipo: {self.tipo_bicicleta}"      

class Motocicleta(Bicicleta):                                                                   #clase Motocicleta que hereda de Bicicleta
    def __init__(self, marca, modelo, numero_ruedas, tipo_bicicleta, motor, cuadro, nro_radios):    #constructor de la clase Motocicleta
        super().__init__(marca, modelo, numero_ruedas, tipo_bicicleta)                          #llamamos al constructor de la clase Bicicleta
        self.motor = motor                                                                      #agregamos el motor al objeto
        self.cuadro = cuadro                                                                    #agregamos el cuadro al objeto
        self.nro_radios = nro_radios                                                            #agregamos el número de radios al objeto

    def __str__(self):                                                                          #metodo para representar el objeto como cadena de texto
        return super().__str__() + f", Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"    #devuelve el sstring "Marca, Modelo, número de ruedas, Tipo: {self.tipo_bicicleta}, Motor: {self.motor}, 
                                                                                                                    #Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"

# creamos las instancias solicitadas
particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)                                       #instancia del vehiculo particular
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)                                      #instancia del vehiculo de carga
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")                                     #instancia de la bici
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)               #instancia de la moto

# mostramos las insstancias
print()                         #dejamos una fila vacía para separar
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

# Verificar las relaciones de instancia
print()                         #dejaamos una fila vacía para separar
print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))   # imprimimos el resultado de la relación de instancia
print("Motocicleta es instancia con relación a Automovil:", isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo particular:", isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de Carga:", isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))



