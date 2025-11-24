import socket
import tkinter as tk
from tkinter import messagebox

class ClienteGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cliente - Ordenação de Números")
        master.geometry("400x300")

        self.sock = None
        self.conectado = False

        self.label = tk.Label(master, text="Digite números separados por espaço:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(master, width=40)
        self.entry.pack(pady=5)

        self.btn_conectar = tk.Button(master, text="Conectar ao Servidor", command=self.conectar)
        self.btn_conectar.pack(pady=5)

        self.btn_enviar = tk.Button(master, text="Enviar", command=self.enviar, state="disabled")
        self.btn_enviar.pack(pady=5)

        self.output = tk.Text(master, height=8, width=45)
        self.output.pack(pady=5)

    def conectar(self):
        if self.conectado:
            return

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(("localhost", 5000))
            self.conectado = True
            self.output.insert(tk.END, "Conectado ao servidor!\n")
            self.btn_enviar.config(state="normal")
        except:
            messagebox.showerror("Erro", "Não foi possível conectar ao servidor.")

    def enviar(self):
        if not self.conectado:
            messagebox.showwarning("Aviso", "Conecte ao servidor primeiro.")
            return

        numeros = self.entry.get().strip()

        if not numeros:
            messagebox.showwarning("Aviso", "Digite os números!")
            return

        try:
            self.sock.sendall(numeros.encode("utf-8"))
            resposta = self.sock.recv(1024).decode("utf-8")
            self.output.insert(tk.END, f"Servidor: {resposta}\n")
        except:
            messagebox.showerror("Erro", "Erro ao enviar ou receber dados do servidor.")

root = tk.Tk()
app = ClienteGUI(root)
root.mainloop()
