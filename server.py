import socket
from funcao_sort import funcao_sort as fs

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

# receber_lista = "Envie uma lista de números separados por espaço entre eles"
# conexao.sendall(receber_lista.encode("utf-8"))]

try:
  dados = conexao.recv(1024).decode("utf-8").strip()
  print(f"Mensagem recebida: {dados}")

  if not dados:
    print("[SERVER] Nenhum dado recebido. Encerrando conexão.")
  
  partes = dados.split()
  numeros = [int(p) for p in partes]
  print(f"[SERVER] Lista de números recebida: {numeros}")

  numeros_ordenados = fs(numeros)
  print(f"[SERVER] Lista ordenada: {numeros_ordenados}")

  resposta = " ".join(str(n) for n in numeros_ordenados)

  resposta = "Recebido"
  conexao.sendall(resposta.encode("utf-8"))
  print(f"Resposta enviada: {resposta}")
except ValueError:
  erro_msg = "ERRO: envie apenas números inteiros separados por espaço."
  conexao.sendall(erro_msg.encode("utf-8"))
  print("[SERVER] Erro de conversão para int. Mensagem de erro enviada ao cliente.")

finally:
  conexao.close()
  tcp.close()
  print("Conexão fechada")