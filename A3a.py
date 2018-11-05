import re
import os

for filename in os.listdir('C:/Users/Miruna/Documents/Masters/biocomputing/practicals/practical8'):
    if filename.endswith('.h'):
        with open(filename, 'r') as pdb:
            pdb_file = pdb.read().splitlines()
            
        p = re.compile(r' ORGANISM\_SCIENTIFIC\:\s(.+)\;')
        t = re.compile(r' \bSTRAIN\:\s(.+)\;')
        species_list =[]
        strain_list =[]
        for i in pdb_file:
            #print(i)
            species = p.finditer(i)
            strain = t.finditer(i)
            
            for match in species:
                species_name = match.group(1)
                if species_name not in species_list:
                    species_list.append(species_name)
                
            for match in strain:
                strain_name = match.group(1)
                if strain_name not in strain_list:
                    strain_list.append(strain_name)
        print('Strains found in ' , filename, ': ', ', '.join(str(e) for e in strain_list))
        print('Species found in ' ,filename, ': ', ', '.join(str(e) for e in species_list))


