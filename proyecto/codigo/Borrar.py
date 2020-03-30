#Para el método borrar, es exactamente lo mismo, sólo que en vez de retornar todo un estudiante o un atributo del mismo, borra o elimina todo el vector, o un atributo en específico del estudiante (Del vector fila).
def Borrar (data_array,cabeceras,ID_estudiante, atributo=None):

  if isinstance(ID_estudiante, str) :
    for i in range(len(data_array)):
      if (data_array[i][0]) == ID_estudiante:
        ID_estudiante = i

  if atributo == None:
    data_array.pop(ID_estudiante)
  else:
    for j in range(len(cabeceras)):
      if cabeceras[j] == atributo:
        atributo = j  
    data_array[ID_estudiante][atributo] = None
    