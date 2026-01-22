my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

points_map = {
    "A": 100,
    "B": 80,
    "C": 40
}

total = 0

for subject, rank in my_ranks.items():

    points = points_map[rank]
    total += points

    print(f"My Rank in {subject} Is {rank} And This Equal {points} Points")

print(f"Total Points Is {total}")

# Needed Output
"My Rank in Math Is A And This Equal 100 Points"
"My Rank in Science Is B And This Equal 80 Points"
"My Rank in Drawing Is A And This Equal 100 Points"
"My Rank in Sports Is C And This Equal 40 Points"
"Total Points Is 320"