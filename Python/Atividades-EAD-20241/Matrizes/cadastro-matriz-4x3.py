import numpy as np

print("\nATIVIDADE 1 - Cadastro (Matriz 4x3)\n")

l = 4
c = 3

matriz2 = np.zeros((l, c), dtype='U100')

for l in range(4):
    for c in range(3):
        if c == 0:
            nome = str(input("Digite seu nome: "))
            matriz2[l, c] = nome
        elif c == 1:
            email = str(input("Digite seu email: "))
            matriz2[l, c] = email
        elif c == 2:
            telefone = str(input("Digite seu telefone: "))
            matriz2[l, c] = telefone

print(matriz2)
