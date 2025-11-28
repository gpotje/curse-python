#len --> how much keys have
#keys --> iteravel com as keys
#values --> iteravel com as valores
#setdefault --> if there isn't keys, add value default

person = {
    'name': 'Gabriel',
    'age': 29,
    'lastName':'Potje',
 
}

print(len(person))
print(list(person.keys()))
print(list(person.values()))

person.setdefault('address',0)

for keys, values in person.items():
    print(keys,values)

