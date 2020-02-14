# 1.1 algoritmo RECURSIVO que calcula las n formas diferemtes en las que se puede acomodar un rectángulo de 1x2 en otro de 2xN
def rectangulo(N):
  if (N==0):
    return 0
  elif (N==1):
    return 1
  elif(N==2):
    return 2 
  parado = rectangulo(N-1) 
  
  acostado = rectangulo(N-2) 

  return parado + acostado

print(rectangulo(4))