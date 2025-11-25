#dicionarios

person = {
    'name': 'Gabriel',
    'age': 29,
    'lastName':'Potje',
    'address':[
        {
            'street':'sueo',
            'number':200
         }
    ]
}
print(person, type(person))
print("--------"+person['lastName'])

for keys in person:
    print(keys, person[keys])

if person.get('middleName') is None:
    print('Não existe')


if person.get('lastName') is None:
    print('Não existe')
else:
    print("------"+person['lastName'])

