import java.util.Scanner;

public class Menu {

    private int tentativas = 3;

    private void resetarTentativas() {
        this.tentativas = 3;
    }
    private void diminuirDepoisMostrarTentativas() {
        System.out.println(String.format("Tentativas restantes: %d", --this.tentativas));
    }

    public void autenticarEscolha(Senha senha) {
        Scanner s = new Scanner(System.in);

        while (this.tentativas > 0) {
            int escolha = imprimirMenu();

            switch (escolha) {
                case 1: {
                    System.out.print("Digite a senha: ");
                    String senhaDigitada = s.next();

                    if (senha.entraSenha(senhaDigitada, true)) {
                        resetarTentativas();
                    } else {
                        diminuirDepoisMostrarTentativas();
                    }
                } break;
                case 2: {
                    System.out.print("Digite a senha atual: ");
                    String senhaAtual = s.next();
                    System.out.print("Digite a senha nova: ");
                    String senhaNova = s.next();

                    if (!(senha.trocarSenha(senhaAtual, senhaNova))) {
                        this.diminuirDepoisMostrarTentativas();
                    } else {
                        resetarTentativas();
                    }
                } break;
            }
        }

        System.out.println("Sua senha foi bloqueada!");
    }

    private int imprimirMenu() {
        Scanner s = new Scanner(System.in);
        System.out.println("");
        System.out.println("Opções: ");
        System.out.println("1 - Verificar senha; ");
        System.out.println("2 - Mudar senha; ");

        System.out.print("Você deseja: ");
        int resposta = Integer.parseInt(s.next());

        if (resposta == 1 || resposta == 2){
            return resposta;
        }
        else {
            System.out.println("Resposta inválida! Tente novamente.");
            return imprimirMenu();
        }
    }
}
