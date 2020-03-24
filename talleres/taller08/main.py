#Punto 1 calculadora
def calculator(cadena):
  import operator
  operators = {'+' : operator.add,
          '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,
          }

  a = cadena.split(" ")

  pila = []
  while len(pila) != 1: 
    for i in range(len(a)): 
      if  a[i]=="+" or a[i]=="-" or a[i]=="/" or a[i]=="*":
        num1 = int(pila[0])
        num2 = int(pila[1])
        sum = operators[a[i]](num1,num2)
        pila.pop()
        pila.pop()
        pila.append(sum)
      else:
        pila.append(a[i])

  return(pila)

#Punto 2 neveras

pila_neveras = list(range(10))
pila2 = []
pilaName = []
print(pila_neveras)
for j in range(2):
  Nombre = str(input("Escriba el nombre del almacén __   "))
  pilaName.append(Nombre)
  NumNev = int(input("Escriba el número de neveras solicitadas __   "))
  pila2.append(NumNev)

for n in range(len(pila2)):
  for o in range(pila2[n]):
    print("nevera numero " + str(pila_neveras[o]) + " entregada al almacén " + str(pilaName[n]))
  pila_neveras = pila_neveras[(pila2[n]):len(pila_neveras)]
print(pila_neveras)