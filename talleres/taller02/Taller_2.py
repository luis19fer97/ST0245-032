def euclides (p,q):

    if (p % q) == 0:
        return q
    else:
        return euclides (q,(p % q))


def Suma_grupo(start, nums, target):

  if (start >= nums.length):
      return (target == 0);
    
    lopongo = Suma_grupo(start+1,nums, target - nums[start])
    nolopongo = Suma_grupo(start+1,nums, target)
    if (lopongo or nolopongo):
        return true
     else:
         return false
    

  
print(Suma_grupo(0,[2, 4, 8],10))
