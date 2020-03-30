

def Acceder(data_array,val_data,val_estu = None):
  if val_estu == None:
    return data_array[val_data]
  else:
    return data_array[val_data][val_estu] 

