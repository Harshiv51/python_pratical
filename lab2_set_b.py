

numbers_set = {22, 12, 10, 2, 24}

print(f"numbers set: {numbers_set}")

num = int(input("Enter number to remove: "))

try:
    numbers_set.remove(num)
except Exception as e:
    pass

print(f"numbers set: {numbers_set}")