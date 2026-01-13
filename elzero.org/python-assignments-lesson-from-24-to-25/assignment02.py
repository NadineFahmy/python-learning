friends = ("Osama", "Ahmed", "Sayed")

friends = list(friends)

friends[0] = "Elzero"

friends = tuple(friends)

print(friends)
print(type(friends))
print(str(len(friends)) + " Elements")

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements