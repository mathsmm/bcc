import socket
import threading

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 65433
BUFFER_SIZE = 1024

# Lista de conexões ativas
clients = {}
clients_lock = threading.Lock()

def broadcast(sender_socket, message):
    """Envia mensagem para todos os clientes exceto o emissor"""
    with clients_lock:
        for socket, nickname in clients.items():
            if socket != sender_socket:
                try:
                    socket.send(message)
                except:
                    # Se falhar, fecha a conexão
                    socket.close()
                    # Remove da lista de clientes (será removido no próximo loop)

def handle_client_connection(client_socket, client_address):
    """Gerencia a conexão com um cliente específico"""
    # Adiciona cliente com nome padrão
    with clients_lock:
        clients[client_socket] = f"user_{client_address[0]}_{client_address[1]}"

    # Envia mensagem de boas-vindas
    welcome = f"Bem-vindo ao chat! Você está conectado como {clients[client_socket]}\n"
    welcome += "Comandos disponíveis:\n/nick <nome> - Alterar seu nome\n/quit - Sair do chat\n"
    client_socket.send(welcome.encode('utf-8'))
    
    # Anuncia novo usuário
    broadcast(client_socket, f">>> {clients[client_socket]} entrou no chat <<<\n".encode('utf-8'))

    while True:
        try:
            # Recebe dados do cliente
            data = client_socket.recv(BUFFER_SIZE)
            if data:
                # Processa a mensagem
                message = data.decode('utf-8').strip()

                # Comando para alterar nickname
                if message.startswith('/nick '):
                    with clients_lock:
                        new_nickname = message[6:].strip()
                        old_nickname = clients[client_socket]
                        clients[client_socket] = new_nickname
                    client_socket.send(f"Seu nome foi alterado para {new_nickname}\n".encode('utf-8'))
                    broadcast(client_socket, f">>> {old_nickname} agora é conhecido como {new_nickname} <<<\n".encode('utf-8'))

                # Comando para sair
                elif message == '/quit':
                    with clients_lock:
                        nickname = clients[client_socket]
                        del clients[client_socket]
                    broadcast(client_socket, f">>> {nickname} saiu do chat <<<\n".encode('utf-8'))
                    client_socket.close()
                    break

                # Mensagem normal
                else:
                    with clients_lock:
                        nickname = clients[client_socket]
                    broadcast_msg = f"{nickname}: {message}\n"
                    broadcast(client_socket, broadcast_msg.encode('utf-8'))
            else:
                # Desconexão do cliente
                with clients_lock:
                    if client_socket in clients:
                        nickname = clients[client_socket]
                        del clients[client_socket]
                broadcast(client_socket, f">>> {nickname} saiu do chat <<<\n".encode('utf-8'))
                client_socket.close()
                break
        except:
            # Em caso de erro, remove o cliente
            with clients_lock:
                if client_socket in clients:
                    nickname = clients[client_socket]
                    del clients[client_socket]
            broadcast(client_socket, f">>> {nickname} saiu do chat <<<\n".encode('utf-8'))
            client_socket.close()
            break

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    print(f"Servidor de chat iniciado em {HOST}:{PORT}")

    try:
        while True:
            # Aceita nova conexão
            client_socket, addr = server_socket.accept()
            print(f"Nova conexão de {addr}")

            # Inicia uma thread para lidar com o cliente
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, addr))
            client_thread.daemon = True
            client_thread.start()
    except KeyboardInterrupt:
        print("\nServidor encerrado")
    finally:
        with clients_lock:
            for client in clients:
                try:
                    client.close()
                except:
                    pass
        server_socket.close()

if __name__ == "__main__":
    main()