def fibo(n):
  if(n==0):
    return (0)
  elif(n==1):
    return(1)
  else:
    return fibo(n-1)+fibo(n-2)

def fact(n):
  if (n==0):
    return 1
  else:
    return(fact(n-1)*n)

def ears(n):
  if (n==0):
    return(0)
  elif (n%2 != 0):
    return(ears(n-1))+ 3
  elif(n%2 ==0):
    return(ears(n-1)+2)

def countx(string):
  if len(string)==0:
    return 0
  elif (string[len(string)-1])== "x":
    print(string)
    return 1 + countx(string[:len(string)-1])
  else:
    print(string)
    return countx(string[0:len(string)-1])


def array11(array, i=0):
  if len(array)==0:
    return 0
  elif (array[0]== 11):
    return 1 +array11(array[i+1:])
  else:
    return array11(array[i+1:])
def array6(array,i=0):
  if i>=len(array):
    return False
  if array[i]==6:
    return True
  else:
    return array6(array,i=i+1) 


