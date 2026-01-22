numbers = [15, 81, 5, 17, 20, 21, 13]

count = 1

for num in sorted(numbers, reverse=True):

    if num % 5 == 0:
        print(f"{count} => {num}")
        count += 1

print("Loop finished successfully.")

# Needed Output
"1 => 20"
"2 => 15"
"3 => 5"
"All Numbers Printed"
