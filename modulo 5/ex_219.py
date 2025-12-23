# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self,nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self,nome):
        self.nome = nome
   

class Fabricante:
    def __init__(self,nome):
        self.nome = nome
   
c1 = Carro('Fusca')
f1 = Fabricante('Volkswagen')
m1 = Motor('1.0')

c1.fabricante = f1 
c1.motor = m1

print(f'carro: {c1.nome}, motor: {c1.motor.nome}, Fabricante: {c1.fabricante.nome}')        

