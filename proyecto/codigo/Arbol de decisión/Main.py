#Importar las librerías necesarias
import pandas as pd
import numpy as np
from pprint import pprint
from time import time

#Importar los módulos necesarios
from Carga_datos import carga_datos
from Arbol import construir_arbol
from Dibujar_arbol import print_tree
from Clasificar import clasificar
from Exactitud import Exactitud



# Cargar los datos de entrenamiento y prueba
data_array,data_array_test,cabeceras = carga_datos("Datos/train.csv","Datos/test.csv")


if __name__ == '__main__':

    tiempo_inicial = time()

    arbol = construir_arbol(data_array,cabeceras)
    Exactitud(data_array_test,arbol)

    tiempo_final = time()
    tiempo_ejecución = tiempo_final -tiempo_inicial

    print("Tarda " + str(round(tiempo_ejecución,2)) +" segundos en ejecutar")
    print_tree(arbol)