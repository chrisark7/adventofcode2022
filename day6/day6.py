# Import input data
with open(r"C:\dev\personal\adventofcode2022\day6\input.txt") as f:
    data = [line.rstrip() for line in f]
input_str = data[0]

#input_str = "bvwbjplbgvbhsrlpgdmjqwftvncz"

# Part 1: Loop over the string characters
num_chars = 4
for i in range(len(input_str) - num_chars):
    now_code = input_str[i:i+num_chars]
    if len(set(now_code)) == num_chars:
        break

final_char = i + num_chars
print(f"Part 1: The final character is number {final_char}")

# Part 2: look for 14 distinct characters
num_chars = 14
for i in range(len(input_str) - num_chars):
    now_code = input_str[i:i+num_chars]
    if len(set(now_code)) == num_chars:
        break

final_char = i + num_chars
print(f"Part 2: The final character is number {final_char}")
