# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears

# todo = [] -> lista de tarefas

# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
import os


lista_tarefas  = ['tomar banho']
lista_tarefas_clone  = []

tafera_comando = ''


while True:
   
   print("=================================")
   print('Digite uma tarefa ou comando:')
   print('listar, desfazer, refazer, clean')
   print("=================================")
   print()
   
   tafera_comando = input()


   if tafera_comando == 'listar':
        print()
        print("TAREFAS:")
        for tarefa in lista_tarefas:
            print(tarefa)
        print()
   elif tafera_comando == 'clean':
       os.system("cls")
   elif tafera_comando == 'desfazer':
       lista_tarefas_clone.append(lista_tarefas[-1])
       del lista_tarefas[-1]
   elif tafera_comando == 'refazer':
       lista_tarefas.append(lista_tarefas_clone[-1])
       del lista_tarefas_clone[-1]
   else:
     lista_tarefas.append(tafera_comando)



