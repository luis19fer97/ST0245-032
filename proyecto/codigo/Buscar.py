#El método buscar recibo el ID_Estudiante como argumento principal, y el atributo como opcional, retornando entonces todo un vector fila o estudiante, o un atributo en específico del mismo (Si el argumento atributo es dado).Mediante el acceso al vector cabeceras, la función asigna una posición (Número) al str ingresado, que es una cabecera o atributo que se dese buscar.

def Buscar (data_array,cabeceras,ID_estudiante, atributo=None):

  if isinstance(ID_estudiante, str) :
    for i in range(len(data_array)):
      if (data_array[i][0]) == ID_estudiante:
        ID_estudiante = i
      

  if atributo == None:
    return (data_array[ID_estudiante])
  else:
    for j in range(len(cabeceras)):
      if cabeceras[j] == atributo:
        atributo = j  
    return (data_array[ID_estudiante][atributo]) 

