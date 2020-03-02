# Tomado de https://www.geeksforgeeks.org/python-program-for-insertion-sort/ 
def insertionSort(arr): 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

#%%
# Tomado de https://www.geeksforgeeks.org/merge-sort/
def mergeSort(x): 
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
    return x


  
