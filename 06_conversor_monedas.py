def conversor(tipo_pesos, valor_peso):
  peso = input("¿Cuantos " + tipo_pesos + " tienes?: ")
  peso = float(peso)

  dolar = peso * valor_peso
  dolar = round(dolar, 2)
  dolar = str (dolar)
  print ("Tienes " + dolar + " pesos")

menu = """
Bienvenido al convertido de pesos a 
1. Dolares
2. Pesos argentinos
3. Pesos colombianos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
  conversor('dolares', 20)
elif opcion == 2:
  conversor('pesos argentinos', 4.82)
elif opcion == 3:
  conversor('pesos colombianos', 184.28)
else:
  print('Elige una opción correcta')


