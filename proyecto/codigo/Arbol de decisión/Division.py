# Permite subdividir los datos en aquellos que sí cumplen con la pregunta y los que no, esto con 
# el fin de crear las ramas del árbol


def division(filas, pregunta):

    filas_verdaderas, filas_falsas = [], []
    for row in filas:
        if pregunta.match(row):
            filas_verdaderas.append(row)
        else:
            filas_falsas.append(row)
    return filas_verdaderas, filas_falsas
