public class Main {
    public static void main(String[] args) {
        double[] numeros1 = {4.5, 5.5, 10.0};
        double[] numeros2 = {12.0, 2.0, 0.001};

        TestaCalculadoras t1 = new TestaCalculadoras(numeros1);
        t1.testarCalculadoraSimples();

        System.out.println("");

        TestaCalculadoras t2 = new TestaCalculadoras(
                numeros2, 2.0, 6.0
        );
        t2.testarCalculadoraCientifica();
    }
}