import os


def simulate_rearrangement_9000(stacks: list[list[str]], plan: list[str]):
    result = []
    for stack in stacks:
        result.append(stack.copy())

    for line in plan:
        tokens = line.split()
        count = int(tokens[1])
        from_stack = int(tokens[3]) - 1
        to_stack = int(tokens[5]) - 1

        for _ in range(count):
            result[to_stack].append(result[from_stack].pop())

    return result


def simulate_rearrangement_9001(stacks: list[list[str]], plan: list[str]):
    result = []
    for stack in stacks:
        result.append(stack.copy())

    for line in plan:
        tokens = line.split()
        count = int(tokens[1])
        from_stack = int(tokens[3]) - 1
        to_stack = int(tokens[5]) - 1

        crates_to_move = []
        for _ in range(count):
            crates_to_move.append(result[from_stack].pop())
        for _ in range(count):
            result[to_stack].append(crates_to_move.pop())

    return result


with open(os.path.join("input", "input.txt"), "r") as input_file:
    description = [line[0:len(line)-1] for line in input_file.readlines()]

stacks: list[list[str]] = []

line = description.pop(0)
while line:
    last_stack_in_line = (len(line) + 1) // 4
    if len(stacks) < last_stack_in_line:
        for i in range(last_stack_in_line):
            stacks.append([])

    for i in range(1, len(line) + 1, 4):
        if line[i].isalpha():
            stacks[i//4].append(line[i])

    line = description.pop(0)

for stack in stacks:
    stack.reverse()

rearranged_stacks_9000 = simulate_rearrangement_9000(stacks, description)
message_9000 = ''.join([stack[len(stack)-1]
                       for stack in rearranged_stacks_9000])
rearranged_stacks_9001 = simulate_rearrangement_9001(stacks, description)
message_9001 = ''.join([stack[len(stack)-1]
                       for stack in rearranged_stacks_9001])

print("The crates that end up at the top of each stack after the rearrangement with crane model 9000 are: " + message_9000)
print("The crates that end up at the top of each stack after the rearrangement with crane model 9001 are: " + message_9001)
