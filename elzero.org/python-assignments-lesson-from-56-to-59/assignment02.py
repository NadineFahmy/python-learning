def addition(*numbers):
    total = 0

    for num in numbers:
        if num == 10:
            continue   # Skip 10 completely

        elif num == 5:
            total -= num  # Subtract 5

        else:
            total += num  # Add normally

    return total

# Tests
print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160

