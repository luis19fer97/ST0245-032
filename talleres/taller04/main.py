x = (1,2,3,4,5,400,0,1)

def high(array, i=0 , h=0):
  if (len(array)==1):
    return array[0]
  elif (len(array)==i):
    print(h)
    return(h)
  elif(len(array)>i):
    if(array[i]>h):
      h = array[i]
    return high(array,i+1,h)
high(x)
