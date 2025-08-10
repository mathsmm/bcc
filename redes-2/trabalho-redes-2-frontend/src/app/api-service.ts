import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  executarQuery(apiUrl: string, query: string): Observable<any> {
    const url = `${apiUrl}/executar-query/`;

    const headers = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    const body = {
      query: query
    };

    return this.http.post(url, body, { headers });
  }
}
