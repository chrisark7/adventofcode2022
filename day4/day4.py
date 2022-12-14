import re

# Import the data
with open(r"C:\dev\personal\adventofcode2022\day4\input.txt") as f:
    data = [line.rstrip() for line in f]

# Define regex to capture integer groups
re_int_grps = r"(\d+)"

# Loop through the data and find subsets
tot_complete_subsets = 0
tot_any_overlap = 0
for d in data:
    # Pull out the integer groups
    st_1, end_1, st_2, end_2 = re.findall(re_int_grps, d)
    # Create sets to look for complete intersection
    e1 = set(range(int(st_1), int(end_1) + 1))
    e2 = set(range(int(st_2), int(end_2) + 1))
    # Check if either is a subset
    if e1.issubset(e2) | e2.issubset(e1):
        tot_complete_subsets += 1
    if len(e1.intersection(e2)) > 0:
        tot_any_overlap += 1

print(f"Part 1: The total which are complete subsets is {tot_complete_subsets}.")
print(f"Part 2: The total which have any overlap are {tot_any_overlap}.")


