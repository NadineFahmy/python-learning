email = input("Enter your email: ").strip().lower()

name = email.split("@")[0].capitalize()
site = email.split("@")[1].split(".")[0]
tld = email.split(".")[-1]

print(f"Your Name is {name}")
print(f"Email Service Provider is {site}")
print(f"Top Level Domain is {tld}")

# Inputs

"Osama@Nn.Sa" # Email

# Needed Output

"Your Name Is Osama"
"Email Service Provider Is nn"
"Top Level Domain Is sa"