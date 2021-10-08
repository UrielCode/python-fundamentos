# Diccionarios

# Esctrucurar de llaves y valores
# Accedemos a sus llaves(indice)

def run():
  mi_diccionario = {
    'llave1': 1,
    'llave2': 2,
    'llave3': 3,
    'llave4': 4,
  }

  # print(mi_diccionario['llave1'])
  # print(mi_diccionario['llave2'])
  # print(mi_diccionario['llave3'])

  poblacion_pais ={
    'Argentina': 12312312,
    'Brazil': 1231212,
    'Mexico': 1232312
  }

  # print(poblacion_pais['Argentina'])

  # for pais in poblacion_pais.keys():
  #   print(pais)

  # for pais in poblacion_pais.values():
  #   print(pais)

  for pais, poblacion in poblacion_pais.items():
    print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
  run()
