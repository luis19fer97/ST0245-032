from Hoja import hoja
from Nodo_decision import nodo_decision
from Division import division
from Mejor_division import mejor_division

# En este método se crea el arbol mediante recursión, se parte el dataset en un atributo único, se calcula 
# el info gain y con la pregunta que produce el gain mayor se procede a crear una rama


def construir_arbol(filas,cabeceras):

    gain, pregunta = mejor_division(filas,cabeceras)

    # si no hay gain no se debe realizar más particiones
    if gain == 0:
        return hoja(filas)

    # Con este llamado es posible obtener una característica importante para la división
    filas_verdaderas, filas_falsas = division(filas, pregunta)

    # Llamado recursivo para la construcción de las ramas
    rama_verdadera = construir_arbol(filas_verdaderas,cabeceras)

    # Llamado recursivo para la construcción de las ramas
    rama_falsa = construir_arbol(filas_falsas,cabeceras)

    # Devolver un nodo con la pregunta, este tiene la mejor característica y valor para preguntar en este punto
    return nodo_decision(pregunta, rama_verdadera, rama_falsa)
