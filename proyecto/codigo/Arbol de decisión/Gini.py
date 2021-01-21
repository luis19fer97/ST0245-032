from Conteo import conteo
# En este método se calcula la impureza de gini que existe en una columna, la impuerza de Gini
# es una medida de la frecuencia con la que un elemento elegido 
# aleatoriamente del conjunto se etiquetaría incorrectamente

def gini(filas):

    conteos = conteo(filas)
    impureza = 1
    for lbl in conteos:
        prueba = conteos[lbl] / float(len(filas))
        impureza -= prueba**2
    return impureza