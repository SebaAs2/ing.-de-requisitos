class Ejercicio2_7:

    "atributos"
    
    def __init__(self, litrosProductos, precioPorGalon):
        self.__litrosProductos = litrosProductos
        self.__precioPorGalon = precioPorGalon
        self.__litrosPorGalon = 3.785
        
    "metodos"
    
    def convertirAGalones (self):
        return self.__litrosProductos / self.__litrosPorGalon
    
    def calcularPrecioTotal(self):
        galones = self.convertirAGalones
        return galones * self.__precioPorGalon
    