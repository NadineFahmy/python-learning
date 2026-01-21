arab_countries = ["Egypt", "Saudi", "UAE", "Qatar", "Kuwait"]
discount = 20   
price = 1000    

country = input("Enter your country: ").strip().capitalize()

if country in arab_countries:
    final_price = price - (price * discount / 100)
    print(f"You have a {discount}% discount.")
    print(f"Final price is: {final_price}")
else:
    print("Sorry, no discounts for your country.")
    print(f"Final price is: {price}")
