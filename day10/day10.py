import numpy as np

# Import input data
with open(r"C:\dev\personal\adventofcode2022\day10\input.txt") as f:
    data = [line.rstrip() for line in f]


def execute_instr(instr_str, x_reg):
    # Split the instruction string into command and value if possible
    splt =  instr_str.split(' ')
    if len(splt) == 1 and splt[0] == 'noop':
        # Initially the register will be empty
        x_reg.append(x_reg[-1])
    else:
        # This is and addx command
        x_val = int(splt[1])
        x_reg.append(x_reg[-1])
        x_reg.append(x_reg[-1] + x_val)
    return x_reg

# Initialize the x register
x_reg = [1]

# Run through the instructions
for instr in data:
    x_reg = execute_instr(instr, x_reg)

# Multiply the correct indices
sig_str = [(i+1) * x_reg[i] for i in range(19, 220, 40)]

print(f"Part1: The sum of the signal strengths is {sum(sig_str)}")


# Part 2: Determine if the pixel is lit or not
pixels = []
for i, x_n in enumerate(x_reg):
    i_n = i % 40
    pixels.append(x_n - 1 <= i_n <= x_n + 1)

pixel_chars = ''.join(["#" if x else '.' for x in pixels])

for i in range(0, 240, 40):
    print(pixel_chars[i:(i+40)])
