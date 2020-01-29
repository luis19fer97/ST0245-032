def euclides (p,q):

    if (p % q) == 0:
        return q
    else:
        return euclides (q,(p % q))


def Suma_grupo(start, nums, target):

  if (start >= len(nums)):
      return (target == 0);
      
  se_toma = Suma_grupo(start+1 ,nums, target - nums[start])
  
  no_se_toma = Suma_grupo(start+1,nums, target)
  
  if (se_toma or no_se_toma):
        return True
  else:
         return False
     
