def consulta_2(data_1,data_2,data_3,estudiante,semestre):
  respuesta =  []
  for i in range(len(data_1)):
    if data_1[i][0] == estudiante:
      if data_1[i+1][0] == data_1[i][0]:
          i = i +1
      else:
        aux1 = 'Fundamentos de programación: '+str(data_1[i][13])
        respuesta.append(aux1)
        break
  
  for i in range(len(data_2)):
    if data_2[i][0] == estudiante:
      if data_2[i+1][0] == data_2[i][0]:
          i = i +1
      else:
        aux2 = 'Estructura de datos y algoritmos 1: '+str(data_2[i][13])
        respuesta.append(aux2)
        break
  
  for i in range(len(data_3)):
    if data_3[i][0] == estudiante:
      if data_3[i+1][0] == data_3[i][0]:
          i = i +1
      else:
        aux3 = 'Estructura de datos y algoritmos 2: '+str(data_3[i][13])
        respuesta.append(aux3)
        break
  if len(respuesta)<3:
    print("El estudiante sólo cursó los siguientes cursos: ")
  return respuesta
