import tkinter as tk
from tkinter import font

# Criando a janela principal
janela = tk.Tk()
janela.title("Visualização de Fontes")
janela.geometry("600x700")

# Criando um título
titulo = tk.Label(janela, text="Exemplo de Fontes no Tkinter", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

# Obtendo todas as fontes disponíveis
fontes_disponiveis = sorted(font.families())

# Criando labels para cada fonte
frame = tk.Frame(janela)
frame.pack(fill="both", expand=True)

canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

for f in fontes_disponiveis:
    label = tk.Label(scrollable_frame, text=f"A fonte usada aqui é {f}", font=(f, 14))
    label.pack(pady=2)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Executando a janela
janela.mainloop()