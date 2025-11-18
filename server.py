import socket

host = 'localhost'

minha_porta = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[TCP] Socket criado.")

teste_mensagem = ''

MEU_SERVIDOR = (host, minha_porta)
tcp.bind(MEU_SERVIDOR)
print(f"[SERVER] Bind feito em {host}:{minha_porta}")

tcp.listen(1)
print("[SERVER] Aguardando conexão do cliente...")

conexao, docliente = tcp.accept()
print("O cliente = ", docliente, "se conectou")

dados = conexao.recv(1024).decode("utf-8")
print(f"Mensagem recebida: {dados}")

resposta = "Recebido"
conexao.sendall(resposta.encode("utf-8"))
print("Resposta enviada")

conexao.close()
tcp.close()
print("Conexão fechada")

# while 1:
#   mensagem_recebida = conexao.recv(1024)
#   if teste_mensagem != mensagem_recebida:
#     print("Recebi = ", mensagem_recebida, " , do cliente ", docliente)

    # conexao.close()