import tkinter as tk
from tkinter import ttk
import os
import json

ARQUIVO = "tarefas.json"

def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

tarefas = carregar()

def adicionar():
    tarefas = carregar()  # recarrega sempre
    
    titulo = titulo_entry.get()
    
    if titulo.strip() == "":
        return
    
    tarefa = {
        "titulo": titulo,
        "concluida": False
    }
    
    tarefas.append(tarefa)
    salvar(tarefas)
    
    titulo_entry.delete(0, tk.END)
    listar()
    
def listar():
    lista_tarefas.delete(0, tk.END)
    
    tarefas = carregar() 
    
    if not tarefas:
        lista_tarefas.insert(tk.END, "Nenhuma tarefa.")
        return

    for i, t in enumerate(tarefas):
        status = "✔" if t["concluida"] else "✘"
        lista_tarefas.insert(tk.END, f"{i} - [{status}] {t['titulo']}")

def concluir():
    tarefas = carregar()

    selecionado = lista_tarefas.curselection()

    if not selecionado:
        print("Selecione uma tarefa.")
        return

    i = selecionado[0]

    tarefas[i]["concluida"] = True
    salvar(tarefas)

    listar()
    
def remover():
    tarefas = carregar()
    
    selecionado = lista_tarefas.curselection()
    
    if not selecionado:
        print("Selecione uma tarefa.")
        return
    
    i = selecionado[0]
    tarefas.pop(i)
    
    salvar(tarefas)
    listar()
    
def sair():
    root.destroy()
    
#---------------interface-------------------------

root = tk.Tk()
root.geometry("400x400")
root.title("ToDo")

icone = tk.PhotoImage(file="icone.png")
root.iconphoto(True, icone)

titulo_entry = ttk.Entry(root)

lista_tarefas = tk.Listbox(root)
lista_tarefas.grid(row=1, column=1, rowspan=4, sticky="nsew")

butad = ttk.Button(root, text="Adicionar tarefa", command=adicionar)
butli = ttk.Button(root, text="Listar tarefas", command=listar)
butco = ttk.Button(root, text="Concluir tarefa", command=concluir)
butre = ttk.Button(root, text="Remover tarefa", command=remover)
butsa = ttk.Button(root, text="Sair", command=sair)

butad.grid(row=0, column=0, sticky="nsew")
titulo_entry.grid(row=0, column=1, sticky="nsew")

butli.grid(row=1, column=0, sticky="nsew")
butco.grid(row=2, column=0, sticky="nsew")
butre.grid(row=3, column=0, sticky="nsew")
butsa.grid(row=4, column=0, sticky="nsew")


root.mainloop()