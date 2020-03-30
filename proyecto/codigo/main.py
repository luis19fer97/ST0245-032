import sys
from time import time
from Buscar import Buscar
from Borrar import Borrar
from Insertar import Insertar
from Acceder import Acceder

#Inicializar el tiempo de ejecución para leer los datos
tiempo_inicial = time()

data_array = []
estudiante = []

#Cargar el archivo de datos
archivo = open("Datos/0_train_balanced_15000.csv")

#Crear una lista de listas de estudiantes
for linea in archivo:
  linea = linea[:-1] #Se quita salto de línea
  estudiante = linea.split(";")
  data_array.append(estudiante)

#Retirar las cabeceras del data_array, estas funcionan como diccionarios para las diferentes funciones  
cabeceras = data_array[0]
data_array.pop(0) #Se eliminan las cabezera

#Iniciaizar tiempo final y obtener el tiempo de ejecución para lectura de datos
tiempo_final = time()
tiempo_ejecución = tiempo_final - tiempo_inicial

print("El tiempo de ejecución para "+str(len(data_array))+" datos fue: "+str(round(tiempo_ejecución,3))+" segundos")

#Tamaño en bytes que consume el dataset
print("El tamaño del dataset es de: "+str(sys.getsizeof(data_array))+" bytes")


"""
#Llamado a los diferentes métodos
print(Buscar(data_array,cabeceras,"SB11201220492226")) 
print(data_array[0][0])
Borrar(data_array,cabeceras,"SB11201220492226","estu_consecutivo.1")
print(data_array[0][0])

new = data_array[0]

Insertar(data_array,cabeceras,None,"SB11201220492226","estu_consecutivo.1","hola")
print(data_array[0][0])
print(Acceder(data_array,0,0))
"""
