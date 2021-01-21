from Conteo import conteo

# Este método permite conocer la cantidad de filas que terminan en una hoja siguiendo una clasificación
# específica

class hoja:
    def __init__(self, filas):
        self.prediccion = conteo(filas)