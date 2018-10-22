
with open('species1.txt', 'r') as f1:
    species1 = f1.read().splitlines()

with open('species2.txt', 'r') as f2:
    species2 = f2.read().splitlines()

d1={}
for sp in species1:
    d1[sp]= True
d2={}
for sp in species1:
    d2[sp]= True
count = 0

for k in d2:
    if not k in d1:
        print(k)
        count +=1
print(count)
