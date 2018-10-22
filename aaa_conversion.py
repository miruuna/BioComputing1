#Create a dictionary that maps 3-letter to 1 letter amino acid codes using the
#the file aa_types.txt. Use the dictionary to convert the sequence in the file
#sequence3code.txt to a simple sequence
with open('aa_types.txt', 'r') as f:
    aa_conv  = f.read().splitlines()
d_aa = {}    
for aa in aa_conv:
    (aa3, aa1) = aa.split(' ')
    d_aa[aa3]=aa1
print(d_aa)

sequence_singleletter =' '
with open('sequence3code.txt', 'r') as f2:
    sequence_3letter = f2.read()
    sequence_list = sequence_3letter.split(' ')
print(sequence_singleletter)
for a_code in sequence_list:
    sequence_singleletter += d_aa[a_code]
print(sequence_singleletter)
    
