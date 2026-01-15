nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums.union(letters))

print(nums | letters)

merged = nums.copy()
merged.update(letters)
print(merged)

# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}