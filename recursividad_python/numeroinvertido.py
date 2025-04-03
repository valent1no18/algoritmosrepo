def invertirnum_aux(n, invertido_parcial):
  """
  Función auxiliar recursiva para invertir un número entero.
  """
  if n == 0:
    return invertido_parcial # Caso base: si n es 0 (ya no quedan dígitos en n), devolvemos el número invertido acumulado
  else:
    resto = n % 10 # extrae el último dígito (el dígito de las unidades) de un número entero.
    nuevo_invertido = invertido_parcial * 10 + resto #  movemos todos sus dígitos a la izquierda y añadimos el nuevo dígito al final (resto = n % 10).
    return invertirnum_aux(n // 10, nuevo_invertido) 

def invertirnum(n):
  """
  Invierte un número entero de forma recursiva sin convertirlo a cadena.

  """
  if n < 0:
    return -invertirnum_aux(abs(n), 0) # Si el número es negativo, lo convertimos a positivo y llamamos a la función auxiliar.
  else:
    return invertirnum_aux(n, 0) # Si el número es positivo, llamamos a la función auxiliar directamente.

numero = 123
numero_invertido = invertirnum(numero)
print(f"El inverso de {numero} es: {numero_invertido}")
