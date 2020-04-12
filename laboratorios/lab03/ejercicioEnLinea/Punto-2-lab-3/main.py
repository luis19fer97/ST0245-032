from lista import LinkedList

def texto (text):
  #Iniciarlizar la lista enlazada
  llist = LinkedList()

  #Crear un arreglo con la cantidad de elementos a insertar
  aux = text.replace("[",",")
  aux = aux.replace("]",",")
  aux = aux.split(",") 
  #Insertar en la lista el primer elemento
  llist.push(aux[0])

  con = 1 # contador 
  for i  in range(len(text)):
    #Si hay un [ y el siguiente elemento no es vacío se inserta al inicio de la lista
    if text[i] == "[":
      if aux[con] != '':
        llist.push(str(aux[con]))
      con = con+1
    #Si hay un ] y el siguiente elemento no es vacío se inserta al final de la lista
    if text[i] == "]":
      if aux[con] != '':
        llist.append(aux[con])
      con = con+1

  #Imprimir la lista en el orden correcto  
  llist.printList()

texto('asd[fgh[jkl')