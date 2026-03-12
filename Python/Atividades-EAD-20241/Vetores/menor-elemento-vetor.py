print("\nATIVIDADE 2 - MENOR ELEMENTO EM UM VETOR\n")

vetor = []
for i in range(15):
  numero = int(input(f"Digite o número {i + 1}/15: "))
  vetor.append(numero)

menor_valor = min(vetor)
posicao = vetor.index(menor_valor)

print(f"O menor elemento é {menor_valor} e sua posição no vetor é {posicao + 1}")