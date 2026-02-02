def show_skills(name, *skills):
    print(f"Hello {name}")

    if skills:
        print("Your Skills Are:")
        for skill in skills:
            print(f"- {skill}")
    else:
        print("You Have No Skills Yet")


# Input
show_skills("Osama", "HTML", "CSS", "JS", "Python")

# Output
"Hello Osama Your Skills Is"
"- HTML"
"- CSS"
"- JS"
"- Python"

# Input
show_skills("Ahmed")

# Output
"Hello Ahmed You Have No Skills To Show"