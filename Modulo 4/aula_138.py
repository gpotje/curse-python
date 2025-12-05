#list comprehension 

l1 = []
for numero in range(10):
    l1.append(numero)

print(l1)

l2 = [
    n  * 2
    for n in range(10)
]
print(l2)