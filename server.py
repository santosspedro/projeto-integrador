import socket
from funcao_sort import funcao_sort as fs

HOST = "localhost"
PORT = 5000

def tratar_cliente(conexao, endereco):
    print("O cliente = ", endereco, "se conectou")

    try:
        dados = conexao.recv(1024).decode("utf-8").strip()
        print(f"Mensagem recebida: {dados}")

        if not dados:
            print("[SERVER] Nenhum dado recebido deste cliente.")
            return

        partes = dados.split()
        numeros = [int(p) for p in partes]
        print(f"[SERVER] Lista de números recebida: {numeros}")

        numeros_ordenados = fs(numeros)
        print(f"[SERVER] Lista ordenada: {numeros_ordenados}")

        resposta = " ".join(str(n) for n in numeros_ordenados)
        conexao.sendall(resposta.encode("utf-8"))
        print(f"Resposta enviada: {resposta}")

    except ValueError:
        erro_msg = "ERRO: envie apenas números inteiros separados por espaço."
        conexao.sendall(erro_msg.encode("utf-8"))
        print("[SERVER] Erro de conversão para int. Mensagem de erro enviada ao cliente.")
    finally:
        conexao.close()
        print("Conexão com o cliente encerrada.")


def main():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("[TCP] Socket criado.")

    MEU_SERVIDOR = (HOST, PORT)
    tcp.bind(MEU_SERVIDOR)
    print(f"[SERVER] Bind feito em {HOST}:{PORT}")

    tcp.listen(5)
    print("[SERVER] Aguardando conexão do cliente...")

    while True:
        conexao, docliente = tcp.accept()
        tratar_cliente(conexao, docliente)

if __name__ == "__main__":
    main()