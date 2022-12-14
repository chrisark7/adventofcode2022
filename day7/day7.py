max_size = 100000

# Import input data
with open(r"C:\dev\personal\adventofcode2022\day7\input.txt") as f:
    data = [line.rstrip() for line in f]

line_num = 1
debug = 1
# Process
filesystem = {}
cur_dir = "/"
for line in data:
    # Is this line a command?
    if line.startswith("$"):
        # Is it a cd command?
        if line.startswith("$ cd"):
            # Is it taking us to the root directory?
            if line.startswith("$ cd /"):
                cur_dir = "/"
            # Is it telling us to move up one directory?
            elif line.startswith("$ cd .."):
                # Split the dir string from the end twice to remove the final slash and the directory
                cur_dir = cur_dir.rsplit(sep='/', maxsplit=2)[0] + "/"
                if cur_dir == '':
                    cur_dir = '/'
            # Otherwise it must be giving us a new lower directory
            else:
                cur_dir = cur_dir + line.removeprefix("$ cd ") + "/"
        # Is it an ls command?
        elif line.startswith("$ ls"):
            # Do nothing because we will capture this by knowing it isn't a command upon loop entry
            pass
    # This line is not a command, so it must be a dir or file listing
    elif line.startswith("dir"):
        # Do nothing for directory listings because we will capture them through the ls command
        pass
    # If not, this must be a file listing
    else:
        # Extract the filesize and filename
        flsz, flnm = line.split(' ')
        filesystem.setdefault(cur_dir, []).append([flnm, int(flsz)])
    if debug != '0':
        print(f" Line: {line_num}; Dir: {cur_dir}, Files: {filesystem.get(cur_dir, None)}")
        debug = input("   ...")
        line_num += 1

# Create a top-level sums dictionary
top_level_sums = {key: sum(n for _, n in val) for key, val in filesystem.items()}

# Create a sub-level sums directory
sub_level_sums = {key2: sum(val for key, val in top_level_sums.items() if key.startswith(key2)) for key2 in top_level_sums.keys()}

# Calculate total under the max and print to screen
tot_under_max = sum(val for key, val in sub_level_sums.items() if val <= max_size)
print(f"Total under the max is {tot_under_max}.")

