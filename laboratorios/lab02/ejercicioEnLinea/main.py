#Array2
#countEvens
def count(array, cont=0):
  for i in range(len(array)):
    if array[i]%2 == 0:
      cont = cont + 1
  return cont

#Sum13
def Sum13(array):
  sum=0
  for i in range(len(array)):
    if i ==0:
      if array[i] != 13:
        sum = sum + array[i]
    else:
      if array[i] != 13 and array[i-1]!=13:
        sum = sum + array[i]
  return sum  
  
#lucky13
def lucky13(array):
  var = True
  for i in range(len(array)):
    if array[i]==1 or array[i]==3:
      var = False
    return var

#Matchup
def matchup(array1, array2):
  cont = 0
  for i in range(len(array1)):
    if abs(array1[i] - array2[i])==1 or abs(array1[i] - array2[i])==2:
      cont = cont + 1 
  return cont

#Sum28
def sum28(array):
  cont=0
  for i in range(len(array)):
    if array[i]==2:
      cont = cont + 1
  if cont == 4:
    return True
  else:
    return False

    
  


    
  