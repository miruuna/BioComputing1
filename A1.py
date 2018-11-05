with open('add.txt', 'r') as f:
    numbers1 = f.read().splitlines()
print(numbers1)
the_sum1 = 0

for number in numbers1:
    the_sum1 += int(number)

print(the_sum1)
        


with open('sub.txt', 'r') as f2:
    numbers2 = f2.read()
number_list = []
for line in numbers2:
    a_number = float(line)
    number_list.append(a_number)

print(number_list)
    
