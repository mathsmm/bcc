import socket
import threading

SERVER_HOSTNAME = "prog27" # Nome da máquina do servidor
OWN_HOSTNAME = socket.gethostname()
SERVER_PORT = 22222 # Porta do servidor
CLIENT_PORT = 22223
DATA_PAYLOAD = 1024 # O payload máximo de dados para ser recebido em 'uma tacada só'

SERVER_COMMAND_LIST = \
    "l - See the client list\n" + \
    "w - Wait for client connection\n" + \
    "e - Exit. Closes connection\n" + \
    "Choose one of the options above"

def client():

    def connect_to_server():
        host = socket.gethostbyname(SERVER_HOSTNAME)
        s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
        s.connect((host, SERVER_PORT))
        return s, host
    
    def receive_message_from_server(pr_server: socket.socket):
        decoded = ""
        while True:
            msg = pr_server.recv(DATA_PAYLOAD)
            decoded += msg.decode("utf-8")
            if len(msg) < DATA_PAYLOAD:
                break
        return decoded
    
    def connect_to_client(ip: str, port: int): 
        s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
        s.connect((ip, port))
        return s
    
    def receive_message_from_client(pr_client: socket.socket):
        decoded = ""
        while True:
            msg = pr_client.recv(DATA_PAYLOAD)
            decoded += msg.decode("utf-8")
            if len(msg) < DATA_PAYLOAD:
                break
        return decoded

    def open_socket_for_client():
        host = socket.gethostbyname(OWN_HOSTNAME)
        s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
        s.bind((host, CLIENT_PORT))
        return s

    server, host = connect_to_server() # Inicia a conexão com o servidor
    print(f"Server connected at {host}:{SERVER_PORT}")
    print("SERVER >> " + receive_message_from_server(server)) # Deve imprimir 'You are connected to the server'

    other_client_addr = ""
    other_client_port = 0
    other_client_number = 0
    step = 0
    decoded = ""

    # Etapa 0 -> vendo lista de comandos
    # Etapa 1 -> vendo lista de clientes
    # Etapa 2 -> esperando conexão de alguém
    # Etapa 3 -> vai se conectar a outro cliente -> é o REQUESTER
    # Etapa 4 -> vai se conectar a outro cliente -> é o REQUESTED
    while True:
        if step == 0: # Está na etapa de ver os comandos do servidor
            print(SERVER_COMMAND_LIST) # Imprime os comandos do servidor
            option = input().strip() # Pede a opção ao usuário

            if (option != "l") and (option != "e") and (option != "w"):
                print("Invalid option")
                continue # Pede a opção novamente ao usuário
            
            server.sendall(option.encode("utf-8")) # Envia a opção para o servidor
            
            decoded = receive_message_from_server(server)
            print("SERVER >> " + decoded)

            if decoded == "You are disconnected": # Cliente enviou 'e' e foi desconectado
                print("Finishing program")
                return
            elif decoded == "No one available": # Cliente enviou 'l' e não tem ninguém pra se conectar
                print("Wait for someone to connect to the server")
                continue
            elif decoded == "Now you are visible to others": # Cliente enviou 'w'
                step = 2
                continue
            else: # Cliente enviou 'l' e recebeu a lista dos clientes disponíveis
                step = 1
                continue
        elif step == 1: # Está na etapa de receber a lista de clientes
            client_list = decoded.split(", ")

            while True:
                print("Choose one of the items above or 'c' to cancel and go back")
                option = input().strip() # Pede o número do cliente ao usuário
                if (option not in client_list) and (option != "c"):
                    print("Invalid option")
                    continue # Pede a opção novamente ao usuário
                elif option == "c":
                    server.sendall(option.encode("utf-8")) # Envia a opção para o servidor
                    decoded = receive_message_from_server(server)
                    print("SERVER >> " + decoded)
                    step = 0
                    break
                else:
                    server.sendall(option.encode("utf-8")) # Envia a opção para o servidor
                    print("SERVER >> " + receive_message_from_server(server)) # 'SERVER >> Asking for connection...'
                    other_client_number = int(option)

                    decoded = receive_message_from_server(server) # Aceitação ou recusa
                    print("SERVER >> " + decoded)
                    if decoded == "Request refused": # Recusado
                        step = 0
                        break # Sai deste laço e volta a printar a lista de comandos
                    else: # Aceito. Vem o endereço e a porta do outro cliente
                        decoded = decoded.split(":")
                        other_client_addr = decoded[0]
                        other_client_port = decoded[1]
                        step = 3
                        break
        elif step == 2: # Está na etapa de esperar por conexão de algum outro cliente
            print("Waiting for connetion from other client...")
            decoded = receive_message_from_server(server)

            while True:
                print("SERVER >> " + decoded)
                decoded = decoded[7:]
                decoded = decoded[:decoded.index(" ")]
                other_client_number = int(decoded)
                print("Choose 'y' to accept or 'n' to refuse")
                option = input().strip() # Pede a opção ao usuário
                if (option != "y") and (option != "n"):
                    print("Invalid option")
                    continue
                elif (option == "y"):
                    server.sendall(option.encode("utf-8")) # Envia 'y' para o servidor
                    step = 4
                    break
                elif (option == "n"):
                    server.sendall(option.encode("utf-8")) # Envia 'n' para o servidor
                    break
        elif step == 3: # Está na etapa de se conectar a outro cliente. É O REQUESTER
            other_client = connect_to_client(other_client_addr, int(other_client_port))
            print(f"Connected to client {other_client_number}. Address/Port: ({other_client_addr}:{other_client_port})")
            break
        elif step == 4: # Está na etapa de se conectar a outro cliente. É O REQUESTED
            # REQUESTED DEVE ABRIR O SOCKET E FUNCIONAR COMO UM "SERVIDOR"
            s = open_socket_for_client()
            s.listen(1)
            other_client, other_client_addr = s.accept()
            print(f"Connected to client {other_client_number}. Address/Port: {other_client_addr}")
            break

    def recebendo():
        while True:
            decoded = receive_message_from_client(other_client)
            print(f"Client {other_client_number} >> " + decoded)

    def enviando():
        while True:
            msg = input()
            encoded = msg.encode('utf-8')
            other_client.sendall(encoded)
            print("SENT:", msg)

    # Inicia as threads
    thread_recebendo = threading.Thread(target=recebendo)
    thread_enviando = threading.Thread(target=enviando)

    thread_recebendo.start()
    thread_enviando.start()

    print("Ready to listen and send messages!")


def main():
    client()

if __name__ == "__main__":
    main()