from Tipo_dato import es_numero

class pregunta:
    # En esta clase se generan las preguntas que ayudan a partir el data set
    # estas preguntas surgen del information gain, pues es este quien dice cuales son las variables realmente
    # importates, la clase guarda una columna con los valores y el item para realizar la pregunta
    # el método comparar realiza la comparación validando el tipo de dato, numérico o string, para poder 
    # e criterio de comparación indicado >= para número, == para string

    def __init__(self, columna, valor, cabeceras):
        self.columna = columna
        self.valor = valor
        self.cabeceras = cabeceras

    def match(self, ejemplo):
        val = ejemplo[self.columna]
        if es_numero(val):
            if self.valor == '':
                return float(val) >= 0
            return float(val) >= float(self.valor)
        else:
            return val == self.valor

    def __repr__(self):
        condicion = "=="
        if es_numero(self.valor):
            condicion = ">="
        return "Is %s %s %s?" % (
            self.cabeceras[self.columna], condicion, str(self.valor))
