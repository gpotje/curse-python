class Carro:
    def __init__(self,potencia,nome):
        self.potencia = potencia
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando')