with open('dna_seq.txt', 'r') as f:
    sequence = f.read()
count = 0

#create a dictionary that stores the DNA bases and their respective percentage
d={}
for base in sequence:
    count = sequence.count(base)
    percentage = count/len(sequence)*100
    d[base] = percentage
print(d)
