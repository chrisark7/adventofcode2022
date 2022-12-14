import string

# Create the alphabet key with upper and lowercase letters
alpha_key = {let:val for let, val in zip(string.ascii_lowercase, range(1, 27))}
alpha_key.update({let:val for let, val in zip(string.ascii_uppercase, range(27, 53))})

# Import the data
with open(r"C:\dev\personal\adventofcode2022\day3\input.txt") as f:
    data = [line.rstrip() for line in f]


## Part 1
# Look for common letters in first and second half of strings
com_lets = []
for d in data:
    # Calculate length of string halves (keeping it an integer for slicing)
    l = len(d)//2
    # Create sets of the front and second halves
    set_front = set(d[0:l])
    set_back = set(d[l:2*l])
    # Check for the intersection of the two sets
    intsct = set_front.intersection(set_back)
    # If the length is greater than one, raise an error
    if len(intsct) > 1:
        raise("Intersection contains multiple elements")
    # Store the intersection in the common letter list
    com_lets.append(intsct.pop())

# Calculate the sum of the priorities
tot_val = sum([alpha_key[x] for x in com_lets])
print(f"Part 1: The sum of priorities is {tot_val}")

## Part 2
# Iterate over the three line groups
com_lets_pt2 = []
for i in range(0, len(data), 3):
    # Pull out the three elves rucksack contents as sets
    e1 = set(data[i])
    e2 = set(data[i+1])
    e3 = set(data[i+2])
    # Look for the intersection of all three
    intsct = e1.intersection(e2)
    intsct = intsct.intersection(e3)
    # If the length is greater than one, raise an error
    if len(intsct) > 1:
        raise("Intersection contains multiple elements")
    # Store the common letter
    com_lets_pt2.append(intsct.pop())

# Calculate the sum of priorities
tot_val_pt2 = sum([alpha_key[x] for x in com_lets_pt2])
print(f"Part 2: The sum of priorities is {tot_val_pt2}")

