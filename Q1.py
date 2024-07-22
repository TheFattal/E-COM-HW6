# a:
my_list = []
for i in range(80, 100):
    my_list.append(i)
# b:
print(f"{my_list[0]}")
# c:
print(f"{my_list[-1]}")
# d:
print(f"{len(my_list)}")
# e:
print(f"{my_list[3:13]}")
# f:
print(f"{my_list[3:]}")
# g:
print(f"{my_list[0:10]}")
# h:
# Determine the middle index:
middle_index = len(my_list) // 2
# Insert 999 value into the middle of the list:
my_list.insert(middle_index, 999)
# i:
print(f"{my_list[::-1]}")
# j:
print(f"{my_list[1::2]}")
