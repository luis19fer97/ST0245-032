def lectura(archivo):
  
  data_array = []
  estudiante = []
  cont = 0

  archivo = open(archivo)
  
  for linea in archivo:
    cont += 1
    if cont % 2 == 1: #Se quitan líneas vacías
      linea = linea[:-1] #Se quita salto de línea
      estudiante = linea.split(",")
      data_array.append(estudiante)
  return(data_array)

