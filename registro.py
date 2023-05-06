class Registro:
    __temperatura=float
    __humedad=float
    __presion=float
    def __init__(self, temperatura, humedad, presion):
        self.__temperatura= temperatura
        self.__humedad= humedad
        self.__presion=presion
    
    def get_temperatura(self):
        return self.__temperatura

    def get_humedad(self):
        return self.__humedad

    def get_presion(self):
        return self.__presion

