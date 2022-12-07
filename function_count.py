def count(sequence, item):

  count = 0
  for i in sequence:
    if i == item:
      count +=1
  return count

#llamo a la funcion
print count([3,5,6,7,3,3], 3)
