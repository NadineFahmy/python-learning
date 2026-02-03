def get_score(**skills):
	for skill_key, skill_value in skills.items():
		print(f"\"{skill_key} => {skill_value}\"")


# Tests
get_score(Math=90, Science=80, Language=70)

# Output
"Math => 90"
"Science => 80"
"Language => 70"

print("-"*30)

# Tests
get_score(Logic=70, Problems=60)

# Output
"Logic => 70"
"Problems => 60"