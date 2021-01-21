# Este método permite obtener los valores únicos que hay en la columna interesada (éxito)

def valores_unicos(filas, columnas):
    return set([row[columnas] for row in filas])

