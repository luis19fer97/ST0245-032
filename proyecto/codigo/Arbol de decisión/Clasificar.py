from Hoja import hoja

# Este método decide donde almacenar los valores siguientes, si en una rama falsa o verdadera, hasta llegar
# a realizar una predicción

def clasificar(filas, nodo):

    if isinstance(nodo, hoja):
        return nodo.prediccion

    if nodo.pregunta.match(filas):
        return clasificar(filas, nodo.rama_verdadera)
    else:
        return clasificar(filas, nodo.rama_falsa)
