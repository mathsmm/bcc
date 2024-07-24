import java.util.Objects;

public class Senha {
    private String senha;

    public Senha(String senha) {
        this.senha = senha;
    }

    public boolean entraSenha(String senhaDigitada, boolean mostrarMensagem) {
        if (Objects.equals(senhaDigitada, this.senha)) {
            if (mostrarMensagem) { System.out.println("Senha correta."); }
            return true;
        }
        if (mostrarMensagem) { System.out.println("Senha incorreta!"); }
        return false;
    }

    public boolean trocarSenha(String senhaAtual, String senhaNova) {
        if (this.entraSenha(senhaAtual, false)) {
            this.senha = senhaNova;
            System.out.println(String.format("Nova senha definida: %s", this.senha));
            return true;
        } else {
            System.out.println(String.format("A senha atual informada não está correta!"));
            return false;
        }
    }
}
