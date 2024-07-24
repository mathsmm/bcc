public class TestaData {

    public TestaData() {}

    public void testarData() {
        Data d1 = new Data(1, 1, 2000);
        Data d2 = new Data(31, 7, 2022);
        Data d3 = new Data(28, 2, 2024);
        Data d4 = new Data(31, 12, 1990);
        Data d5 = new Data(32, 12, 1990);

        Data[] datas = {d1, d2, d3, d4, d5};

        int i = 0;
        while (i < datas.length) {
            System.out.println(String.format("Data %d ", i + 1) + "- " + datas[i].imprimir());
            datas[i].proximoDia();
            System.out.println(String.format("Data %d ", i + 1) + "depois de ter um dia incrementado: " + datas[i].imprimir());
            i++;
        }
    }
}
