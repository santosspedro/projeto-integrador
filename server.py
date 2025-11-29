import socket
from funcao_sort import funcao_sort as fs
HOST = "localhost"
PORT = 5000
def tratar_cliente(conexao: socket.socket, endereco):
    print(f"[SERVER] Cliente conectado: {endereco}")
    try:
        dados = conexao.recv(1024).decode("utf-8").strip()
        print(f"[SERVER] Mensagem recebida: '{dados}'")
        if not dados:
            print("[SERVER] Nenhum dado recebido deste cliente.")
            return
        partes = dados.split()
        numeros = [int(p) for p in partes]
        print(f"[SERVER] Lista recebida: {numeros}")
        numeros_ordenados = fs(numeros)
        print(f"[SERVER] Lista ordenada: {numeros_ordenados}")
        resposta = " ".join(str(n) for n in numeros_ordenados)
        conexao.sendall(resposta.encode("utf-8"))
        print(f"[SERVER] Resposta enviada: '{resposta}'")
    except ValueError:
        erro_msg = "ERRO: envie apenas números inteiros separados por espaço."
        conexao.sendall(erro_msg.encode("utf-8"))
        print("[SERVER] Erro ao converter para int. Mensagem de erro enviada.")
    finally:
        conexao.close()
        print(f"[SERVER] Conexão com {endereco} encerrada.")
def main():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("[SERVER] Socket criado.")
    servidor = (HOST, PORT)
    tcp.bind(servidor)
    print(f"[SERVER] Bind feito em {HOST}:{PORT}")
    tcp.listen(5)
    print("[SERVER] Aguardando conexões... (Ctrl+C para parar)")
    try:
        while True:
            conexao, endereco = tcp.accept()
            tratar_cliente(conexao, endereco)
    except KeyboardInterrupt:
        print("\n[SERVER] Encerrando servidor (Ctrl+C detectado).")
    finally:
        tcp.close()
        print("[SERVER] Socket do servidor fechado.")
if __name__ == "__main__":
    main()
