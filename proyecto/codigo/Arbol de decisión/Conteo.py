# Este método cuenta la cantidad de valores iguales que existen en una columna del data set

def conteo (filas):
    conteo = {}  # diccionario para contar la cantidad de 1 y 0 de la columna exito
    for fila in filas:
        
        exito = fila[-1] # la variable de decisión se encuentra en la última columna
        if exito not in conteo:
            conteo[exito] = 0
        conteo[exito] += 1
    return conteo