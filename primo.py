num = int(input("Ingrese un numero: "))

def nPrimo(num):
  if num < 1:
    return False
  elif num == 2:
    return True
  else:
    for i in range (2, num):
      if num % i == 0:
        return False
    return True

resultado = nPrimo(num)
if resultado is True:
  print("El numero es primo")
else: 
  print("El numero no es primo")
