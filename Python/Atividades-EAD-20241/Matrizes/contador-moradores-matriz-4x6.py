import numpy as np
import random

print("\nATIVIDADE 2 - Contador de moradores prédio\n")

andar = 4
apto = 6
moradores = 0

predio = np.zeros((andar, apto), dtype=int)

for l in range(andar):
  for c in range(apto):
    predio[l,c] = random.randint(0, 4)
    moradores += predio[l,c]

print(predio)
print(f"\nEsse prédio abriga {moradores} moradores.")