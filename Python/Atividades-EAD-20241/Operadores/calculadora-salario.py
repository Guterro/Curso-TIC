print("\nATIVIDADE 2 - CÁLCULO DO SALÁRIO FINAL DE UM VENDEDOR\n")

idvendedor = int(input("Digite seu ID de vendedor:"))
salariofixo = float(input("Digite o valor de seu salário fixo: R$"))
vendas = float(input("Digite o valor total das vendas vendas efetuadas por você no mês: R$"))

comissao = (vendas * 0.15) + salariofixo

print ("O salário do vendedor", idvendedor,  "no fim do mês (sem decontos) será de: R$", comissao)