import os


def find_fully_overlapping_assignments(assignment_pairs: list[str]):
    result = []

    for pair in assignment_pairs:
        first_assignment, second_assignment = pair.split(',')
        first_start, first_end = [int(position)
                                  for position in first_assignment.split('-')]
        second_start, second_end = [int(position)
                                    for position in second_assignment.split('-')]
        if ((first_start >= second_start and first_end <= second_end)
                or (second_start >= first_start and second_end <= first_end)):
            result.append(pair)

    return result


def find_overlapping_assignments(assignment_pairs: list[str]):
    result = []

    for pair in assignment_pairs:
        first_assignment, second_assignment = pair.split(',')
        first_start, first_end = [int(position)
                                  for position in first_assignment.split('-')]
        second_start, second_end = [int(position)
                                    for position in second_assignment.split('-')]
        if ((first_start >= second_start and first_start <= second_end) or (first_end >= second_start and first_end <= second_end)
                or (second_start >= first_start and second_start <= first_end) or (second_end >= first_start and second_end <= first_end)):
            result.append(pair)

    return result


with open(os.path.join("input", "input.txt"), "r") as input_file:
    assignment_pairs = [line.strip() for line in input_file.readlines()]

fully_overlapping_assignments = len(
    find_fully_overlapping_assignments(assignment_pairs))
overlapping_assignments = len(
    find_overlapping_assignments(assignment_pairs))

print("The number of fully overlapping assignments is: " +
      str(fully_overlapping_assignments))
print("The number of assignment pairs that overlap at all is: " +
      str(overlapping_assignments))
