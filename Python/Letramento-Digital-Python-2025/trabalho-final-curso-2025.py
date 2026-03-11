import datetime
import csv
import os

ARQUIVO_CSV = 'despesas.csv'
CATEGORIAS_VALIDAS = {
    1: 'Alimentação',
    2: 'Transporte',
    3: 'Moradia',
    4: 'Lazer',
    5: 'Saúde',
    6: 'Outros'
}

despesas = []


def carregar_csv():
    if not os.path.exists(ARQUIVO_CSV):
        return
    try:
        with open(ARQUIVO_CSV, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data = datetime.datetime.strptime(row['Data'], "%Y-%m-%d").date()
                despesas.append({
                    'data': data,
                    'categoria': row['Categoria'],
                    'valor': float(row['Valor']),
                    'descricao': row['Descricao']
                })
    except Exception:
        pass


def obter_data():
    while True:
        data_str = input("Data (DD/MM/AAAA) [Enter para hoje]: ").strip()
        if not data_str:
            return datetime.date.today()
        try:
            return datetime.datetime.strptime(data_str, "%d/%m/%Y").date()
        except ValueError:
            print("Erro: Formato de data inválido. Use DD/MM/AAAA.")


def obter_valor():
    while True:
        try:
            val_input = input("Valor (R$): ").replace(',', '.')
            if not val_input:
                print("Erro: O valor não pode ser vazio.")
                continue

            valor = float(val_input)

            if valor <= 0:
                print("Erro: O valor deve ser maior que ZERO.")
                continue

            if valor != round(valor, 2):
                print("Erro: O valor deve ter no máximo 2 casas decimais.")
                continue

            return valor

        except ValueError:
            print("Erro: Digite um número válido.")


def obter_categoria():
    print("\nCategorias:")
    for k, v in CATEGORIAS_VALIDAS.items():
        print(f"{k} - {v}")
    while True:
        try:
            opcao = int(input("Escolha a categoria (número): "))
            if opcao in CATEGORIAS_VALIDAS:
                return CATEGORIAS_VALIDAS[opcao]
            print("Opção inválida.")
        except ValueError:
            print("Digite apenas o número.")


def adicionar_despesa():
    print("Nova Despesa:")
    data = obter_data()
    categoria = obter_categoria()
    descricao = input("Descrição: ").strip()
    valor = obter_valor()
    nova_despesa = {
        'data': data,
        'categoria': categoria,
        'valor': valor,
        'descricao': descricao
    }
    despesas.append(nova_despesa)
    print("\nDespesa registrada!")


def listar_despesas():
    if not despesas:
        print("\nNenhuma despesa registrada.")
        return
    print(f"\n{'DATA':<12} | {'CATEGORIA':<15} | {'DESCRIÇÃO':<20} | {'VALOR':>10}")
    print("-" * 65)
    for d in despesas:
        data_fmt = d['data'].strftime("%d/%m/%Y")
        print(f"{data_fmt:<12} | {d['categoria']:<15} | {d['descricao']:<20} | R$ {d['valor']:>8.2f}")


def grafico_texto(dados):
    if not dados:
        print("Nenhum dado para exibir no gráfico.")
        return

    maior_valor = max(dados.values())
    escala = 40 / maior_valor if maior_valor > 0 else 1

    print("\nGráfico:\n")
    for categoria, valor in dados.items():
        barras = "█" * int(valor * escala)
        print(f"{categoria:<15} | {barras} R$ {valor:.2f}")

def relatorio_mensal():
    try:
        mes = int(input("\nInforme o Mês (1-12): "))
        ano = int(input("Informe o Ano (ex: 2024): "))
    except ValueError:
        print("Mês ou Ano inválidos.")
        return

    filtro = [d for d in despesas if d['data'].month == mes and d['data'].year == ano]

    if not filtro:
        print(f"\nNenhuma despesa encontrada para {mes}/{ano}.")
        return

    total_geral = sum(d['valor'] for d in filtro)
    gastos_por_cat = {}
    for d in filtro:
        gastos_por_cat[d['categoria']] = gastos_por_cat.get(d['categoria'], 0) + d['valor']

    categoria_maior_gasto = max(gastos_por_cat, key=gastos_por_cat.get)

    print(f"\nRELATÓRIO MENSAL - {mes:02d}/{ano}")
    print(f"Total Gasto: R$ {total_geral:.2f}")
    print(f"Maior Categoria: {categoria_maior_gasto} (R$ {gastos_por_cat[categoria_maior_gasto]:.2f})")

    grafico_texto(gastos_por_cat)

def relatorio_anual():
    try:
        ano = int(input("\nInforme o Ano (ex: 2024): "))
    except ValueError:
        print("Ano inválido.")
        return

    filtro = [d for d in despesas if d['data'].year == ano]

    if not filtro:
        print(f"\nNenhuma despesa encontrada para {ano}.")
        return

    total_geral = sum(d['valor'] for d in filtro)
    gastos_por_cat = {}
    for d in filtro:
        gastos_por_cat[d['categoria']] = gastos_por_cat.get(d['categoria'], 0) + d['valor']

    categoria_maior = max(gastos_por_cat, key=gastos_por_cat.get)

    print(f"\n=== RELATÓRIO ANUAL - {ano} ===")
    print(f"Total Gasto no Ano: R$ {total_geral:.2f}")
    print(f"Maior Categoria no Ano: {categoria_maior} (R$ {gastos_por_cat[categoria_maior]:.2f})")

    grafico_texto(gastos_por_cat)

def exportar_csv():
    if not despesas:
        print("Nada para exportar.")
        return
    try:
        with open(ARQUIVO_CSV, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Data', 'Categoria', 'Valor', 'Descricao'])
            for d in despesas:
                writer.writerow([
                    d['data'].strftime("%Y-%m-%d"),
                    d['categoria'],
                    d['valor'],
                    d['descricao']
                ])
        print(f"\nDados exportados com sucesso para '{ARQUIVO_CSV}'.")
    except Exception as e:
        print(f"Erro ao exportar: {e}")


carregar_csv()

while True:
    print("\n=== CONTROLE DE DESPESAS ===\n")
    print("1. Adicionar Despesa")
    print("2. Listar Todas")
    print("3. Relatório Mensal e Gráfico")
    print("4. Relatório Anual e Gráfico")
    print("5. Exportar para CSV")
    print("0. Sair")

    opcao = input("Opção: ")

    if opcao == '1':
        adicionar_despesa()
    elif opcao == '2':
        listar_despesas()
    elif opcao == '3':
        relatorio_mensal()
    elif opcao == '4':
        relatorio_anual()
    elif opcao == '5':
        exportar_csv()
    elif opcao == '0':
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida!")