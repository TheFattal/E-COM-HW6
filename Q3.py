import random

# a:
random_list = [random.choice([True, False]) for _ in range(3)]
print(f"{random_list}")
# b:
print("There only trues in the list!" if all(random_list) else "NO, There are some False elements in the list too...")
# c:
print("The list contains at least one True." if any(random_list) else "The list does not contain any True.")
# d:
print("There only FALSE elements!" if all(not elem for elem in random_list) else "NO, There are some TRUE elements in the list too.")
# e:
print("The list contains at least 1 False." if any(not elem for elem in random_list) else "The list doesn't contain any FALSE.")
# f:
random_numbers = [random.randint(-2, 2) for _ in range(5)]
print(f"{random_numbers}")
# g:
print("All numbers in the list are different from 0!" if all(elem != 0 for elem in random_numbers) else "There are some 0")
# h and i:
print("All elements are 0!" if all(elem == 0 for elem in random_numbers) else "Not all elements are 0!")
# j:
print("At least one element is 0" if any(elem == 0 for elem in random_numbers) else "there no zeroes at all!")