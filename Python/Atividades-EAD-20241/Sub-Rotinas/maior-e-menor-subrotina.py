print("\nATIVIDADE 3 - NÚMEROS MAIOR E MENOR\n")

def maior(x, y, z):
  if x > y and x > z:
    return f'{x} é maior que {y} e {z}'

  if y > x and y > z:
    return f'{y} é maior que {x} e {z}'

  if z > y and z > x:
    return f'{z} é maior que {y} e {x}'

def menor(x, y, z):
  if x < y and x < z:
    return f'{x} é menor que {y} e {z}'

  if y < x and y < z:
    return f'{y} é menor que {x} e {z}'

  if z < y and z < x:
    return f'{z} é menor que {y} e {x}'

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um outro número inteiro diferente do primeiro: "))

while n2 == n1:
  print("ERRO")
  n2 = int(input("Digite um outro número inteiro, diferente do primeiro: "))
  if n2 != n1:
    break

n3 = int(input("Digite um outro número inteiro, diferente dos outros dois: "))

while n3 == n2 or n3 == n1:
  print("ERRO")
  n3 = int(input("Digite um outro número inteiro, diferente dos outros dois: "))
  if n3 != n2 and n3 != n1:
    break

print(maior(n1, n2, n3))
print(menor(n1, n2, n3))