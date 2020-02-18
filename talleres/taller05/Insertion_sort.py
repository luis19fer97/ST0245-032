 
def insertionSort(a): 

    for i in range(1, len(a)): 

        num = a[i]                          # C1

        j = i-1                             # C2 + T(n-1)
        while j >=0 and num < a[j] :        # C3
            a[j+1] = a[j]                   # C4
            j -= 1                          # C5
        a[j+1] = num                        # C6
        
    return (a)


""" La ecuación de complejidad para este caso es T(n) = c_2 n + c_1 donde c_2 y c_1 son parametros arbitrarios"""
