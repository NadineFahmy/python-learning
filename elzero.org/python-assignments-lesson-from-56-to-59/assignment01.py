def calculate(num1, num2, operation="add"):
    operation = operation.lower()

    if operation == "add" or operation == "a":
        return num1 + num2

    elif operation == "subtract" or operation == "s":
        return num1 - num2

    elif operation == "multiply" or operation == "m":
        return num1 * num2

    else:
        print("This operation does not exist.")


# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200
