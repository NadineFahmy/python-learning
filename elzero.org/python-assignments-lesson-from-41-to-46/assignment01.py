num1 = int(input("Enter first number: ").strip())
num2 = int(input("Enter second number: ").strip())
operation = input("Enter operation (+, -, *, /, %): ").strip()

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "%":
    print(num1 % num2)
else:
    print("Invalid operation")

# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800