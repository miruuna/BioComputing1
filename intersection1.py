with open('filenames.txt', 'r') as f1:
    file_names = f1.read().splitlines()

d={}
nfiles = 0
for file in file_names:
    nfiles += 1
    with open(file) as f:
        words = f.read().splitlines()
        for w in words:
            if w in d:
                d[w]+=1
            else:
                d[w]=1

for k in d:
    if d[k] == nfiles:
        print(k)
        
