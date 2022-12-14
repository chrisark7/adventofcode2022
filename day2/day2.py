# Part 1 keys
# Define a win-loss guide
win_loss_key = {
    'A X': 3, # Rock - Rock
    'A Y': 6, # Rock - Paper
    'A Z': 0, # Rock - Scissors
    'B X': 0, # Paper - Rock
    'B Y': 3, # Paper - Paper
    'B Z': 6, # Paper - Scissors
    'C X': 6, # Scissors - Rock
    'C Y': 0, # Scissors - Paper
    'C Z': 3, # Scissors - Scissors
}

# Define a point guide for my throw
throw_key = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

# Part 2 keys
# Define a win-loss guide
pt2_win_loss_key = {
    'A X': 3 + 0, # Rock - Lose = Scissors
    'A Y': 1 + 3, # Rock - Draw = Rock
    'A Z': 2 + 6, # Rock - Win = Paper
    'B X': 1 + 0, # Paper - Lose = Rock
    'B Y': 2 + 3, # Paper - Draw = Paper
    'B Z': 3 + 6, # Paper - Win = Scissors
    'C X': 2 + 0, # Scissors - Lose = Paper
    'C Y': 3 + 3, # Scissors - Draw = Scissors
    'C Z': 1 + 6, # Scissors - Win = Rock
}



# Import the data
with open(r"C:\dev\personal\adventofcode2022\day2\input.txt") as f:
    data = [line.rstrip() for line in f]

# Calculate win-loss points and throw points
throw_pts = [throw_key[line[-1]] for line in data]
win_loss_pts = [win_loss_key[line] for line in data]
pt2_win_loss_pts = [pt2_win_loss_key[line] for line in data]

# Print the total points for part 1
print(f"The total points for part 1 are {sum(throw_pts) + sum(win_loss_pts)}.")

# Print the total points for part 2
print(f"The total points for part 2 are {sum(pt2_win_loss_pts)}.")
