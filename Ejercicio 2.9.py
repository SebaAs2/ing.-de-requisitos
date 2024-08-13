class Ejercicio2_9:
    
    "atributos"
    def __init__(self, horasTrabajadas, pagoPorHoras):
        self.__horasTrabajadas = horasTrabajadas
        self.__pagoPorHora = pagoPorHoras
        
    "metodos"
    
    def calcularSalario(self):
        return self.__horasTrabajadas * self.__pagoPorHora