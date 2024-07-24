public class Eleitor {
    private String nome;
    private int idade;
    
    public Eleitor(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }
    
    public String verificar() {
        String mensagem = "";

        if (this.idade < 16) {
            mensagem = String.format(
                    "%s ainda não pode votar. Tem apenas %d anos de idade.",
                    this.nome, this.idade
            );
        } else if (this.idade >= 18 && this.idade <= 65) {
            mensagem = String.format(
                    "%s tem %d anos de idade. Deve votar.",
                    this.nome, this.idade
            );
        } else {
            mensagem = String.format(
                    "%s tem %d anos de idade. Voto facultativo.",
                    this.nome, this.idade
            );
        }

        return mensagem;
    }
}
