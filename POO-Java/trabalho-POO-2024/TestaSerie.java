import java.io.IOException;
import java.util.Scanner;

public class TestaSerie {
    public static void main(String[] args) throws IOException {
        ServicoStreaming servico = new ServicoStreaming();
        servico.carregaDados();
        
        System.out.println("\n--- Dados carregados do arquivo ---\n");
        servico.listarSeriesTV();

        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\nEscolha uma opção:");
            System.out.println("1. Cadastrar nova série");
            System.out.println("2. Alterar série existente");
            System.out.println("3. Remover série");
            System.out.println("4. Listar séries após um ano");
            System.out.println("5. Listar séries por gênero");
            System.out.println("6. Listar todas as séries");
            System.out.println("7. Sair");

            int opcao = sc.nextInt();
            sc.nextLine();

            switch (opcao) {
                case 1:
                    System.out.print("Título: ");
                    String titulo = sc.nextLine();
                    System.out.print("Gênero (Comédia, Drama, Romance, Ficção): ");
                    String genero = sc.nextLine();
                    System.out.print("Número de Temporadas: ");
                    int temporadas = sc.nextInt();
                    System.out.print("Ano: ");
                    int ano = sc.nextInt();
                    System.out.print("Concluída? (true/false): ");
                    boolean concluida = sc.nextBoolean();

                    SerieTV novaSerie = new SerieTV(titulo, genero, temporadas, ano, concluida);
                    servico.adicionaSerieTV(novaSerie);
                    System.out.println("\nSérie adicionada com sucesso!\n");
                    break;

                case 2:
                    System.out.print("Informe o título da série para alterar: ");
                    String tituloAlterar = sc.nextLine();
                    System.out.print("Informe o ano da série: ");
                    int anoAlterar = sc.nextInt();
                    sc.nextLine();
                    
                    servico.removeSerieTV(tituloAlterar, anoAlterar);

                    System.out.println("Informe os novos dados da série:");
                    System.out.print("Novo título: ");
                    String novoTitulo = sc.nextLine();
                    System.out.print("Novo gênero (Comédia, Drama, Romance, Ficção): ");
                    String novoGenero = sc.nextLine();
                    System.out.print("Novo número de temporadas: ");
                    int novasTemporadas = sc.nextInt();
                    System.out.print("Novo ano: ");
                    int novoAno = sc.nextInt();
                    System.out.print("Concluída? (true/false): ");
                    boolean novaConclusao = sc.nextBoolean();

                    SerieTV novaVersao = new SerieTV(novoTitulo, novoGenero, novasTemporadas, novoAno, novaConclusao);
                    servico.adicionaSerieTV(novaVersao);

                    System.out.println("\nSérie alterada com sucesso!\n");
                    break;

                case 3:
                    System.out.print("Título da série a remover: ");
                    String tituloRemover = sc.nextLine();
                    System.out.print("Ano da série: ");
                    int anoRemover = sc.nextInt();

                    servico.removeSerieTV(tituloRemover, anoRemover);
                    System.out.println("\nSérie removida com sucesso!\n");
                    break;

                case 4:
                    System.out.print("Informe o ano: ");
                    int anoConsulta = sc.nextInt();
                    servico.listarSeriesTV(anoConsulta);
                    break;

                case 5:
                    System.out.print("Informe o gênero: ");
                    String generoConsulta = sc.nextLine();
                    System.out.println("\n--- Séries do gênero " + generoConsulta + " ---");
                    servico.listarSeriesTV(generoConsulta);
                    break;

                case 6:
                    System.out.println("\n--- Todas as séries ---");
                    servico.listarSeriesTV();
                    break;

                case 7:
                    servico.gravar();
                    System.out.println("\nDados salvos no arquivo. Saindo do sistema...");
                    sc.close();
                    return;

                default:
                    System.out.println("\nOpção inválida! Tente novamente.\n");
                    break;
            }
        }
    }
}
