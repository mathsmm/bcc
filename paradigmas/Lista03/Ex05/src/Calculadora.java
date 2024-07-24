public class Calculadora {

    public Calculadora() {}

    public double somar(double[] numeros) {
        double resultado = 0;
        int i = 0;
        while (i < numeros.length) {
            resultado = resultado + numeros[i];
            i++;
        }
        return resultado;
    }

    public double subtrair(double[] numeros) {
        double resultado = 0;
        int i = 0;
        while (i < numeros.length) {
            resultado = resultado - numeros[i];
            i++;
        }
        return resultado;
    }

    public double multiplicar(double[] numeros) {
        double resultado = numeros[0];
        int i = 1;
        while (i < numeros.length) {
            resultado = resultado * numeros[i];
            i++;
        }
        return resultado;
    }

    public double dividir(double[] numeros) {
        double resultado = numeros[0];
        int i = 1;
        while (i < numeros.length) {
            resultado = resultado / numeros[i];
            i++;
        }
        return resultado;
    }
}
