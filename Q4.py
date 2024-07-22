import random

# a:
numbers_list = [num for num in range(95, 106)]
print(numbers_list)
# b:
even_numbers_list = [num for num in range(10, 21) if num % 2 == 0]
print(f"{even_numbers_list}")
# c:
random_bool_list = [random.choice([False, True]) for _ in range(5)]
print(f"{random_bool_list}")
# d:
# It's shorter, and make reader see the variable is not so much important.
# e:
numbers_list = [random.randint(1, 100) for _ in range(10)]
print(f"{numbers_list}")
# f:
above_50 = [num for num in numbers_list if num > 50]
print(f"{above_50}")




