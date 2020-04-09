# Balanced brackets (Opcional 2.4)
#Este código, como el ejercicio, asume que el usuario sabe la jerarquía de cada signo de agrupación, por lo que no se tiene en cuenta que el usuario escriba, por ejemplo: ({[]}), porque no es el orden usual; si se le ingresa algo con la misma lógica, el algoritmo retorna YES, pues sí está equilibrado, mas no respeta la jerarquía de los signos de agrupación en el álgebra común.
string = str(input("Sólo se reciben caracteres {,[,(,),],}\nEscriba la cadena:  "))
pila = []
pila1 = []
pila_aux = []
if len(string)%2 ==1:
  print("NO, n impar")
else:
  key = True
  for j in range(len(string)):
    if string[j] != ")" and string[j] != "}" and string[j] != "]":
      pila.append(string[j])
    elif string[j] == ")":
      pila1.append("(")
    elif string[j] == "]":
      pila1.append("[")
    else:
      pila1.append("{")
  if len(pila) != len(pila1):
    print("NO")

  else:
    for i in range(len(pila)):
      pila_aux.append(pila1[len(pila1)-1])
      pila1 = pila1[:-1]
    

    for j in range(len(pila_aux)):
      if pila[len(pila)-1] != pila_aux[len(pila_aux)-1]:
        if key == True:
          print("NO")
        key = False
      pila = pila[:-1]
      pila_aux = pila_aux[:-1]
    if key == True:
      print("YES")
    
  

  

