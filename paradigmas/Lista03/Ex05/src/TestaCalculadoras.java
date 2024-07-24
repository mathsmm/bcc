public class TestaCalculadoras {
    private double[] numeros;
    private double base;
    private double expoente;

    public TestaCalculadoras(double[] numeros) {
        this.numeros = numeros;
    }

    public TestaCalculadoras(
            double[] numeros,
            double base,
            double expoente
    ) {
        this.numeros = numeros;
        this.base = base;
        this.expoente = expoente;
    }

    public void testarCalculadoraSimples() {
        Calculadora cs = new Calculadora();

        System.out.println(String.format("Soma dos números: %f", cs.somar(this.numeros)));
        System.out.println(String.format("Subtração dos números: %f", cs.subtrair(this.numeros)));
        System.out.println(String.format("Multiplicação dos números: %f", cs.multiplicar(this.numeros)));
        System.out.println(String.format("Divisão dos números: %f", cs.dividir(this.numeros)));
    }

    public void testarCalculadoraCientifica() {
        CalculadoraCientifica cn = new CalculadoraCientifica();

        System.out.println(String.format("Soma dos números: %f", cn.somar(this.numeros)));
        System.out.println(String.format("Subtração dos números: %f", cn.subtrair(this.numeros)));
        System.out.println(String.format("Multiplicação dos números: %f", cn.multiplicar(this.numeros)));
        System.out.println(String.format("Divisão dos números: %f", cn.dividir(this.numeros)));
        System.out.println(String.format(
                "Base %f elevada à %fª potência: %f",
                this.base, this.expoente,
                cn.potencia(this.base, this.expoente)
        ));
    }
}
