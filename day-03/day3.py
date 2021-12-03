import os
import sys

with open("input.txt") as file:
    data = [str(x).rstrip('\n') for x in file]
file.close()

# PART 1
bit_count = []
gamma_rate = ""
epsilon_rate = ""

def count_bits(inputs):
    bit_count = []
    for i in range(len(inputs[0])):
        bit_count.append(0)

    for bin in inputs:
        for i in range(len(bin)):
            if(bin[i] == '1'): 
                bit_count[i] = bit_count[i]+1
    return bit_count

bit_count = count_bits(data)

for total in bit_count:
    if(total < len(data)/2): 
        gamma_rate = gamma_rate + '0'
        epsilon_rate = epsilon_rate + '1'
    else:
        gamma_rate = gamma_rate + '1'
        epsilon_rate = epsilon_rate + '0'

gamma_rate = int(gamma_rate,2)
epsilon_rate = int(epsilon_rate,2)

# print(gamma_rate*epsilon_rate)
# print(bit_count)

# PART 2

index = 0
oxygen_data = data
while(len(oxygen_data)>1):
    bit_count = count_bits(oxygen_data)
    if (bit_count[index] >= len(oxygen_data)/2):
        oxygen_data = list(filter(lambda line: (line[index] == '1'), oxygen_data))
    else:
        oxygen_data = list(filter(lambda line: (line[index] == '0'), oxygen_data))
    index = index+1
print(oxygen_data)


index = 0
carbon_data = data
while(len(carbon_data)>1):
    bit_count = count_bits(carbon_data)
    if (bit_count[index] >= len(carbon_data)/2):
        carbon_data = list(filter(lambda line: (line[index] == '0'), carbon_data))
    else:
        carbon_data = list(filter(lambda line: (line[index] == '1'), carbon_data))
    index = index+1
print(carbon_data)

oxygen_rating = int(oxygen_data[0],2)
carbon_rating = int(carbon_data[0],2)

print(oxygen_rating*carbon_rating)
# for bit in rating
