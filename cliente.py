import socket

host = 'localhost'
minha_porta = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[TCP] Socket criado.")

MEU_SERVIDOR = (host, minha_porta)

try:
    tcp.connect(MEU_SERVIDOR)
    print(f"Conectando ao servidor: {MEU_SERVIDOR}")
except ConnectionRefusedError:
    print("Não foi possível conectar ao servidor. Verifique se ele está rodando.")
    tcp.close()
    exit(1)

while True:
    insira_seus_numeros = input("Insira seus números (separados por espaço): ").strip()
    partes = insira_seus_numeros.split()

    if not partes:
        print("Nenhum número inserido. Tente novamente.")
        continue
    
    try:
        _ = [int(p) for p in partes]
        break
    except ValueError:
        print("Entrada inválida! Use apenas números inteiros separados por espaço.")
        continue  

try:
    tcp.sendall(insira_seus_numeros.encode("utf-8"))
    print(f"Mensagem enviada: {insira_seus_numeros}")

    resposta = tcp.recv(1024).decode("utf-8")

    if not resposta:
        print("Servidor não enviou resposta.")
    else:
        print(f"Resposta recebida: {resposta}")

except ConnectionResetError:
    print("A conexão foi encerrada pelo servidor.")
finally:
    tcp.close()
    print("Conexão fechada")
