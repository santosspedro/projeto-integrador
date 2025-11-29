import socket
from funcao_sort import funcao_sort as fs
HOST = "0.0.0.0"
PORT = 5000
def tratar_cliente(conexao: socket.socket, endereco):
    print(f"Cliente conectado: {endereco}")
    try:
        dados = conexao.recv(1024).decode("utf-8").strip()
        print(f"Mensagem recebida: '{dados}'")
        if not dados:
            print("enhum dado recebido deste cliente.")
            return
        partes = dados.split()
        numeros = [int(p) for p in partes]
        print(f"Lista recebida: {numeros}")
        numeros_ordenados = fs(numeros)
        print(f"Lista ordenada: {numeros_ordenados}")
        resposta = " ".join(str(n) for n in numeros_ordenados)
        conexao.sendall(resposta.encode("utf-8"))
        print(f"Resposta enviada: '{resposta}'")
    except ValueError:
        erro_msg = "ERRO: envie apenas números inteiros separados por espaço."
        conexao.sendall(erro_msg.encode("utf-8"))
        print("Erro ao converter para int. Mensagem de erro enviada.")
    finally:
        conexao.close()
        print(f"Conexão com {endereco} encerrada.")
def main():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket criado.")
    servidor = (HOST, PORT)
    tcp.bind(servidor)
    print(f"Bind feito em {HOST}:{PORT}")
    tcp.listen(5)
    print("Aguardando conexões...)")
    try:
        while True:
            conexao, endereco = tcp.accept()
            tratar_cliente(conexao, endereco)
    except KeyboardInterrupt:
        print("Encerrando servidor")
    finally:
        tcp.close()
        print("Socket do servidor fechado.")
if __name__ == "__main__":
    main()
