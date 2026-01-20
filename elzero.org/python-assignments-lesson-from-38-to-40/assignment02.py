age = int(input("Enter your age: "))

if age <= 16:
    print("This site contains articles not suitable for people under 16.")
else:
    print(f"Welcome! Your age is {age} and this site is suitable for you.")


# Inputs

16 # Input One
24 # Input Two

# Needed Output

"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" # If Age < 16
"Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You" # If Age Is 16+