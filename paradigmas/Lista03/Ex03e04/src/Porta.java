public class Porta {
    private boolean aberta;
    private String cor;
    private double dimensaoX;
    private double dimensaoY;
    private double dimensaoZ;

    public Porta(boolean aberta,
                 String cor,
                 double dimensaoX,
                 double dimensaoY,
                 double dimensaoZ) {
        this.aberta = aberta;
        this.cor = cor;
        this.dimensaoX = dimensaoX;
        this.dimensaoY = dimensaoY;
        this.dimensaoZ = dimensaoZ;
    }

    public void abre() {
        this.aberta = true;
    }

    public void fecha() {
        this.aberta = false;
    }

    public void pinta(String cor) {
        this.cor = cor;
    }

    public boolean estaAberta() {
        return this.aberta;
    }
}
