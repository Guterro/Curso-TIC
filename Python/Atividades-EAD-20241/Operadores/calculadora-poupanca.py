print("\nATIVIDADE 1 - CÁLCULO DE QUANTO A POUPANÇA IRÁ LUCRAR\n")

deposito = float(input("Informe o valor depositado na poupança: R$"))
juros = float(input("Informe o valor da porcentagem de rendimento de sua poupança:"))
mes = int(input("Informe quantos meses você deseja deixar esse valor rendendo em sua poupança:"))

juros_decimal = juros / 100

valor_atual = deposito

for n in range(mes):
    valor_atual += valor_atual * juros_decimal

rendimento = valor_atual - deposito

if mes == 1:
    print(f"O valor depositado de R$ {deposito:.2f} rendeu R$ {rendimento:.2f} na poupança após {mes} mês.\nCom isso, seu valor atual na poupança é de: R$ {valor_atual:.2f}")
else:
    print(f"O valor depositado de R$ {deposito:.2f} rendeu R$ {rendimento:.2f} na poupança após {mes} meses.\nCom isso, seu valor atual na poupança é de: R$ {valor_atual:.2f}")