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
from ex_194_funcao import *

lista_tarefas  = []
lista_tarefas_clone  = []

tafera_comando = ''

while True:
   desenha_menu()
   tafera_comando = input()

   if tafera_comando == 'listar':
        listar(lista_tarefas)

   elif tafera_comando == 'clean':
       os.system("cls")

   elif tafera_comando == 'desfazer':
       desfazer(lista_tarefas,lista_tarefas_clone)
       listar(lista_tarefas)

   elif tafera_comando == 'refazer':
       refazer(lista_tarefas,lista_tarefas_clone)
       listar(lista_tarefas)

   else:
     lista_tarefas.append(tafera_comando)



