import csv
import numpy as np
from registro import Registro

class ManejadorRegistro:
    def __init__(self):
        self.__registros = np.empty((30,24), dtype=Registro)

    def cargarDatos(self, archivo):
        cabecera=True
        with open(archivo) as f:
            reader = csv.reader(f,delimiter=',')
            for fila in reader:
                if cabecera:
                    cabecera=not cabecera
                else:
                    dia = int(fila[0])-1
                    hora = int(fila[1])
                    temperatura = float(fila[2])
                    humedad = float(fila[3])
                    presion = float(fila[4])
                    self.__registros[dia, hora]=Registro(temperatura, humedad, presion)
                    

    def mostrarDatos(self):
        for i in range(30):
            for j in range(24):
                registro = self.__registros[i, j]
                if registro is not None:
                    print(f"Día {i+1}, Hora {j}:")
                    print(f"Temperatura: {registro.get_temperatura()}")
                    print(f"Humedad: {registro.get_humedad()}")
                    print(f"Presión: {registro.get_presion()}")

    def mostrarMayoryMenor (self):
        max= 0.0
        min = 9999.0
        for i in range(30):
            for j in range(24):
                registro = self.__registros[i, j]
                if registro is not None and registro.get_temperatura() > max:
                    max=registro.get_temperatura()
                    maxdia=i+1; maxhora=j
                elif registro is not None and registro.get_temperatura() < min:
                    min=registro.get_temperatura()
                    mindia=i+1; minhora=j
        print(f"Valor maximo de Temperatura para el dia {maxdia}, hora {maxhora}: {max}")
        print(f"Valor minimo de Temperatura para el dia {mindia}, hora {minhora}: {min}")

        for i in range(30):
            for j in range(24):
                registro = self.__registros[i, j]
                if registro is not None and registro.get_humedad() > max:
                    max=registro.get_humedad()
                    maxdia=i+1; maxhora=j
                elif registro is not None and registro.get_humedad() < min:
                    min=registro.get_humedad()
                    mindia=i+1; minhora=j
        print(f"Valor maximo de Humedad para el dia {maxdia}, hora {maxhora}: {max}")
        print(f"Valor minimo de Humedad para el dia {mindia}, hora {minhora}: {min}")

        for i in range(30):
            for j in range(24):
                registro = self.__registros[i, j]
                if registro is not None and registro.get_presion() > max:
                    max=registro.get_presion()
                    maxdia=i+1; maxhora=j
                elif registro is not None and registro.get_presion() < min:
                    min=registro.get_presion()
                    mindia=i+1; minhora=j
        print(f"Valor maximo de Presión para el dia {maxdia}, hora {maxhora}: {max}")
        print(f"Valor minimo de Presión para el dia {mindia}, hora {minhora}: {min}")
        
    def tempMensual(self):
        promedios = []
        for hora in range(24):
            suma = 0
            i = 0
            for dia in range(30):
                registro = self.__registros[dia, hora]
                if registro is not None:
                    suma += registro.get_temperatura()
                    i += 1
            if i > 0:
                prom = suma / i
                promedios.append(prom)
            else:
                promedios.append(None)
        print("Temperatura promedio mensual por hora:")
        for hora in range(24):
            print(f"A las {hora}:00 horas: {promedios[hora]:.2f}")

    def obtenerValoresPorDia(self, dia):
        fila = self.__registros[dia-1]
        print("Hora\tTemperatura\tHumedad\tPresion")
        for hora in range(24):
            registro = fila[hora]
            if registro is not None:
                temperatura = registro.get_temperatura()
                humedad = registro.get_humedad()
                presion = registro.get_presion()
                print(f"{hora}\t{temperatura}\t\t{humedad}\t{presion}")
            else:
                print(f"{hora}\t-\t\t-\t-")