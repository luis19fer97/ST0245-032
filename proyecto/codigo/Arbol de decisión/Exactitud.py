from Clasificar import clasificar

# En este método se almacenan los valores iniciales del data set de prueba y son comparados con los 
# entregados por el algoritmo y así obtener el porcentaje de exactitud

def Exactitud(data_array_test, arbol):
    valores_reales = []
    valores_predecidos = []
    
    
    for row in data_array_test:
        valores_reales.append(row[-1])
        valores_predecidos.append([*clasificar(row, arbol).keys()])

    total = 0

    for i in range(len(valores_reales)):
        if int(valores_reales[i]) == int(valores_predecidos[i][0]):
            total += 1
    
    return (print('Exactitud: ' +str((total/len(valores_reales))*100) +'%'))