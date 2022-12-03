import os


def get_priorities_within_rucksacks(rucksacks: list[str]):
    priorities = []

    for rucksack in rucksacks:
        first_compartment = rucksack[0:len(rucksack)//2]
        second_compartment = rucksack[len(rucksack)//2:]

        try:
            common_char = next(
                char for char in second_compartment if char in first_compartment)
            priorities.append(ord(common_char) - ord('A') +
                              27 if common_char.isupper() else ord(common_char) - ord('a') + 1)
        except StopIteration:
            print("Unexpected error: no common character found in the two compartments")
            exit(1)

    return priorities


def get_priorities_among_groups(rucksacks: list[str]):
    priorities = []

    for i in range(0, len(rucksacks), 3):
        group = rucksacks[i:i+3]
        try:
            common_char = next(
                char for char in group[2] if char in group[0] and char in group[1])
            priorities.append(ord(common_char) - ord('A') +
                              27 if common_char.isupper() else ord(common_char) - ord('a') + 1)
        except StopIteration:
            print("Unexpected error: no common character found in the two compartments")
            exit(1)

    return priorities


with open(os.path.join("input", "input.txt"), "r") as input_file:
    rucksacks = [line.strip() for line in input_file.readlines()]

priorities_within_rucksacks_sum = sum(
    get_priorities_within_rucksacks(rucksacks))
priorities_among_groups = sum(get_priorities_among_groups(rucksacks))

print("The sum of priorities of each item types appearing in both compartments is: " +
      str(priorities_within_rucksacks_sum))
print("The sum of priorities of each item types corresponding to the badge of each group of three is: " +
      str(priorities_among_groups))
