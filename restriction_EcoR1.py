the_sequence = ' '
with open('dna_seq1.txt', 'r') as f:
    sequence = f.read().splitlines()
    for base in sequence:
        the_sequence += base
#print(the_sequence)

#cut out first exon runnning from the start to position 63

coding_region1 = the_sequence[63::]
coding_region2 = the_sequence [::91]
print(coding_region1)
print(coding_region2)

#cut out second exon runnning from position 91 to the end
