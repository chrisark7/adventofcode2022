import numpy as np

# Import input data
with open(r"C:\dev\personal\adventofcode2022\day9\input.txt") as f:
    data = [line.rstrip() for line in f]


# Define a function to move the tail given the location of the head and the tail
def move_tail(tail, head):
    # Separate out the x and y portions to simplify notation
    tail_x = tail[0]
    tail_y = tail[1]
    head_x = head[0]
    head_y = head[1]
    sign_x = np.sign(head_x - tail_x)
    sign_y = np.sign(head_y - tail_y)
    # Remove all of the non-movement cases first
    if (abs(head_x - tail_x) <= 1) and (abs(head_y - tail_y) <= 1):
        tail_out = tail
    # If they are both on the same column
    elif tail_x == head_x:
        tail_out = (head_x, tail_y + sign_y)
    # If they are both on the same row
    elif tail_y == head_y:
        tail_out = (tail_x + sign_x, head_y)
    # If not, they are on a diagonal
    else:
        tail_out = (tail_x + sign_x, tail_y + sign_y)
    return tail_out


# Define a function to move the head given a letter input
def move_head(head, dir):
    if dir == 'R':
        head_out = (head[0] + 1, head[1])
    elif dir == 'L':
        head_out = (head[0] - 1, head[1])
    elif dir == 'U':
        head_out = (head[0], head[1] + 1)
    elif dir == 'D':
        head_out = (head[0], head[1] - 1)
    else:
        raise ValueError("Not a correct direction")
    return head_out

head_n = (0, 0)
tail_n = (0, 0)
tail_visits = [tail_n]
# Run through the instructions and find all the tail visits
for instruction in data:
    # Seperate the direction and the number of moves
    dir, num_moves = instruction.split(' ')
    num_moves = int(num_moves)
    # Iterate over the instructions moving the tail and the head each time
    while num_moves:
        head_n = move_head(head_n, dir)
        tail_n = move_tail(tail_n, head_n)
        tail_visits.append(tail_n)
        num_moves -= 1

print(f"Part 1: The tail visited {len(set(tail_visits))} positions")

## Part 2
# Intialize a 10-knot rope
N_knots = 10
knots = [(0, 0) for i in range(N_knots)]
tail_visits = [(0, 0)]
# Run through the instructions and find all of the tail visits
for instruction in data:
    # Seperate the direction and the number of moves
    dir, num_moves = instruction.split(' ')
    num_moves = int(num_moves)
    # Iterate over the instructions moving the tail and the head each time
    while num_moves:
        # Move the head
        knots[0] = move_head(knots[0], dir)
        # Move all of the other knots
        for i in range(1, N_knots):
            knots[i] = move_tail(knots[i], knots[i-1])
        # Store the latest tail position and decrement num_moves
        tail_visits.append(knots[-1])
        num_moves -= 1
    #print(knots)

print(f"Part 2: The tail visited {len(set(tail_visits))} positions")



