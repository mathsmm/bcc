import { Component } from '@angular/core';
import { ApiService } from './api-service';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  standalone: false,
  styleUrl: './app.scss'
})
export class App {
  protected title = 'FrontRedes2';
  apiUrl: string = 'https://trab-redes-2-api.zeabur.app';
  querySql: string = '';
  resposta: any;

  constructor(private apiService: ApiService) { }

  enviarQuery() {
    if (!this.apiUrl || !this.querySql) {
      alert('Preencha a URL da API e a query.');
      return;
    }

    this.resposta = "";

    this.apiService.executarQuery(this.apiUrl, this.querySql).subscribe({
      next: (data: any) => {
        this.resposta = data;
      },
      error: (error: { error: any; }) => {
        console.error('Erro ao chamar API:', error);
        this.resposta = JSON.stringify(error.error);
      }
    });
  }
}
