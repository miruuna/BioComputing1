with open('filenames.txt', 'r') as f1:
    file_names = f1.read().splitlines()
for file in file_names:
    file_open = open(file) as f:
        words = f.read().splitlines()
        
