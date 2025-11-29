import socket

host = 'localhost'
minha_porta = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[TCP] Socket criado.")

MEU_SERVIDOR = (host, minha_porta)
tcp.connect(MEU_SERVIDOR)
print(f"Conectando ao servidor: {MEU_SERVIDOR}")

insira_seus_numeros = input("Insira seus números (separados por espaço): ").strip()

partes = insira_seus_numeros.split()
try:
    _ = [int(p) for p in partes]
except ValueError:
    print("Entrada inválida! Use apenas números inteiros separados por espaço.")
    tcp.close()
    exit(1)

tcp.sendall(insira_seus_numeros.encode("utf-8"))
print(f"Mensagem enviada: {insira_seus_numeros}")

resposta = tcp.recv(1024).decode("utf-8")
print(f"Resposta recebida: {resposta}")

tcp.close()
print("Conexão fechada")
