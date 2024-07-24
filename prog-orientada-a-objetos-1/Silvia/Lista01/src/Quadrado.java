public class Quadrado {

    private double lado;

    public Quadrado(double lado) {
        this.lado = lado;
    }

    public double calcularArea() {
        return this.lado * this.lado;
    }

    public double calcularPerimetro() {
        return this.lado * 4;
    }

    public void imprimir() {
        System.out.println(String.format("Área do quadrado: %f ", this.calcularArea()));
        System.out.println(String.format("Perímetro do quadrado: %f ", this.calcularPerimetro()));
    }
}
