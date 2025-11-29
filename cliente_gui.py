import socket
import tkinter as tk
from tkinter import messagebox

HOST = "localhost"
PORT = 5000

def enviar_numeros():
    texto = entrada_numeros.get().strip()
    if not texto:
        messagebox.showwarning("Aviso", "Insira pelo menos um número.")
        return

    partes = texto.split()
    try:
        _ = [int(p) for p in partes]
    except ValueError:
        messagebox.showerror(
            "Erro",
            "Entrada inválida!\nUse apenas números inteiros separados por espaço."
        )
        return

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))

        sock.sendall(texto.encode("utf-8"))

        resposta = sock.recv(1024).decode("utf-8")
        sock.close()
        label_resultado["text"] = f"Resposta do servidor: {resposta}"

    except ConnectionRefusedError:
        messagebox.showerror(
            "Erro",
            "Não foi possível conectar ao servidor.\n"
            "Verifique se o servidor está rodando."
        )
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

janela = tk.Tk()
janela.title("Cliente TCP - Ordenação de Números")
label_instrucao = tk.Label(
    janela,
    text="Insira seus números (separados por espaço):"
)
label_instrucao.pack(padx=10, pady=5)
entrada_numeros = tk.Entry(janela, width=50)
entrada_numeros.pack(padx=10, pady=5)
botao_enviar = tk.Button(janela, text="Enviar para o servidor", command=enviar_numeros)
botao_enviar.pack(padx=10, pady=10)
label_resultado = tk.Label(janela, text="Resposta do servidor: ")
label_resultado.pack(padx=10, pady=10)

janela.mainloop()
