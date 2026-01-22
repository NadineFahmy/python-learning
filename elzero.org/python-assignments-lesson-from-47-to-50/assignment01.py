num = int(input("Enter a number: ").strip())

if num <= 0:
    print("Number must be greater than 0.")
else:
    count = 0
    i = num - 1

    while i >= 1:

        if "6" in str(i):
            i -= 1
            continue

        print(i)
        count += 1
        i -= 1

    print(f"All numbers printed successfully. Total printed numbers: {count}")


# Input
#num = 0

# Needed Output
"Number 0 Is Not Larger Than 0"

# Input
# num = 10

# Needed Output
9
8
7
5
4
3
2
1
"8 Numbers Printed Successfully."
