import socket
import threading
import sys

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 65433
BUFFER_SIZE = 1024

def receive_messages(sock):
    """Função para receber mensagens do servidor em uma thread separada"""
    while True:
        try:
            data = sock.recv(BUFFER_SIZE)
            if not data:
                print("\nConexão com o servidor perdida!")
                sock.close()
                sys.exit(1)
            print(data.decode('utf-8'), end='')
        except:
            print("\nErro ao receber mensagem do servidor")
            sock.close()
            sys.exit(1)

def main():
    # Criação do socket TCP/IP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print(f"Conectado ao servidor de chat em {HOST}:{PORT}")

        # Inicia thread para receber mensagens
        receive_thread = threading.Thread(target=receive_messages, args=(s,))
        receive_thread.daemon = True
        receive_thread.start()

        # Loop principal para enviar mensagens
        while True:
            try:
                message = input()
                s.send(message.encode('utf-8'))
                if message == '/quit':
                    break
            except KeyboardInterrupt:
                s.send('/quit'.encode('utf-8'))
                break
            except:
                print("Erro ao enviar mensagem")
                break

        s.close()

    except ConnectionRefusedError:
        print("Erro: Não foi possível conectar ao servidor. Verifique se o servidor está em execução.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()