import json
import os
from typing import TypedDict

NOME_ARQUIVO = 'aula177.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.dirname(__file__)
CAMINHO_FINAL = CAMINHO_ABSOLUTO_ARQUIVO+'\\'+NOME_ARQUIVO
print(CAMINHO_FINAL)

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float

filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_FINAL, 'w') as arquivo:
    json.dump(filme,arquivo,ensure_ascii=False,indent=2)

with open(CAMINHO_FINAL, 'r') as arquivo:
    filme_do_json:Movie = json.load(arquivo)
    print(filme_do_json)