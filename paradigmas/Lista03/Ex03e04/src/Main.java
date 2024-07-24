public class Main {

    public static void main(String[] args) {

        Porta p1 = new Porta(
                true,
                "Cinza",
                1.2,
                2.0,
                0.05
        );

        Porta p2 = new Porta(
                false,
                "Marrom escura",
                1.5,
                3.0,
                0.10
        );

        Porta p3 = new Porta(
                false,
                "Branca",
                0.8,
                1.2,
                0.03
        );

        Porta[] portas = {p1, p2, p3};

        TestaCasa testaCasa = new TestaCasa();
        testaCasa.criarCasa(portas, "Amarela");
        testaCasa.testarCasa();
    }
}