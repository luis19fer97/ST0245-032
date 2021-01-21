def Insertar(data_array,cabeceras,Estudiante=None,ID_estudiante=None,atributo=None,nuevo_valor=None):

  if Estudiante == None and ID_estudiante == None and atributo == None and nuevo_valor == None:
    return (print("Error, no hay argumentos para la inserción"))
  if (Estudiante == None and ID_estudiante == None) or  (Estudiante == None and atributo == None) or (Estudiante == None and nuevo_valor == None):
    return(print("Error, no hay argumentos suficientes para realizar la inserción"))
  
  if Estudiante != None:
    data_array.append(Estudiante)
  else:   
    if isinstance(ID_estudiante, str) :
      for i in range(len(data_array)):
        if (data_array[i][0]) == ID_estudiante:
          ID_estudiante = i
      for j in range(len(cabeceras)):
        if cabeceras[j] == atributo:
          atributo = j  
      data_array[ID_estudiante][atributo] = nuevo_valor