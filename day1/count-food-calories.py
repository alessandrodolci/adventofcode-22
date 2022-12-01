import os


def get_calories_counts(calories):
    counts = []

    current_count = 0
    for quantity in calories:
        if not quantity:
            counts.append(current_count)
            current_count = 0
        elif quantity:
            current_count += int(quantity)

    return counts


with open(os.path.join("input", "input.txt"), "r") as input_file:
    calories = [line.strip() for line in input_file.readlines()]

    calories_count = get_calories_counts(calories)
    highest_calories_quantity = max(calories_count)

    calories_count.sort(reverse=True)
    top_three_counts_sum = sum(calories_count[0:3])

print("The highest calories quantity carried by an elf is: " +
      str(highest_calories_quantity))
print("The sum of the top three calories counts is: " + str(top_three_counts_sum))
