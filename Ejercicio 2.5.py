class Ejercicio2_5:
    
    "atributos"
    A = ""
    B = "" 
    C = ""
    
    "metodos"
    
    def CalcularAreaTotal(self):
        AreaTriangulo = (self.A + self.B)/2
        AreaRectangulo = self.A + self.C
        AreaTotal = AreaTriangulo + AreaRectangulo
        return AreaTotal