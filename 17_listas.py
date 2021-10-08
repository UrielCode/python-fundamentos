# Listas (Array)

# Pertenece a las estructuras de datos, 
# Almacena varios valores en una variable
# Contiene datos de un mismo tipo o diferente
# Dinámicas
# Usan []
# Son mutables

numeros = [1, 3, 4, 5, 6, 9, 45, 90]

objetos = ['hola', 4.5, True, 3]

# Acceder a un elementos de una lista
objetos[1]

# Agregar un valor al final
objetos.append(False)

# Borrar un elemento 
objetos.pop(3)

# Recorrer un lista
for elementos in objetos:
  print(elementos)

# Invertir una lista
objetos[::-1]

# Contatenar listas
numeros = [1, 2, 3, 4, 5]
numeros2 = [6, 7, 8, 9]

numeros + numeros2 
# [1, 2, 3, 4, 5, 6, 7, 8, 9]