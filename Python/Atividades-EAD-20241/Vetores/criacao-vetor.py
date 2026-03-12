print("\nATIVIDADE 1 - CRIAÇÃO DE VETORES\n")

vetor1 = []
for i in range(20):
  numero = int(input(f"Digite o número para a posição {i + 1}: "))
  vetor1.append(numero)

vetor2 = []
for num in vetor1:
    if num == 0:
        vetor2.append(1)

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)