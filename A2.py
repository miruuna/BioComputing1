with open('clever_birds.txt', 'r') as f1:
    file1 = f1.read().splitlines()
    
clever_birds=[]
for elem in file1:
    clever_birds.append(elem.lower())


corvids =[]
with open('corvids.txt', 'r') as f2:
    file2 = f2.read().splitlines()
for i in file2:
    corvids.append(i.lower())

garden_birds =[]
with open('garden_birds.txt', 'r') as f3:
    file3 = f3.read().splitlines()
for i in file3:
    garden_birds.append(i.lower())

for bird in garden_birds:
    if bird in corvids and bird in clever_birds:
        print(bird)

    
    
