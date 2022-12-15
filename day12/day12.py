import copy
import numpy as np


# Define a function to return all valid moves given a point
def valid_moves(point, data_arr):
    out = []
    # Try to move up and make sure we don't fall off the grid
    if point[0] > 0:
        point_n = (point[0] - 1, point[1])
        # Check that it isn't too high
        if data_arr[point_n] <= data_arr[point] + 1:
            out.append(point_n)
    # Try to move down and make sure we don't fall off the grid
    if point[0] < data_arr.shape[0] - 1:
        point_n = (point[0] + 1, point[1])
        # Check that it isn't too high
        if data_arr[point_n] <= data_arr[point] + 1:
            out.append(point_n)
    # Try to move left and make sure we don't fall off the grid
    if point[1] > 0:
        point_n = (point[0], point[1] - 1)
        # Check that it isn't too high
        if data_arr[point_n] <= data_arr[point] + 1:
            out.append(point_n)
    # Try to move right and make sure we don't fall off the grid
    if point[1] < data_arr.shape[1] - 1:
        point_n = (point[0], point[1] + 1)
        # Check that it isn't too high
        if data_arr[point_n] <= data_arr[point] + 1:
            out.append(point_n)
    return out

def find_best_path(start_point, end_point, data_arr):
    # Begin exploring the paths
    end_found = False
    paths = [[start_point]]
    seen_points = set([start_point])
    iteration = 0
    while not end_found:
        next_paths = []
        for path in paths:
            # Find all possible points from the end point of this path
            pos_points = valid_moves(path[-1], data_arr)
            # Make sure that we haven't alread seen this point
            pos_points = [pnt for pnt in pos_points if pnt not in seen_points]
            # Check if we found the end point
            if end_point in pos_points:
                end_found = True
                best_path = path + [end_point]
                break
            # Append the new paths
            # Note, if there are not possible points then this is a dead end and will not show up in the next paths
            for pnt in pos_points:
                next_paths.append(path + [pnt])
            # Add the end points to the seen points
            for pnt in pos_points:
                seen_points.add(pnt)
        # Prepare the paths for the next iteration
        paths = next_paths
        # If the paths are empty, then we can't make it to the end
        if not paths:
            end_found = True
            best_path = []
            break
        '''
        # Feedback
        iteration += 1
        print(f"Iteration {iteration} complete.  There are {len(paths)} for the next iteration.")
        if iteration == 600:
            break
        '''
    return best_path

def find_bs_by_as(data_arr):
    out = []
    # Find all indices where the value is 0 (i.e. an 'a')
    zero_inds = np.transpose((data_arr == 0).nonzero())
    # Iterate through these
    for ind_n in zero_inds:
        point = tuple(ind_n)
        # Try to move up and make sure we don't fall off the grid
        if point[0] > 0:
            point_n = (point[0] - 1, point[1])
            # Check if it is a one
            if data_arr[point_n] == 1:
                out.append(point)
                continue
        # Try to move down and make sure we don't fall off the grid
        if point[0] < data_arr.shape[0] - 1:
            point_n = (point[0] + 1, point[1])
            # Check that it isn't too high
            if data_arr[point_n] == 1:
                out.append(point)
                continue
        # Try to move left and make sure we don't fall off the grid
        if point[1] > 0:
            point_n = (point[0], point[1] - 1)
            # Check that it isn't too high
            if data_arr[point_n] == 1:
                out.append(point)
                continue
        # Try to move right and make sure we don't fall off the grid
        if point[1] < data_arr.shape[1] - 1:
            point_n = (point[0], point[1] + 1)
            # Check that it isn't too high
            if data_arr[point_n] == 1:
                out.append(point)
                continue
    return out



# Scripting
if __name__ == "__main__":
    # Import input data and cast as a numpy array
    with open(r"C:\dev\personal\adventofcode2022\day12\input.txt") as f:
        data = [line.rstrip() for line in f]
    # Convert the data to individual letters instead of strings
    data = [[char for char in row] for row in data]

    # Find the start and end indices
    char_arr = np.array(data)
    start_point = np.where(char_arr == 'S')
    start_point = (start_point[0][0], start_point[1][0])
    end_point = np.where(char_arr == 'E')
    end_point = (end_point[0][0], end_point[1][0])

    # Create an alphabet array to map letters to heights including the start and end points
    alpha_map = {char: i for i, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
    alpha_map['S'] = 0
    alpha_map['E'] = 25

    # Remap the data to numerical values
    data_arr = np.array([[alpha_map[char] for char in row] for row in data])

    # Find the best path for part 1
    best_path = find_best_path(start_point, end_point, data_arr)

    # Print the Part 1 result
    print(f"Part 1: The shortest number of moves is {len(best_path) - 1}")

    # Find the best path for part 2
    best_paths = []
    # Find all indices where the value is 0 (i.e. an 'a')
    zero_inds = np.transpose((data_arr == 0).nonzero())
    i = 0
    for ind_n in zero_inds:
        # Convert to tuple
        start_point_n = tuple(ind_n)
        #print(f"Trying point {start_point_n}")
        # Calculate the best path
        best_path_n = find_best_path(start_point_n, end_point, data_arr)
        # Keep all paths, even the empty ones
        best_paths.append(best_path_n)
        # Feedback
        i += 1
        #print(f"Finished point {start_point_n} (iteration {i}) with path length {len(best_paths[-1]) + 1}")

    # Calculate the shortest path length sorting out the empty ones
    path_lens = [len(path) + 1 for path in best_paths if path]
    print(f"Part 2: The shortest path has {min(path_lens)} moves.")




