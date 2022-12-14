import numpy as np

# Import input data
with open(r"C:\dev\personal\adventofcode2022\day8\input.txt") as f:
    data = [line.rstrip() for line in f]

# Convert to arrays of integers
data_arr = []
for row in data:
    data_arr.append([int(char) for char in row])
data_arr = np.array(data_arr)

# Create an array of booleans that is the same size with everything initialized to false
vis_arr = np.zeros_like(data_arr)
vis_arr = vis_arr.astype(bool)

# Set the outside values to be true
vis_arr[0, :] = True
vis_arr[-1, :] = True
vis_arr[:, 0] = True
vis_arr[:, -1] = True

# Determine the size of the array
max_rows, max_cols = data_arr.shape
# Look in from the left
for i in range(max_rows):
    for j in range(max_cols):
        ## Visibility from outside
        # Look from the left
        if np.all(data_arr[i, :j] < data_arr[i, j]):
            vis_arr[i, j] = True
        # Look from the right
        if np.all(data_arr[i, j] > data_arr[i, (j+1):]):
            vis_arr[i, j] = True
        # Look from the top
        if np.all(data_arr[:i, j] < data_arr[i, j]):
            vis_arr[i, j] = True
        # Look from the bottom
        if np.all(data_arr[i, j] > data_arr[(i+1):, j]):
            vis_arr[i, j] = True

print(f"The total number of trees visible from the outside is {np.sum(vis_arr)}")

## Visibility from inside
scenic_arr = np.empty((max_cols, max_rows, 4))
for i in range(max_rows):
    for j in range(max_cols):
        max_height = data_arr[i, j]
        # Look left from tree
        vis_trees = 0
        for k in reversed(range(0, j)):
            vis_trees += 1
            if data_arr[i, k] >= max_height:
                break
        scenic_arr[i, j, 0] = vis_trees
        # Look right from tree
        vis_trees = 0
        for k in range(j+1, max_rows):
            vis_trees += 1
            if data_arr[i, k] >= max_height:
                break
        scenic_arr[i, j, 1] = vis_trees
        # Look up
        vis_trees = 0
        for k in reversed(range(0, i)):
            vis_trees += 1
            if data_arr[k, j] >= max_height:
                break
        scenic_arr[i, j, 2] = vis_trees
        # Look down
        vis_trees = 0
        for k in range(i+1, max_rows):
            vis_trees += 1
            if data_arr[k, j] >= max_height:
                break
        scenic_arr[i, j, 3] = vis_trees

# Calculate scenic score
scenic_score = np.prod(scenic_arr, axis=2)

print(f"The highest scenic score is: {int(np.max(scenic_score))}")


