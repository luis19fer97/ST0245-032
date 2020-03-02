import numpy as np
import sys
import time

#Inicializar variables
sys.setrecursionlimit(1000000)
start_time = time.time()
out = np.empty([20, 1])
a = 0

# Tomado de https://www.geeksforgeeks.org/python-program-for-insertion-sort/ 
def insertionSort(x): 
    #start_time = time.time() #Iniciar tiempo de ejecución
    
    # Traverse through 1 to len(x) 
    for i in range(1, len(x)): 
  
        key = x[i] 
  
        # Move elements of x[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < x[j] : 
                x[j+1] = x[j] 
                j -= 1
        x[j+1] = key 
    #return ((time.time() - start_time)*1000) #Retornar tiempo de ejecución en milisegundos

# Tomado de https://www.geeksforgeeks.org/merge-sort/
def mergeSort(x): 
    #start_time = time.time() #Iniciar tiempo de ejecución

    if len(x) >1: 
        mid = len(x)//2 #Finding the mid of the xay 
        L = x[:mid] # Dividing the xay elements  
        R = x[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp xays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                x[k] = L[i] 
                i+=1
            else: 
                x[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            x[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            x[k] = R[j] 
            j+=1
            k+=1
            
    return (x)
    #return ((time.time() - start_time)*1000) #Retornar tiempo de ejecución en milisegundos

"""
#Ciclo para almacenar los tiempos de ejecución de los algoritmos en un arreglo
for i in range (500, 10500, 500):
    array = np.random.randint(1,i,i)
    #out[a,0] =  mergeSort(array)
    out[a,0] =  insertionSort(array)
    a = a +1
print (out)
"""

  
