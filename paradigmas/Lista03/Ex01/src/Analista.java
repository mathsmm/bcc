public class Analista extends Funcionario implements IFuncionario{


    public Analista(String nome, int idade) {
        super(nome, idade);
    }

    @Override
    public double retornarSalario() {
        return 6600.45;
    }
}
