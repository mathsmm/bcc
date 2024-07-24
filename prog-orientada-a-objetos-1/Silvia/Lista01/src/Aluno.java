public class Aluno {
    private int matricula;
    private String nome;
    private float prova1;
    private float prova2;
    private float trabalho;

    public Aluno(int matricula, String nome, float prova1, float prova2, float trabalho) {
        this.matricula = matricula;
        this.nome = nome;
        this.prova1 = prova1;
        this.prova2 = prova2;
        this.trabalho = trabalho;
    }

    public float calcularMedia() {
        return ((this.prova1 + this.prova2) * 4 + this.trabalho * 2) / 10;
    }

    public String retornarSituacao() {
        String mensagem = "";
        if (this.calcularMedia() < 6.0) { mensagem = "Em recuperação."; }
        else if (this.calcularMedia() >= 6.0) { mensagem = "Aprovado."; }
        return mensagem;
    }
}
