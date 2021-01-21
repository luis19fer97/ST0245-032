from Gini import gini

# Este método permite obtener el info gain, el cual es que es el valor condicional esperado 
# de la divergencia Kullback-Leibler de la distribución de probabilidad univariada 
# de una variable de la distribución condicional de esta variable dada la otra

def info_gain(izq, der, incertidumbre):

    p = float(len(izq)) / (len(izq) + len(der))
    return incertidumbre - p * gini(izq) - (1 - p) * gini(der)

