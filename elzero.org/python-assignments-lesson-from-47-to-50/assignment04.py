my_friends = []
max_friends = 4

while len(my_friends) < max_friends:

    name = input("Enter your friend's name: ").strip()

    if name.isupper():
        print("Name is not valid.")
        continue

    if name.islower():
        fixed_name = name.capitalize()
        my_friends.append(fixed_name)
        remaining = max_friends - len(my_friends)

        print(f"{fixed_name} added after capitalizing the first letter.")
        print(f"{remaining} spots left.")

    elif name[0].isupper():
        my_friends.append(name)
        remaining = max_friends - len(my_friends)

        print(f"{name} added successfully.")
        print(f"{remaining} spots left.")

    else:
        print("Invalid name format.")

print("Friends list is full:", my_friends)

# Input
# name = "OSAMA"

# Needed Output
"Invalid Name"

# Input
# name = "osama"

# Needed Output
"Friend osama Added => 1st Letter Become Capital"
"Names Left in List Is 3"

# Input
# name = "Ahmed"

# Needed Output
"Friend Ahmed Added"
"Names Left in List Is 2"