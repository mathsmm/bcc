public class Casa {
    private Porta[] portas;
    private String cor;

    public Casa(Porta[] portas, String cor) {
        this.portas = portas;
        this.cor = cor;
    }

    public void pinta(String cor) {
        this.cor = cor;
    }

    public int quantasPortasEstaoAbertas() {
        int i = 0;
        int contador = 0;
        while (i < this.portas.length) {
            if (portas[i].estaAberta()) {
                contador++;
            }
            i++;
        }
        return contador;
    }

    public String getCor() {
        return this.cor;
    }

    public Porta getPorta1() {
        return this.portas[0];
    }

    public Porta getPorta2() {
        return this.portas[1];
    }

    public Porta getPorta3() {
        return this.portas[2];
    }
}
