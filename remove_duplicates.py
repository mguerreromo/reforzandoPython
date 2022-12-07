#Esta funcion elimina los duplicados dentro de la lista 

def remove_duplicates(list):
  result = []
  for item in list:
    if item not in result:
      result.append(item)
  return result
