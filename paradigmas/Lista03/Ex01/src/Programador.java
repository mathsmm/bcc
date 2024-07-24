public class Programador extends Funcionario implements IFuncionario{


    public Programador(String nome, int idade) {
        super(nome, idade);
    }

    @Override
    public double retornarSalario() {
        return 2990.00;
    }
}
