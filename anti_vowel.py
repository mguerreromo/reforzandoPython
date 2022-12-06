#Se crea funcion que sustituye las vocales por espacio en blanco.
def anti_vowel(text):
  result = ''
  vowel = 'aeiouAEIOU'
  for character in text:
    if character not in vowel:
      result +=  character
  return result

print anti_vowel('Hola mundo!')
