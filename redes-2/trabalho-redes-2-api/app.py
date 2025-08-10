from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_HOST = 'dpg-d1g589ngi27c73eg39og-a.oregon-postgres.render.com'
DB_USER = 'redes2user'
DB_NAME = 'redes2'
DB_PASSWORD = 'cux1vS5Qh6vWv6tUhMjlkz2dw5Uckzci'

class QueryRequest(BaseModel):
    query: str

def executar_psql_comando(query: str) -> str:
    comando = [
        'psql',
        '-h', DB_HOST,
        '-U', DB_USER,
        '-d', DB_NAME,
        '-c', query
    ]

    env = {
        'PGPASSWORD': DB_PASSWORD,
        **dict(**subprocess.os.environ)
    }

    try:
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            env=env
        )

        if resultado.returncode != 0:
            raise Exception(f"{resultado.stderr}")

        return resultado.stdout

    except Exception as e:
        return str(e)

@app.post("/executar-query/")
def executar_query(request: QueryRequest):
    try:
        resultado = executar_psql_comando(request.query)
        return {"resultado": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))