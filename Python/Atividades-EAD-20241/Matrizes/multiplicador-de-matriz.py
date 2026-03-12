import numpy as np

print("\nATIVIDADE 4 - Multiplicar matriz\n")

l = 4
c = 4

matriz3 = np.zeros((l, c), dtype=int)

for l in range(4):
  for c in range(4):
    numero = int(input(f"\nDigite um número inteiro para preencher uma matriz\nPosição[{l},{c}]: "))
    matriz3[l,c] = numero

print(matriz3)

multiplicador = int(input("\nDigite o multiplicador da matriz: "))

for l in range(4):
  for c in range(4):
    numeromultiplicado = matriz3[l,c] * multiplicador
    matriz3[l,c] = numeromultiplicado

print(matriz3)