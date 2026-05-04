import math

nomes = ["max", "bob", "carlos", "Ana"]

possiveis = len(nomes)
duplas = 2

resultado = math.factorial(possiveis) / math.factorial(duplas) * math.factorial(possiveis - duplas)
print(resultado)