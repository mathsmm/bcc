# importar a biblioteca flask
from flask import Flask, request, jsonify
# biblioteca CORS
from flask_cors import CORS
import os
import json
import uuid
SERVER_DIR = "./files/"
import sys
porta = sys.argv[1]

class File:
    # construtor com valor padrão nos parâmetros
    def __init__(self, name="", id="", modified=""):
        self.name = name
        self.id = id
        self.modified = modified

    # expressar a classe em formato texto
    def __str__(self):
        return f'{self.name}, '+\
               f'{self.id}, {self.modified}'

    # expressar a classe em formato json
    def json(self):
        return {
            "name" : self.name,
            "id" : self.id,
            "modified" : self.modified 
        }

# acesso ao flask via variável app
app = Flask(__name__)

# inserindo a aplicação em um contexto
# https://flask.palletsprojects.com/en/2.2.x/appcontext
with app.app_context():

    # aplicando tratamento CORS ao flask
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app)

    # rota padrão
    @app.route("/")
    def ola():
        return "<b>Olá, gente!</b>"

    # rota de listar pessoas
    @app.route("/listar")
    def listar():
        try:
            # cria a lista de retorno que sera usada para gerar o json
            # obtem lista dos arquivos do diretŕio atual
            dir_entries = os.scandir(SERVER_DIR)
            lista_files: 'list[File]' = []
            # percorre a lista de entradas
            for entry in dir_entries:
                # obtem status referente ao arquivo e grava na lista
                fileStatus = entry.stat()
                file = File(entry.name, str(fileStatus.st_ino), str(fileStatus.st_mtime))
                print(file)
                lista_files.append(file)

            lista_retorno: 'list[dict[str, str]]' = []
            # percorrer a lista de arquivos e tranforma em json
            for file in lista_files:
                lista_retorno.append(file.json())

            # preparar uma parte da resposta: resultado ok
            meu_json: 'dict[str, str | list[dict[str, str]]]' = {"header": "OK"}
            meu_json.update({"files": lista_retorno})

            return meu_json
        except Exception as e:
            return {"header": "erro", "files": str(e)}

    @app.route("/criar/<file_name>")
    def criar(file_name):
        try:
            uuidid = str(uuid.uuid4())+"."+file_name.split(".")[1]
            newFile = open(SERVER_DIR + uuidid, "x")
            newFile.close()
            entry = os.stat(SERVER_DIR + uuidid)
            json_object = {}
            with open('diretorios.json', 'r') as openfile:
                # Reading from json file
                json_object = json.load(openfile)

            print(uuidid)
            json_object[file_name] = uuidid

            json_object = json.dumps(json_object, indent=4)

            with open("diretorios.json", "w") as outfile:
                outfile.write(json_object)
            file = File(uuidid, entry.st_ino, entry.st_mtime)

            resposta = jsonify({"header": "OK", "UFID": uuidid})
        except Exception as e:
            resposta = jsonify({"header": "erro", "detail": e})

        return resposta

    @app.route("/deletar/<file_name>")
    def deletar(file_name):
        try:
            os.remove(SERVER_DIR + file_name)
            resposta = jsonify({"header": "OK", "deatil": file_name + ' deleted'})
        except Exception as e:
            resposta = jsonify({"header": "erro", "detail": str(e)})

        return resposta

    # Rota antiga - usando método GET
    @app.route("/escrever_antigo/<file_name>/<conteudo>")
    def escrever_antigo(file_name, conteudo):
        try:
            openedFile = open(SERVER_DIR + file_name, "w")
            openedFile.write(conteudo)
            openedFile.close()
            print(conteudo)
            resposta = jsonify({"header": "OK", "detail": "success!"})
        except Exception as e:
            resposta = jsonify({"header": "erro", "detail": str(e)})
        return resposta
    
    # Para testar a rota: curl -i -X POST -F files=@nome_arquivo http://127.0.0.1:5000/escrever
    @app.route("/escrever", methods=['POST'])
    def escrever():
        try:
            f = request.files['files']
            print(f.filename)
            f.save(SERVER_DIR + f.filename)
            resposta = jsonify({"header": "OK", "detail": "success!"})
        
        except Exception as e:
            resposta = jsonify({"header": "erro", "detail": str(e)})
        
        return resposta


    @app.route("/ler/<file_name>")
    def ler(file_name):
        try:
            retorno = ""
            with open('diretorios.json', 'r') as openfile:
                # Reading from json file
                json_object = json.load(openfile)
                retorno = json_object[file_name]

            openedFile = open(SERVER_DIR + retorno, "r")
            conteudo = openedFile.read()
            openedFile.close()

            resposta = jsonify({"header": "OK", "detail": conteudo, "UFID": retorno})
        except Exception as e:
            resposta = jsonify({"header": "erro", "detail": str(e)})
        return resposta

    app.run(debug=True, host='0.0.0.0', port = porta)
    # para depurar a aplicação web no VSCode, é preciso remover debug=True
    # https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app


'''
resultado da invocação ao servidor:

curl localhost:5000/listar


'''