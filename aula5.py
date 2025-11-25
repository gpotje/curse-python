#copy --> shallow copy
#get --> get keys 
#pop --> delete a specific item
#popitem --> delete the last item
#update --> update a dict with another
#import copy --> d2 = copy.deepcopy(d1)

d1 = {
    'c1': 1,
    'c2': 2,
   
}

#d2 = d1

d2 = d1.copy()

d2['c1'] = 1000
print(d1)
print(d2)


