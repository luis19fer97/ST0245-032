#Este método permite conocer cuál es el tipo de dato que se encuentra en la columna
#es necesario conocer el tipo para establecer la pregunta adecuada

def es_numero(valor):
    aux = False
    
    #verificar si el valor es entero
    if isinstance(valor, int):
        aux = True  
        return aux 

    # verifica si el valor es flotante, se usa un try pues si intenta realizar una conversión de string a 
    # float tendrá un error y parará el programa, en caso de que el dato sea un string el return debe ser false    
    try:
        valor = float(valor)
        if isinstance(valor, float) :
            aux = True
            return aux
    except:
           aux = False
           return aux