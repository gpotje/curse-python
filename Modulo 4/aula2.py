
#Closure e funções que retornam outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

say_good_morning = criar_saudacao('good morning')
say_good_night = criar_saudacao('good night')

for day_name in ['Maria','Joana','Gabriel']:
    print(say_good_morning(day_name))


for night_name in ['Maria','Joana','Gabriel']:
    print(say_good_night(night_name))