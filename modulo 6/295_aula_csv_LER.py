# CSV (Comma Separated Values - Valores separados por vírgulas)
# É um formato de arquivo que armazena dados em forma de tabela, onde cada
# linha representa uma linha da tabela e as colunas são separadas por vírgulas.
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'tabela.csv'

print(CAMINHO_CSV)

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)

print('=================================')

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)