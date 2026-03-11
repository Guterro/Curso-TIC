# Aplicativo de Controle de Despesas Pessoais

Este projeto é o trabalho final do curso de **Letramento Digital em Python: Fundamentos de Programação e Inclusão Digital** (80h), realizado como projeto de extensão na **UFSC**.

O sistema foi desenvolvido para auxiliar no gerenciamento financeiro doméstico, permitindo o registro, a categorização e a análise visual de gastos.

---

## Funcionalidades

* **Registro de Gastos:** Adição de despesas com data, categoria, descrição e valor.
* **Persistência de Dados:** Carregamento automático e exportação de dados em formato CSV (`despesas.csv`).
* **Relatórios Mensais e Anuais:** Filtros inteligentes que agrupam gastos por período.
* **Visualização de Dados:** Geração de gráficos em modo texto (barras) diretamente no terminal para comparação de categorias.
* **Análise de Gastos:** Identificação automática da categoria com maior volume de despesas.

---

## Conceitos de Programação Aplicados

O projeto demonstra o domínio dos seguintes fundamentos de Python:

* **Estruturas de Dados:** Uso de listas e dicionários para gerenciar coleções de despesas.
* **Manipulação de Bibliotecas:** Uso do módulo `datetime` para tratamento de datas e `csv` para persistência de dados.
* **Tratamento de Erros:** Validações de entrada de dados (como valores numéricos e formatos de data) para evitar falhas de execução.
* **Manipulação de Arquivos:** Leitura e escrita de arquivos externos para armazenamento de informações.
* **Lógica de Programação:** Implementação de algoritmos de soma, filtragem e cálculo de escalas para o gráfico.

---

## Como Utilizar

1. Execute o script principal em um ambiente Python:
   ```bash
   python trabalho-final-curso-2025.py