# Exercício - Lista de tarefas com refazerOuDesfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears

# todo = [] -> lista de tarefas

# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# refazerOuDesfazer = ['fazer café',] -> Refazer ['caminhar']
# refazerOuDesfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']

from ex_194_opJson import listaJson,gravaJson

lista_tarefas = []

def desenha_menu():
   print("=================================")
   print('Digite uma tarefa ou comando:')
   print('listar, Desfazer, refazer, LRD ,clean')
   print("=================================")
   print()


def gravaJsonFuncao(tafera_comando):
    lista_tarefas.append(tafera_comando)
    gravaJson(lista_tarefas,'comandos')
    
def listar(Nomelista):
    lista_local = listaJson(Nomelista)
    print()
    print(f"TAREFAS: {Nomelista}")
    if not lista_local:
        print()
        print("=== A lista está vazia! Inseria um item ===")
    else:
        for tarefa in lista_local:
            print(tarefa)
    print()

def desfazer():
    lista_comandos = listaJson('comandos')
    lista_defeitos = listaJson('refazerOuDesfazer')
    if not lista_comandos:
        print("A lista de comandos está vazia!")
    else:
        lista_defeitos.append(lista_comandos[-1])
        del lista_comandos[-1]
        gravaJson(lista_comandos,'comandos')
        gravaJson(lista_defeitos,'refazerOuDesfazer')
    

def refazer():
    lista_comandos = listaJson('comandos')
    lista_desfeitos = listaJson('refazerOuDesfazer')
    if not lista_desfeitos:
        print("A lista está vazia!")
    else:
        lista_comandos.append(lista_desfeitos[-1])
        del lista_desfeitos[-1]
        gravaJson(lista_comandos,'comandos')
        gravaJson(lista_desfeitos,'refazerOuDesfazer')





