def soma(x,y):
  return x + y

def subt(x,y):
    return x - y

def divisao(x,y):
  return x/y

def multi(x,y):
  return x * y

while True:
    print("ATIVIDADE 1 - CALCULADORA BÁSICA")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")
    
    opcao = input("\nEscolha uma operação (0-4): ")

    if opcao == '0':
        print("Encerrando a calculadora...")
        break
    
    if opcao in ['1', '2', '3', '4']:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            print(f"\nResultado: {n1} + {n2} = {soma(n1, n2)}")
        elif opcao == '2':
            print(f"\nResultado: {n1} - {n2} = {subt(n1, n2)}")
        elif opcao == '3':
            print(f"\nResultado: {n1} * {n2} = {multi(n1, n2)}")
        elif opcao == '4':
            if n2 != 0:
                print(f"\nResultado: {n1} / {n2} = {divisao(n1, n2)}")
            else:
                print("\nErro: Não é possível dividir por zero!")
    else:
        print("\nOpção inválida! Tente novamente.")