from json.encoder import INFINITY

numbers_set = {22, 10, 12, 46, 678, 87, 24, 5146}
mini = INFINITY
max = -INFINITY

for i in numbers_set:
    if(i > max):
        max = i

    if(i < mini):
        mini = i


print(f'Numbers set: {numbers_set}')
print(f'Maximum number: {max}')
print(f'Minimum number: {mini}')