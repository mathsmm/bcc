public class TestaCasa {
    private Casa casa;

    public TestaCasa() {}

    public void criarCasa(Porta[] portas,
                          String cor) {
        this.casa = new Casa(portas, cor);
    }

    public void testarCasa() {
        System.out.println(String.format("Cor da casa: %s", this.casa.getCor()));
        this.casa.pinta("Branca");
        System.out.println(String.format("Cor da casa após mudança para 'Branca': %s", this.casa.getCor()));

        System.out.println(String.format("A porta 1 está aberta? %b", this.casa.getPorta1().estaAberta()));
        System.out.println(String.format("A porta 2 está aberta? %b", this.casa.getPorta2().estaAberta()));
        System.out.println(String.format("A porta 3 está aberta? %b", this.casa.getPorta3().estaAberta()));
        this.casa.getPorta2().abre();
        System.out.println(String.format("Estado da porta 2 após ser aberta: %b", this.casa.getPorta2().estaAberta()));
        System.out.println(String.format("Quantas portas da casa estão abertas? %d", this.casa.quantasPortasEstaoAbertas()));
    }
}
