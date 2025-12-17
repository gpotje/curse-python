import json


def gravaJson(lista,Nomelista):
    dados_python = dictJson()
    dados_python[Nomelista] = lista
    with open('dados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_python, arquivo, ensure_ascii=False, indent=4)

def dictJson():
    with open('dados.json', 'r', encoding='utf-8') as arquivo:
        dados_python = json.load(arquivo)
        return dados_python

def listaJson(Nomelista):
    with open('dados.json', 'r', encoding='utf-8') as arquivo:
        dados_python = json.load(arquivo)
        lista_tarefas = dados_python[Nomelista]
        return lista_tarefas