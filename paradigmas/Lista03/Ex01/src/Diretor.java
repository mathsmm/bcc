public class Diretor extends Funcionario implements IFuncionario{


    public Diretor(String nome, int idade) {
        super(nome, idade);
    }

    @Override
    public double retornarSalario() {
        return 7272.50;
    }
}
