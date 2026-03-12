import numpy as np
import random

print("\nATIVIDADE 3 - Criação de Matriz 10x10\n")

l = 10
c = 10

matriz1 = np.zeros((l, c), dtype=int)

for l in range(10):
  for c in range(10):
    numero_novo = random.randint(0, 99)
    matriz1[l,c] = numero_novo

print(matriz1)