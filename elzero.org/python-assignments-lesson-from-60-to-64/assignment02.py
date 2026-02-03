def get_people_scores(*args, **scores):
    if args:
        name = args[0]
        if scores:
            print(f"Hello {name} This Is Your Score Table:")
        else:
            print(f"Hello {name} You Have No Scores To Show")

    for subject, value in scores.items():
        print(f"{subject} => {value}")

# Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"

print("-"*30)

# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)

# Output
"Hello Mahmoud This Is Your Score Table:"
"Logic => 70"
"Problems => 60"

print("-"*30)

# Test 3
get_people_scores(Logic=70, Problems=60)

# Output
"Logic => 70"
"Problems => 60"

print("-"*30)

# Test 4
get_people_scores("Ahmed")

# Output
"Hello Ahmed You Have No Scores To Show"