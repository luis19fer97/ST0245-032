#Array3
#Countclumps
def countclumps(array):
  cont = 0
  aux = None
  for i in range(1,len(array)):
    if array[i]==array[i-1]:
      aux = array[i]
      if i+1 == len(array) and aux!=None:
        cont = cont + 1
    else:
      if aux != None and array[i]!=array[i-1]:
        cont = cont + 1
        aux = None
  return cont

#Canbalance
def canbalance(array):
  sum1 = 0
  sum2 = 0
  res = False
  for i in range(len(array)):
    sum1 = array[i] + sum1 
  for j in range(len(array)):
    sum2 = array[j]+sum2
    sum1 = sum1 - array[j]
    if sum1 == sum2:
      return True
    
  return res


#seriesup
def seriesup(n):
  array = []
  for i in range(1,n+1):
    #print(i)
    for j in range(1,i+1):
      array.append(j)
    
  print(len(array))
  return(array)


#Linearin
def linearin(array1,array2):
  for i in range(len(array2)):
    key = False
    for j in range(len(array1)):
      if array2[i]==array1[j]:
        key = True
    if key == False:
      break
  return key


    
  