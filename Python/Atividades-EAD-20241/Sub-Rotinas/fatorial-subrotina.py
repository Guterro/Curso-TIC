print("\nATIVIDADE 2 - FATORIAL\n")

def fatorial(x):
  if x <= 0:
    return 0
  else:
    resultado = 1
    for _ in range(1, (x+1)):
      resultado = resultado * _
    return resultado

n1 = int(input("Digite um número inteiro, maior que 0, para realizar o fatorial: "))
print(f"{n1}! = {fatorial(n1)}")