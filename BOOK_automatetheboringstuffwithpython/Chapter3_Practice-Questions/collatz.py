def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    print(result)
    return result


# Get valid integer input from the user
while True:
    try:
        num = int(input("Enter number:\n"))
        if num <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")


# Run the Collatz sequence
while num != 1:
    num = collatz(num)
