# trabalho-POO-2024

Sistema de Gerenciamento de Séries em Streaming

Projeto acadêmico desenvolvido na disciplina de Programação Orientada a Objetos em Java.  
O objetivo foi criar um sistema que permita cadastrar, consultar, alterar e remover séries de televisão em um serviço de streaming fictício.

## Objetivos
- Implementar conceitos de **Programação Orientada a Objetos (POO)**.  
- Utilizar **listas dinâmicas (ArrayList)** para armazenar objetos.  
- Realizar operações de **entrada e saída de dados (I/O)** em arquivos `.csv`.  
- Criar um sistema de menu interativo para o usuário.

## Tecnologias Utilizadas
- **Java** (Orientação a Objetos, Classes, Métodos)  
- **ArrayList** (armazenamento dinâmico de objetos)  
- **Manipulação de Arquivos (IO, CSV)**  
- **Console (Scanner)** para interação com o usuário  

## Funcionalidades
O programa oferece as seguintes operações:

1. **Cadastrar nova série**  
2. **Alterar série existente** (buscando por título e ano)  
3. **Remover série** (buscando por título e ano)  
4. **Listar séries lançadas após um determinado ano**  
5. **Listar séries por gênero** (Comédia, Drama, Romance ou Ficção)  
6. **Listar todas as séries cadastradas**  
7. **Sair e salvar os dados em arquivo CSV**  

## Persistência em Arquivo
- As séries são gravadas no arquivo `servicostreaming.csv`.  
- Cada linha contém: `titulo;genero;temporadas;ano;concluida`.  
- Ao iniciar, o sistema carrega os dados do arquivo automaticamente.  
- Ao encerrar, os dados atualizados são salvos novamente.  