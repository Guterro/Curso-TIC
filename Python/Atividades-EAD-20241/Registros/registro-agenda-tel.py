import numpy as np

print("\nATIVIDADE 1 - AGENDA TELEFONICA\n")

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Agenda:
    def __init__(self, capacidade=50):
        self.contatos = [None] * capacidade
        self.capacidade = capacidade
        self.tamanho = 0

    def cadastrar_contato(self, nome, telefone):
        if self.tamanho < self.capacidade:
            self.contatos[self.tamanho] = Contato(nome, telefone)
            self.tamanho += 1
            print(f"Contato {nome} cadastrado com sucesso!\n")
        else:
            print("Agenda cheia! Não é possível adicionar mais contatos.\n")

    def remover_contato(self, nome):
        for i in range(self.tamanho):
            if self.contatos[i].nome == nome:
                self.contatos.pop(i)
                self.contatos.append(None)  # Mantém o vetor de 50 posições
                self.tamanho -= 1
                print(f"Contato {nome} removido com sucesso!\n")
                return
        print(f"Contato {nome} não encontrado na agenda.\n")

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato and contato.nome.lower() == nome.lower():
                return contato
        return None

    def exibir_agenda(self):
        print("\nAgenda de Contatos:")
        for contato in self.contatos:
            if contato:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}\n")

agenda = Agenda()

while True:
    print("Menu:")
    print("1. Cadastrar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Mostrar agenda")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("\nDigite o nome que deseja salvar para o contato: ")
        telefone = input(f"Digite o número de telefone de {nome}: ")
        agenda.cadastrar_contato(nome, telefone)

    elif opcao == '2':
        nome = input("\nDigite o nome de quem deseja remover: ")
        agenda.remover_contato(nome)

    elif opcao == '3':
        nome = input("\nDigite o nome de quem deseja buscar: ")
        contato_encontrado = agenda.buscar_contato(nome)
        if contato_encontrado:
            print(f"Contato encontrado: Nome: {contato_encontrado.nome}, Telefone: {contato_encontrado.telefone}")
        else:
            print(f"Contato {nome} não encontrado.")

    elif opcao == '4':
        agenda.exibir_agenda()

    elif opcao == '5':
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")