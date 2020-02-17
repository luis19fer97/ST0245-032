def Sum_six(index, nums, target):
  if(index >= len(nums)):
    return target==0
  if (nums[index]==6):
   return Sum_six(index+1 ,nums, target - 6)
  SeToma = Sum_six(index+1 ,nums, target - nums[index]) 
  NoSeToma = Sum_six(index+1 ,nums, target)
  if SeToma or NoSeToma:
    return True
  else:
    return False

def groupNoAdj(index, nums, target):
 if (index >= len(nums)):
  return target == 0
 
 return (groupNoAdj(index + 2, nums, target - nums[index]) or groupNoAdj(index + 1, nums, target))


def groupSum5(index, nums, target):
  if(index >= len(nums)):
    return target==0
  if (nums[index]%5==0):
   return groupSum5(index+1 ,nums, target -nums[index] )
  elif (nums[index-1]%5==0) and (nums[index]==1):
    return groupSum5(index+1 ,nums, target)
  else:
    return groupSum5(index+1 ,nums, target - nums[index]) or groupSum5(index+1 ,nums, target)


def groupSumClump(start, nums, target):
  if (start >= len(nums)):
   return target ==0
  i = start + 1
  while (i < len(nums) and nums[start] == nums[i]):
    i += 1 
  if (groupSumClump(i, nums, target - ((i - start) * nums[start]))):
    return True 
  return groupSumClump(i, nums, target)

#Tomado de https://repl.it/@ebrahim_akh95/Recursion3

def splitOdd10(nums):
 b = [] #Grupo 1
 c = [] #Grupo 2
 splitOdd10Helper(nums, b, c, 0)
 result = False  #Todos son pares
 sum_n = sum(nums)  #Suma todos los números de la lista
 if (sum_n % 2 == 1):  #Es impar?
  result = True  #Encontré un impar!
 return result
  
def splitOdd10Helper(a, b, c, idx):
  if (idx == len(a)):
    sum_n = sum(b)
    c.append(sum_n)
    return
  else:
    d = b[:]
    b.append(a[idx])
    splitOdd10Helper(a, b, c, idx + 1)
    splitOdd10Helper(a, d, c, idx + 1)

#Tomado de https://repl.it/@ebrahim_akh95/Recursion3