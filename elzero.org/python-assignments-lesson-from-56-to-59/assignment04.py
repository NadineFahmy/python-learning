def welcome(name="Guest", age="Unknown", country="Unknown"):
    print(f"Hello {name}")
    print(f"Your Age Is {age}")
    print(f"You Live In {country}")


# Examples:

welcome("Nadine", 24, "Egypt")

print("-" * 30)

# No data passed
welcome()
