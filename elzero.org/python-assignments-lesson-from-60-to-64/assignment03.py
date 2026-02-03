scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70
}


def get_the_scores(*args, **scores):

    if args:
        name = args[0]
        if scores:
            print(f"Hello {name} This Is Your Score Table:")
        else:
            print(f"Hello {name} You Have No Scores To Show")

    for subject, value in scores.items():
        print(f"{subject} => {value}")

# Test 1
get_the_scores("Osama", **scores_list)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"

print("-"*30)

# Test 2
get_the_scores("Osama")

# Output
"Hello Osama You Have No Scores To Show"

print("-"*30)


# Test 3
get_the_scores(**scores_list)

# Output
"Math => 90"
"Science => 80"
"Language => 70"