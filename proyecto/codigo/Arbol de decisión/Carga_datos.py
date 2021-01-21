# Este método sirve para cargar los datos de entrenamiento y prueba para el árbol de decisión
# además permite obtener las cabeceras del csv para utilizarlas en las preguntas
import pandas as pd

def carga_datos(ruta_entrenamiento,ruta_prueba):
    datos_entrenamiento = []
    datos_prueba = []
    Filas = []

    #Cargar el archivo de datos
    archivo_entrenamiento = open(ruta_entrenamiento,encoding='utf-8')
    archivo_prueba = open(ruta_prueba,encoding='utf-8')

    #Crear una lista de listas de estudiantes
    for linea in archivo_entrenamiento:
        linea = linea[:-1] #Se elimina el salto de línea en el csv
        Filas = linea.split(";")
        datos_entrenamiento.append(Filas)

    #Retirar las cabeceras del data_array, estas se utilizan para imprimir el árbol  
    cabeceras = datos_entrenamiento[0] 

    Filas = []

    for linea in archivo_prueba:
        linea = linea[:-1] #Se quita salto de línea
        estudiante = linea.split(";")
        datos_prueba.append(estudiante)
    
    datos_entrenamiento.pop(0) #Se eliminan las cabeceras del data set
    datos_prueba.pop(0) #Se eliminan las cabeceras del data set



    #Eliminar columnas
    a = ['estu_consecutivo.1',
    'periodo',
    'fami_numlibros',
    'estu_inst_cod_departamento',
    'estu_tipodocumento.1',
    'estu_nacionalidad.1',
    'estu_genero.1',
    'estu_fechanacimiento.1',
    'periodo.1',
    'estu_estudiante.1',
    'estu_pais_reside.1',
    'estu_cod_reside_depto.1',
    'estu_cod_reside_mcpio.1',
    'fami_ocupacionpadre.1',
    'fami_ocupacionmadre.1',
    'fami_tienedvd',
    'cole_codigo_icfes',
    'cole_nombre_establecimiento',
    'cole_sede_principal',
    'cole_cod_dane_establecimiento',
    'estu_trabajaactualmente',
    'cole_cod_dane_sede',
    'cole_cod_mcpio_ubicacion',
    'cole_cod_depto_ubicacion',
    'desemp_ingles']

    datos_entrenamiento_df = pd.DataFrame.from_records(datos_entrenamiento,columns = cabeceras)
    datos_prueba_df = pd.DataFrame.from_records(datos_prueba,columns = cabeceras)

    for i in range(len(a)):
        del datos_entrenamiento_df[a[i]]
        del datos_prueba_df[a[i]]
        cabeceras.remove(a[i])

    datos_entrenamiento = datos_entrenamiento_df.values.tolist()
    datos_prueba = datos_prueba_df.values.tolist()

    return datos_entrenamiento,datos_prueba,cabeceras

