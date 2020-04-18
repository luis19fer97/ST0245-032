class Nodo(object):

  def buscar(self, a):
    if self.data == a: #Comparación (C)
      return True
    elif a < self.data and self.left: #Comparación (C)
      return self.left.buscar(a) #Llamado recursivo donde se reduce el problema a la mitad.
    elif a > self.data and self.right: #Comparación
      return self.right.buscar(a) #Llamado recursivo donde se reduce el problema a la mitad.
    return False
#Resolviendo y aplicando notación big O, se tiene que la complejidad es O(Log n);, partiendo de que el árbol está balanceado, el algoritmo va preguntando, ¿Es menor? me voy por acá (Y dejo de recorrer el otro nodo donde está el mayor y por tanto los subnodos, reduciendo n a la mitad) o, ¿Es mayor? me voy por acá  (y dejo de recorrer los otros nodos menores y subnodos, reduciendo el problema a la mitad).

  def insertar(self, a):
    if self.data == a:
      return False
    elif a < self.data:
      if self.left:
        return self.left.insertar(a) #Llamado recursivo donde se reduce el problema a la mitad. T(n/2) + C
      else:
        self.left = Nodo(a) #Asignación (C)
      return True
    else:
      if self.right:
        return self.right.insertar(a) #Llamado recursivo donde se reduce el problema a la mitad. T(n/2) + C
      else:
        self.right = Nodo(a) #Asignación (C)
      return True

#Resolviendo y aplicando notación big O, se tiene que la complejidad es O(Log n); partiendo de que el árbol está balanceado, el algoritmo va preguntando, ¿Es menor que el elemento que quiero insertar? me voy por acá (Y dejo de recorrer el otro nodo donde está el mayor y por tanto los subnodos, reduciendo n a la mitad) o, ¿Es mayor que el elemento que quiero insertar? lo inserto, pues es la posición indicada para no perder el balanceo del árbol.

#Procedimiento:
#Si se tiene T(n/2) por cada llamado recursivo, entonces:
"""
T(n) = T(n/2) + T(n/4) + T(n/8) + T(n/16) ... T(n/(2^n))

Se tiene que T(n) = Sumatoria (Desde 1 hasta m) de (n/(2^k))
Donde m es el número de llamados recursivos para llegar a la unidad. K obviamente es el iterador o variable de la sumatoria, correspondiente al exponente (Número de veces que se ha dividido el problema)
Como el problema se divide en dos por cada llamado recursivo, podemos afirmar que se llega a un momento de parado (Donde se encuentra) en el cual no se divide más, siendo ésta la unidad. Por lo tanto:

T(2^m) = T(n)
2^m = n
log (2^m) = log (n)
m = log(n)

O(log(n))

Esto también se puede resolver por medio de WolframAlpha, obteniendo el mismo resultado.
"""