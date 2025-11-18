import socket
from funcao_sort import funcao_sort as fs

host = 'localhost'

minha_porta = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[TCP] Socket criado.")

MEU_SERVIDOR = (host, minha_porta)
tcp.connect(MEU_SERVIDOR)
print(f"Conectando ao servidor: {MEU_SERVIDOR}")

insira_seus_numeros = input("Insira seus números: ")
tcp.sendall(insira_seus_numeros.encode("utf-8"))
print(f"Mensagem enviada: {insira_seus_numeros}")

resposta = tcp.recv(1024).decode("utf-8")
print(f"Resposta recebida: {resposta}")

tcp.close()
print("Conexão fechada")

