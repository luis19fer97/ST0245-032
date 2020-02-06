def hanoi(n, a = "Tower 1", b = "Tower 2", c = "Tower 3"):
    if n == 1:
        print ("From " + a + " to " + c)
    else:
        hanoi(n - 1, a, c , b )
        print ("From " + a + " to " + c)
        hanoi(n - 1, b, a, c )
        
def permutacion(perm, s):
    
       if len(s) == len(perm): 
           yield s # Se usa yield para que luego de la primera permutación no se salga de la función
       for i in perm:
           if i in s: 
               continue
           s=s+i
           for x in permutacion(perm, s): 
               yield x
           s=s[:-1]
               
print(list(permutacion("abc",'')))
