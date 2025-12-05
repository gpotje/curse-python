# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

#& C:/Users/gpotj/AppData/Local/Python/pythoncore-3.14-64/python.exe "c:/Users/gpotj/Desktop/python/modulo 6/281_ex_data"


from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


data_inicial = date(2020, 12, 20)
lista_data = [data_inicial]
# Adiciona 5 anos (aproximadamente 365 dias * 5)
# Nota: Isso não lida perfeitamente com anos bissextos, mas é simples.

emprestimo_maria = float(1000000)

data_futura = data_inicial + timedelta(days=365 * 5)

print(f"Data inicial: {data_inicial.strftime('%d/%m/%Y')}")
print(f"Data futura (aprox.): {data_futura.strftime('%d/%m/%Y')}")

div = emprestimo_maria / 60 

for i in range(1, 61):
   lista_data.append(lista_data[i-1] + relativedelta(months=1)) 
    

for i,data in enumerate(lista_data):
    print(f'n° {i} Datas do emprestimo: {data.strftime('%d/%m/%Y')} valor da parcela: {div:.2f}')
    if i % 12 == 0:
        print('===============================')

