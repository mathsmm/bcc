public class CalculadoraCientifica extends Calculadora {

    public CalculadoraCientifica() {}

    public double potencia(double base, double expoente) {
        double resultado = base;
        int i = 1;
        while (i < expoente) {
            resultado = resultado * base;
            i++;
        }
        return resultado;
    }
}
