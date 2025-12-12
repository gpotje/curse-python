# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME,'Desktop','python','teste_arquivos')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

#print(DESKTOP)
#os.system("dir")

#criar pasta 
os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(DESKTOP):
    if root == NOVA_PASTA:
        continue
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        shutil.copy(caminho_arquivo,NOVA_PASTA)
        