import socket
import threading
import sys
import time

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 65433
BUFFER_SIZE = 1024
TIMEOUT = 10 # (MELHORIA 1) TIMEOUT

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
        # (MELHORIA 1) TIMEOUT
        except socket.timeout:
            print("\nTimeout: O servidor não respondeu a tempo.")
            sock.close()
            sys.exit(1)
        except:
            print("\nErro ao receber mensagem do servidor")
            sock.close()
            sys.exit(1)

# (MELHORIA 2) VALIDA MENSAGEM DO USUÁRIO
def validate_message(message):
    if len(message) == 0:
        print("Mensagem vazia")
        return False
    if "lula" in message:
        print("A palavra 'lula' é uma maldição. Guarde-a para si")
        return False
    if message.startswith("/"):
        if not message.startswith("/nick ") and message not in ["/quit"]:
            print("Comando inválido. Utilizar '/nick' ou '/quit'")
            return False
    return True

# (MELHORIA 3) TENTA SE RECONECTAR AO SERVIDOR
def attempt_reconnect(s, retries=5, delay=5):
    for attempt in range(retries):
        try:
            print(f"Tentando reconectar ao servidor... (Tentativa {attempt + 1}/{retries})")
            s.connect((HOST, PORT))
            print(f"Reconectado ao servidor {HOST}:{PORT}")
            return True
        # (MELHORIA 1) TIMEOUT
        except (ConnectionRefusedError, socket.timeout) as e:
            print(f"Erro: {e}")
            time.sleep(delay) 
    print(f"Falha ao reconectar após {retries} tentativas.")
    return False

def main():
    # Criação do socket TCP/IP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)  # (MELHORIA 1) TIMEOUT

        # (MELHORIA 3) TENTA SE RECONECTAR AO SERVIDOR
        if not attempt_reconnect(s):
            sys.exit(1)

        # try:
        #     s.connect((HOST, PORT))
        # # (MELHORIA 1) TIMEOUT
        # except socket.timeout:
        #     print("Timeout ao conectar no servidor")
        #     sys.exit(1)

        print(f"Conectado ao servidor de chat em {HOST}:{PORT}")

        # Inicia thread para receber mensagens
        receive_thread = threading.Thread(target=receive_messages, args=(s,))
        receive_thread.daemon = True
        receive_thread.start()

        # Loop principal para enviar mensagens
        while True:
            try:
                message = input()

                # (MELHORIA 2) VALIDA MENSAGEM DO USUÁRIO
                if not validate_message(message):
                    continue
                
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