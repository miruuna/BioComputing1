with open('PDB_chain_ids.txt', 'r') as f:
    codes = f.read().splitlines()

d_codes = {}
for code in codes:
    the_code = code[:4]
    aa = code[-1]
    if the_code in d_codes:
        d_codes[the_code].append(aa)
    else:
        d_codes[the_code] = [aa]
print(d_codes)

for k, v in sorted(d_codes.items()):
    s = '{}:'.format(k)
    v.sort()
    for letter in v:
        s +=' '+ letter
    print(s)
    
