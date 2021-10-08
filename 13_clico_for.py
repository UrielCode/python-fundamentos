# contador  = 1
# print(contador)

# while contador < 5:
#     contador += 1
#     print(contador)

# a = list(range(10))
# print(a)

# for contador in range(1, 6):
#   print (contador)

# for i in range(10):
#   print(11 * i)

# Recorrer una cadena de caracteres

def run():
  # nombre = input("Escribe tu nombre: ")

  # for letra in nombre:
  #   print(letra)

  frase = input("Escribe una frase: ")

  for caracter in frase:
    print(caracter.upper())

if __name__ == '__main__':
  run()
