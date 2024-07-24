public class Main {
    public static void main(String[] args) {
//        //EXERCÍCIO 1:
//        Quadrado q1 = new Quadrado(5);
//        q1.imprimir();
//        Quadrado q2 = new Quadrado(8.7);
//        q2.imprimir();


//        //EXERCÍCIO 2:
//        Eleitor e1 = new Eleitor("Thomas", 17);
//        Eleitor e2 = new Eleitor("Jefferson", 22);
//        Eleitor e3 = new Eleitor("André", 68);
//        Eleitor e4 = new Eleitor("Samara", 15);
//        Eleitor e5 = new Eleitor("Helaine", 18);
//
//        Eleitor eleitores[] = {e1, e2, e3, e4, e5};
//        int i = 0;
//        while (i < eleitores.length) {
//            System.out.println(eleitores[i].verificar());
//            i++;
//        }


        //EXERCÍCIO 3:
        Aluno a1 = new Aluno(
                1,
                "Fulano",
                (float)5.0,
                (float)5.5,
                (float)2.0
        );

        Aluno a2 = new Aluno(
                2,
                "Ciclano",
                (float)7.0,
                (float)8.5,
                (float)3.0
        );

        Aluno a3 = new Aluno(
                3,
                "Beltrano",
                (float)9.5,
                (float)10.0,
                (float)9.0
        );

        Aluno alunos[] = {a1, a2, a3};
        int i = 0;
        while (i < alunos.length) {
            System.out.println(String.format("Aluno %d", i + 1));
            System.out.println(String.format("Média: %f", alunos[i].calcularMedia()));
            System.out.println(alunos[i].retornarSituacao());
            System.out.println("");
            i++;
        }

    }
}