# read in sequence (split across multiple lines)
with open('long_seq.txt', 'r') as f:
 file = f.read().splitlines()
# create sequence as single string
my_seq = ''
for aa in file:
 my_seq += aa
# Create sliding window onto the sequence,
# starting with longest possible. At each
# iteration, compare window to its reverse. If
# match (i.e. palindrome) found, print it out.
full_len = len(my_seq)
current_len = full_len
# Used to indicate when a palindrome is found
found = False
# Loop through windows of the current size
while current_len > 1:
    i = 0
    while i + current_len <= full_len:
        sub_seq = my_seq[i:i + current_len]
        sub_reversed = sub_seq[::-1]
        if sub_reversed == sub_seq:
            print(sub_seq)
            print(len(sub_seq))
            found = True
        i += 1
    if found:
        break
    current_len -= 1
