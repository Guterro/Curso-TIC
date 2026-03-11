import java.io.*;
import java.util.*;

public class ServicoStreaming {
    private ArrayList<SerieTV> lista;

    public ServicoStreaming() {
        this.lista = new ArrayList<>();
    }

    public void adicionaSerieTV(SerieTV stv) {
        if (!lista.contains(stv)) {
            lista.add(stv);
        }
    }

    public void removeSerieTV(SerieTV stv) {
        lista.remove(stv);
    }

    public void removeSerieTV(String titulo, int ano) {
        for (int i = 0; i < lista.size(); i++) {
            SerieTV serie = lista.get(i);
            if (serie.getTitulo().equals(titulo) && serie.getAno() == ano) {
                lista.remove(i);
                break;
            }
        }
    }

    public void gravar() throws IOException {
        File arq = new File("servicostreaming.csv");
        BufferedWriter arqw = new BufferedWriter(new FileWriter(arq));

        for (SerieTV stv : lista) {
            arqw.write(stv.getSerieTVCSV());
            arqw.newLine();
        }
        arqw.close();
    }

    public void carregaDados() throws IOException {
        File arq = new File("servicostreaming.csv");
        if (!arq.exists()) {
            return;
        }

        BufferedReader arqr = new BufferedReader(new FileReader(arq));
        String linha;

        while ((linha = arqr.readLine()) != null) {
            SerieTV stv = new SerieTV("", "", 2020, 1, false);
            stv.setSerieTVCSV(linha);
            adicionaSerieTV(stv);
        }

        arqr.close();
    }
    
    public void listarSeriesTV(String genero) {
        for (SerieTV serie : lista) {
            if (serie.getGenero().equals(genero)) {
                System.out.println(serie);
            }
        }
    }
    
    public void listarSeriesTV(int ano) {
        for (SerieTV serie : lista) {
            if (serie.getAno() >= ano) {
                System.out.println(serie);
            }
        }
    }
    
    public void listarSeriesTV() {
        for (SerieTV serie : lista) {
            System.out.println(serie);
        }
    }
}