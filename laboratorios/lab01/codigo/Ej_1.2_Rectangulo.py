# 1.2 algoritmo RECURSIVO que calcula las n formas diferemtes en las que se puede acomodar un rectángulo de 1x2 en otro de 2xN
def rectangulo(N):
  if (N<=2):
    return N 
  return rectangulo(N-1) + rectangulo(N-2) 

