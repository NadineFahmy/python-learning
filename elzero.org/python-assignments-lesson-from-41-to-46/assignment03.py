age = int(input("Enter your age: ").strip())

if age <= 10 or age >= 100:
    print("Age is out of range.")
else:
    months = age * 12
    weeks = age * 52
    days = age * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    print(f"Your age in months is: {months}")
    print(f"Your age in weeks is: {weeks}")
    print(f"Your age in days is: {days}")
    print(f"Your age in hours is: {hours}")
    print(f"Your age in minutes is: {minutes}")
    print(f"Your age in seconds is: {seconds}")

# Input Example 38

# Needed Output
"Your Age In Months Is 456 Months" # Months Example
"Your Age In Weeks Is 1824 Weeks" # Weeks Example
