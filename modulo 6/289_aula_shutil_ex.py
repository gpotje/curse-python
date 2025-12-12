# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME,'Desktop','python','teste_arquivos')
PASTA =   os.path.join(DESKTOP,'EXEMPLO')

caminho_arquivo = DESKTOP+'\meu_arquivo2.txt'


print(caminho_arquivo)

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write("Olá, este é o conteúdo do meu arquivo TXT!\n")
    arquivo.write("Python facilita muito a manipulação de arquivos.")

# for root, dirs, files in os.walk(DESKTOP):
#      if root == PASTA:
#         continue
#      for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         shutil.copy(caminho_arquivo,PASTA)



shutil.copy(caminho_arquivo,PASTA)
print('teste')
shutil.rmtree(caminho_arquivo,PASTA)
#shutil.copytree(caminho_arquivo,PASTA)
#shutil.move(caminho_arquivo,PASTA)
#shutil.move(caminho_arquivo,PASTA)