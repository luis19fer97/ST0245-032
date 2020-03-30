

def Acceder(data_array,val_estu,val_data = None):
  if val_estu == None:
    return data_array[val_estu]
  else:
    return data_array[val_estu][val_data] 

