import socket

# Configurações do cliente
HOST = '127.0.0.1' # Endereço do servidor
PORT = 65432 # Porta do servidor

try:
    # Criação do socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Conecta ao servidor
        s.connect((HOST, PORT))
        print(f"Conectado ao servidor {HOST}:{PORT}")

        # Loop para enviar mensagens
        while True:
            # Solicita mensagem ao usuário
            message = input("Digite uma mensagem (ou 'sair' para encerrar): ")

            # Verifica se usuário quer encerrar
            if message.lower() == 'sair':
                break

            # Envia a mensagem codificada em bytes
            s.sendall(message.encode('utf-8'))

            # Recebe a resposta do servidor
            data = s.recv(1024)
            print(f"Resposta do servidor: {data.decode('utf-8')}")

    print("Conexão encerrada")
except ConnectionRefusedError:
    print("Erro: Não foi possível conectar ao servidor. Verifique se o servidor está em execução.")
except Exception as e:
    print(f"Erro: {e}")