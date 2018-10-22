with open('dna_seq.txt', 'r') as f:
    sequence = f.read()

sequence.replace('A', 'T')
sequence.replace('G', 'C')
sequence.replace('T', 'A')
sequence.replace('C', 'G')

print(sequence)
