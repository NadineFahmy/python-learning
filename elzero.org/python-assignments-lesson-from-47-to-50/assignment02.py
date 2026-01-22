friends = ["Mohamed", "shady", "Ahmed", "eman", "Sherif"]

i = 0
ignored = 0

while i < len(friends):

    if friends[i][0].islower():
        ignored += 1
        i += 1
        continue

    print(friends[i])
    i += 1

print(f"Ignored names count: {ignored}")
