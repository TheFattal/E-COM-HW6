import statistics

# a:
temperatures = []
# b:
while True:
    temp = float(input("Enter a temperature (enter -999 to stop): "))

    if temp == -999:
        break

    if temp < -50 or temp > 50:
        print("Temperature must be between -50 and 50. Please enter again.")
        continue

    temperatures.append(temp)
# c:
additional_temperatures = [18.5, 39.1, -20.0]
temperatures.extend(additional_temperatures)
# d:
print(f"The highest temperature is:{max(temperatures)}")
# e:
print(f"The highest temperature is:{min(temperatures)}")
# f:
temp_len: int = len(temperatures)
temp_sum: float = sum(temperatures)
temp_avg: float = temp_sum / temp_len
print(f"The list average is: {temp_avg:.2f}")
# g:
print(f"Mean temperature: {statistics.mean(temperatures):.2f}")
# h:
del temperatures[0]
# i:
temperatures.remove(18.5)
# j:
last_temp = temperatures.pop()
# k:
temperatures_copy = temperatures.copy()
# Sort the copied list
temperatures_copy.sort()
# l:
temperatures_copy = temperatures.copy()
temperatures_copy.sort(reverse=True)
# M:
# ANSWER: sort() is a list method that sorts the list in place and modifies it directly.
# sorted() is a built-in function that returns a new sorted list without modifying the original.

# N:
# It returns an iterator object (reversed) specific to the type of input (list, tuple, string, etc.).
my_list = [1, 2, 3, 4, 5]

# Get a reversed iterator
reversed_list_iterator = reversed(my_list)

# Convert reversed iterator to a list
reversed_list = list(reversed_list_iterator)

print(reversed_list)  # Output: [5, 4, 3, 2, 1]


