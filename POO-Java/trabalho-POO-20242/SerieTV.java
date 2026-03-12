public class SerieTV {
    private String titulo, genero;
    private int temporadas, ano;
    private boolean concluida;

    public SerieTV(String titulo, String gen, int temp, int ano, boolean conc) {
        this.titulo = titulo;
        setGenero(gen);
        setTemporadas(temp);
        setAno(ano);
        this.concluida = conc;
    }

    public String getGenero() {
        return genero;
    }

    public int getAno() {
        return ano;
    }

    public int getTemporadas() {
        return temporadas;
    }

    public String getTitulo() {
        return titulo;
    }

    public boolean isConcluida() {
        return concluida;
    }

    void setGenero(String gen) {
        gen = gen.toLowerCase();
        
        if (gen.equals("ficção") || gen.equals("romance") || gen.equals("comédia") || gen.equals("drama")) {
            
            if (gen.equals("ficção")) {
                this.genero = "Ficção";
            } else if (gen.equals("romance")) {
                this.genero = "Romance";
            } else if (gen.equals("comédia")) {
                this.genero = "Comédia";
            } else if (gen.equals("drama")) {
                this.genero = "Drama";
            }
        } else {
            this.genero = "Sem Classificação";
        }
    }

    void setTemporadas(int temp) {
        if (temp < 1) {
            this.temporadas = 1;
        } else {
            this.temporadas = temp;
        }
    }

    void setAno(int ano) {
        if (ano >= 2020) {
            this.ano = ano;
        } else {
            this.ano = 2020;
        }
    }

    @Override
    public boolean equals(Object o) {
        if (o == this) return true;
        if (!(o instanceof SerieTV)) return false;

        SerieTV stv = (SerieTV) o;
        return this.titulo.equals(stv.titulo) && this.ano == stv.ano;
    }

    @Override
    public String toString() {
        return "Titulo: " + this.titulo + "\nGenero: " + this.genero + "\nAno: " + this.ano +
               "\nTemporadas: " + this.temporadas + "\nConcluida: " + this.concluida + "\n";
    }

    public String getSerieTVCSV() {
        return titulo + ";" + genero + ";" + temporadas + ";" + ano + ";" + concluida;
    }

    public void setSerieTVCSV(String linha) {
        String[] campos = linha.split(";");
        this.titulo = campos[0];
        setGenero(campos[1]);
        setTemporadas(Integer.parseInt(campos[2]));
        setAno(Integer.parseInt(campos[3]));
        this.concluida = Boolean.parseBoolean(campos[4]);
    }
}
