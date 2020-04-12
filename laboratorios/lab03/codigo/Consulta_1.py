estudiantes= []
def consulta_1(data,curso,semestre):
  if curso == 'ESTRUCTURA DATOS Y ALGORÍTMOS 1':
    for i in range(len(data)):
      if semestre == data[i][3]: 
        if data[i+1][0] == data[i][0]:
          i = i +1
        else:
          aux = str(data[i][0]) +' '+str(data[i][13])
          estudiantes.append(aux)
  
  if curso == 'ESTRUCTURA DATOS Y ALGORÍTMOS 2':
    for i in range(len(data)):
      if semestre == data[i][3]: 
        if data[i+1][0] == data[i][0]:
          i = i +1
        else:
          aux = str(data[i][0]) +' '+str(data[i][13])
          estudiantes.append(aux)
  
  if curso == 'FUNDAMENTOS DE PROGRAMACIÓN':
    for i in range(len(data)):
      if semestre == data[i][3]: 
        if data[i+1][0] == data[i][0]:
          i = i +1
        else:
          aux = str(data[i][0]) +' '+str(data[i][13])
          estudiantes.append(aux)
  
  return estudiantes
