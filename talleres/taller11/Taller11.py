import numpy as np

class GraphAL:
  def __init__(self, size):
    self.size = size
    aux = []
    matriz = []
    for i in range(self.size+1):
      aux = []
      for j in range(self.size+1):
        aux.append(None)
      matriz.append(aux)
    array = np.array(matriz)
    self.matriz = array
    print(self.matriz) #Se crea matriz con None, ya que los ceros condicionan a solo recibir nodos o vértices del tipo flotante, y en realidad se pueden tener strings.

# Agregar arco entre A y B (Y crear vértices asignándoles el peso respectivo):
  def addArc(self, vertex, edge, weight):
    vertex_exist = False
    edge_exist = False
    fila = None
    columna = None
    for i in range(1,len(self.matriz),1): #Se buscan los valores, rango en len (#filas)
      if vertex == self.matriz[0][i]:
        vertex_exist = True
      if edge == self.matriz[0][i]:
        edge_exist = True
    if vertex_exist == False: #Si no existe, agregar
      for i in range(1,len(self.matriz),1):
        if self.matriz[0][i] == None:
          self.matriz[0][i] = vertex
          self.matriz[i][0] = vertex
          break
    if edge_exist == False: #Si no existe, agregar
      for i in range(1,len(self.matriz),1):
        if self.matriz[0][i] == None:
          self.matriz[0][i] = edge
          self.matriz[i][0] = edge
          break
    for i in range(len(self.matriz)):
      if self.matriz[i][0] == vertex:
        fila = i
      if self.matriz[0][i] == edge:
        columna = i
    self.matriz[fila][columna] = weight
  
    return (self.matriz)
    print(self.matriz)
#Retornar nodos adjacentes al buscado:       
  def getSucessors(self, vertice):
    fila = 0
    columna = 0
    nodos = []
    #Se encuentran nodos adyacentes a través de filas
    #y de columnas
    for i in range(len(self.matriz)):
      if self.matriz[i][0] == vertice:
        for j in range(1,len(self.matriz),1):
          if self.matriz[i][j] != None:
            nodos.append(self.matriz[0][j])

    for i in range(len(self.matriz)):
      if self.matriz[0][i] == vertice:
        for j in range(1,len(self.matriz),1):
          if self.matriz[j][i] != None:
            nodos.append(self.matriz[j][0])
    
    nodos = list(set(nodos)) #Se eliminan repetidos
    for i in range(len(nodos)):
      print("El nodo " + str(nodos[i]) + " es adyacente al nodo " +str(vertice) + str(" y viceversa"))
    return nodos
#Obtener el peso o la etiqueta de la relación que parte del nodo Source hacia el Destination:
  def getWeight(self, source, destination):
    fila = None
    columna = None
    for i in range(len(self.matriz)):
      if self.matriz[i][0] == source:
        fila = i
      if self.matriz[0][i] == destination:
        columna = i
    peso = (self.matriz[fila][columna])
    if peso == None:
      return "No existe peso desde " + str(source) + " hacia " + str(destination)
    else:
      return "El peso ejercido desde " + str(source) + " hacia " + str(destination) + " es de " + str(peso)

g = GraphAL(4) #Se defina el objeto g de la clase GraphAL
print(g.addArc("A","B","500")) #Se asigna etiqueta al arco (Pareja ordenada), esta etiqueta es el peso
print(g.addArc("C","A","800"))
print(g.addArc("H","A","600"))
print(g.getSucessors("A")) #
print(g.getWeight("B","A"))
""" NOTA:
el algoritmo asume que el usuario sabe qué tantos nodos se le van a asignar al grafo, por tanto si se intenta asignar un arco y los nodos de éste sumados a los anteriores superan el tamaño ingresado por el usuario, el algoritmo no funciona, pues excede los límites
