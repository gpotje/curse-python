# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears

# todo = [] -> lista de tarefas

# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']

def desenha_menu():
   print("=================================")
   print('Digite uma tarefa ou comando:')
   print('listar, desfazer, refazer, clean')
   print("=================================")
   print()

def listar(lista):
    print()
    print("TAREFAS:")
    if not lista:
        print()
        print("=== A lista está vazia! Inseria um item ===")
    else:
        for tarefa in lista:
            print(tarefa)
    print()

def desfazer(lista_tarefas,lista_tarefas_clone):
    if not lista_tarefas:
        print("A lista está vazia!")
    else:
        lista_tarefas_clone.append(lista_tarefas[-1])
        del lista_tarefas[-1]

def refazer(lista_tarefas,lista_tarefas_clone):
    if not lista_tarefas_clone:
        print("A lista está vazia!")
    else:
        lista_tarefas.append(lista_tarefas_clone[-1])
        del lista_tarefas_clone[-1]





