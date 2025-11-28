#Instalando o pytz
#pip install pytz types-pytz
#https://docs.python.org/3/library/datetime.html
from datetime import datetime

#datetime(ano,mes,dia) 2025-11-20 00:00:00
d0 = datetime(2025,11,20)
print(d0)


#datetime(ano,mes,dia,horas) 2025-11-20 07:00:00
d0 = datetime(2025,11,20,7)
print(d0)

#datetime(ano,mes,dia,horas,min) 2025-11-20 07:49:00
d0 = datetime(2025,11,20,7,49)
print(d0)


data_srt_data = '2025-11-20 00:00:00'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

d1 = datetime.strptime(data_srt_data,data_str_fmt)
print(d1)
