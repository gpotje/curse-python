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
from ex_194_funcoes import listar, refazer, desfazer, desenha_menu, gravaJsonFuncao


lista_tarefas = []
lista_tarefas_clone  = []


while True:

   desenha_menu()
   tafera_comando = input()

   if tafera_comando == 'listar':
        listar('comandos')

   elif tafera_comando == 'clean':
       os.system("cls")

   elif tafera_comando == 'desfazer':
       desfazer()
       listar('comandos')

   elif tafera_comando == 'refazer':
       refazer()
       listar('comandos')

   elif tafera_comando == 'LRD':
       listar('refazerOuDesfazer')

   else:
     gravaJsonFuncao(tafera_comando)
     



