# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears

# todo = [] -> lista de tarefas

# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']

import json

lista_tarefas = []
lista_tarefas_clone  = []

def desenha_menu():
   print("=================================")
   print('Digite uma tarefa ou comando:')
   print('listar, desfazer, refazer, clean')
   print("=================================")
   print()

def gravaJson(lista,local):
    dados_python = dictJson()
    dados_python[local] = lista
    with open('dados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_python, arquivo, ensure_ascii=False, indent=4)

def dictJson():
    with open('dados.json', 'r', encoding='utf-8') as arquivo:
        dados_python = json.load(arquivo)
        return dados_python

def listaJson():
    with open('dados.json', 'r', encoding='utf-8') as arquivo:
        dados_python = json.load(arquivo)
        lista_tarefas = dados_python['comandos']
        return lista_tarefas


def listar():
    lista_local = listaJson()
    print()
    print("TAREFAS:")
    if not lista_local:
        print()
        print("=== A lista está vazia! Inseria um item ===")
    else:
        for tarefa in lista_local:
            print(tarefa)
    print()

def desfazer():
    lista_tarefas = listaJson()
    if not lista_tarefas:
        print("A lista está vazia!")
    else:
        lista_tarefas_clone.append(lista_tarefas[-1])
        del lista_tarefas[-1]
        gravaJson(lista_tarefas,'comandos')




def refazer():
    lista_tarefas = listaJson()
    if not lista_tarefas_clone:
        print("A lista está vazia!")
    else:
        lista_tarefas.append(lista_tarefas_clone[-1])
        del lista_tarefas_clone[-1]
        gravaJson(lista_tarefas,'refazer')





