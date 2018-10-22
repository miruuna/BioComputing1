with open('species1.txt', 'r') as f1:
    species1 = f1.read().splitlines()
print(len(species1))

with open('species2.txt', 'r') as f2:
    species2 = f2.read().splitlines()
print(len(species2))

list1=[]
found = False
for species in species1:
    if species in species2:
        found = True
    else:
        found = False
    if found == False:
        list1.append(species)
#print(list1)
print(len(list1))

list2=[]
for species in species2:
    if species in species1:
        found = True
    else:
        found = False
    if found == False:
        list2.append(species)
#print(list2)
print(len(list2))
