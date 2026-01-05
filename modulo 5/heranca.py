#Associação - usa
#Agregação - tem
#Composição - é dono de

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(" PESSOA NOME CLASSE:"+self.__class__.__name__)
    
class Cliente(Pessoa):
   def falar(self):
     print(" CLIENTE NOME CLASSE:"+self.__class__.__name__)


c1 = Cliente('João',45)
c1.falar()

# Method resolution order:
# --> Cliente
# --> Pessoa
# --> builtins.object

