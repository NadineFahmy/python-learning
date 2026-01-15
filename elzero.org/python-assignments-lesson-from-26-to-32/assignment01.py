my_list = [1, 2, 3, 3, 4, 5, 1]

unique_list = list(set(my_list))

unique_list.sort()

print(unique_list)

print(type(unique_list))

print(unique_list[:-1])

# Needed Output

# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4
