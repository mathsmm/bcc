public abstract class Funcionario implements IFuncionario {
    protected String nome;
    protected int idade;

    public Funcionario(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    @Override
    public abstract double retornarSalario();
}
