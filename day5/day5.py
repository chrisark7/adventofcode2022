import re
import queue
import copy

# Define the initial queues for each column
q_inits = ['DTRBJLWG',
           'SWC',
           'RZTM',
           'DTCHSPV',
           'GPTLDZ',
           'FBRZJQCD',
           'SBDJMFTR',
           'LHRBTVM',
           'QPDSV']

# Import move instructions and remove the initial lines
with open(r"C:\dev\personal\adventofcode2022\day5\input.txt") as f:
    data = [line.rstrip() for line in f]
data = data[10:]

# Build initial queues for pt 1
queues = [queue.LifoQueue() for x in q_inits]
for i, q_init_n in enumerate(q_inits):
    for container in q_inits[i]:
        queues[i].put(container)

# Define regex to extricate instructions
re_moves = r"move (\d+) from (\d+) to (\d+)"

# Loop through all of the instructions
for d_num, d in enumerate(data):
    # Take out the key integers
    match = re.search(re_moves, d)
    num_conts = int(match.group(1))
    col_from = int(match.group(2)) - 1
    col_to = int(match.group(3)) -1
    # Execute instructions
    for i in range(num_conts):
        queues[col_to].put(queues[col_from].get(block=False))

# Produce the final string from the queues
out_string = ''.join(q.get(block=False) for q in queues)
print(f"Part 1: the top containers are {out_string}")

# Reproduce initial queues for pt2
queues = [queue.LifoQueue() for x in q_inits]
for i, q_init_n in enumerate(q_inits):
    for container in q_inits[i]:
        queues[i].put(container)

# Loop through all of the instructions
for d_num, d in enumerate(data):
    # Take out the key integers
    match = re.search(re_moves, d)
    num_conts = int(match.group(1))
    col_from = int(match.group(2)) - 1
    col_to = int(match.group(3)) -1
    # Initialize an intermediate queue
    temp_q = queue.LifoQueue()
    # Pop items into the temporary queue
    for i in range(num_conts):
        temp_q.put(queues[col_from].get(block=False))
    # Put items back into the queue
    for i in range(num_conts):
        queues[col_to].put(temp_q.get(block=False))

# Produce the final string from the queues
out_string = ''.join(q.get(block=False) for q in queues)
print(f"Part 2: the top containers are {out_string}")


