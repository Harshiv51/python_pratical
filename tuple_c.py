number_tuple = (45, 34, 67,212, 2002, 2210)
print(f"Number tuple before adding: {number_tuple}")

number_list = list(number_tuple) # making list from tuple
number_list.append(51) # adding element

number_tuple = tuple(number_list) # making tuple from list

print(f"Number tuple after adding: {number_tuple}")