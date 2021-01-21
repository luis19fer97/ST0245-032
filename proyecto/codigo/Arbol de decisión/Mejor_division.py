from Gini import gini
from Preguntas import pregunta
from Division import division
from Info_gain import info_gain

# En este método se ncuentra la mejor pregunta para realizar iterando entre cada característica, 
# su valor y calculando el info gain, para posteriormente separar el data set en aquellos 
# estudiantes que cumplen y los que no

def mejor_division(filas,cabeceras):

    mejor_gain = 0  
    mejor_pregunta = None  
    incertidumbre = gini(filas)
    caracteristicas = len(filas[0]) - 1  

    for col in range(caracteristicas):  

        valores = set([fila[col] for fila in filas])  

        for val in valores:  

            preg = pregunta(col, val, cabeceras)

            
            filas_verdaderas, filas_falsas = division(filas, preg)

            
            
            if len(filas_verdaderas) == 0 or len(filas_falsas) == 0:
                continue

            
            gain = info_gain(filas_verdaderas, filas_falsas, incertidumbre)

            if gain >= mejor_gain:
                mejor_gain, mejor_pregunta = gain, preg

    return mejor_gain, mejor_pregunta
