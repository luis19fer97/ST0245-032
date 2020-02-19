 
def insertionSort(a): 

    for i in range(1, len(a)): 

        num = a[i]                          # C1

        j = i-1                             # C2 + T(n-1)
        while j >=0 and num < a[j] :        # C3
            a[j+1] = a[j]                   # C4
            j -= 1                          # C5
        a[j+1] = num                        # C6
        
    return (a)


""" la ecuación de complejidad para este caso es T(n) = c_2 n + c_1 donde c_2 y c_1 son parametros arbitrarios"""



def suma(a,res = 0):
    
    for i in range(0,len(a)):

        res = res +a[i]
    return res

# Recursivo:
def sum(array, i=0):
  if i>=len(array):
    return 0
  else:
    return sum(array,i+1)+array[i]
