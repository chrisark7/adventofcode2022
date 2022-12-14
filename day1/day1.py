
with open(r"C:\dev\personal\adventofcode2022\day1\input.txt") as f:
    data = [int(line.rstrip()) if line.rstrip() != '' else None for line in f]

# There are 251 elves:
# sum(1 if x is None else 0 for x in data) + 1

# Calculate the total calorie counts for each elf
elves = []
tot = 0
for val in data:
    if val is not None:
        tot += val
    else:
        elves.append(tot)
        tot = 0
elves.append(tot)

# Find the elf with the most calories
print(f"The elf carrying the most calories is carrying {max(elves)} calories.")

# Find the top three elves and sum their calories
elves.sort()
print(f"The top three elves are carrying {sum(elves[-3:])} calories.")
