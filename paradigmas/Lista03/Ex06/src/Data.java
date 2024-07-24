import java.time.Instant;

public class Data {
    private int dia;
    private int mes;
    private int ano;
    private int[] qtdDiasEmCadaMes = {
            31, 28, 31, 30,
            31, 30, 31, 31,
            30, 31, 30, 31
    };

    public Data(int dia, int mes, int ano) {
        this.verificarSeAnoBissexto(ano);
        if (!this.verificarValidade(dia, mes)) {
            this.dia = 1;
            this.mes = 1;
            this.ano = 1899;
            return;
        }
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }

    public void verificarSeAnoBissexto(int ano) {
        if      (ano % 400 == 0) {this.qtdDiasEmCadaMes[1] = 29;}
        else if (ano % 100 == 0) {return;}
        else if (ano % 4   == 0) {this.qtdDiasEmCadaMes[1] = 29;}
    }

    public boolean verificarValidade(int dia, int mes) {
        if ((mes < 1 || mes > 12) ||
            (dia > this.qtdDiasEmCadaMes[mes - 1])) {
            return false;
        }
        return true;
    }

    public String imprimir() {
        return String.format("%d/%d/%d", this.dia, this.mes, this.ano);
    }

    public void proximoDia() {
        this.dia++;
        if (this.dia > this.qtdDiasEmCadaMes[this.mes - 1]) {
            this.dia = 1;
            this.mes++;
            if (this.mes > 12) {
                this.mes = 1;
                this.ano++;
            }
        }
    }
}
