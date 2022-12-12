import os


def get_visible_trees(trees: list[list[str]]):
    length = len(trees[0])
    height = len(trees)

    result = length * 2 + (height - 2) * 2

    for i in range(1, length-1):
        for j in range(1, height-1):
            is_visible_from_left = True
            is_visible_from_right = True
            for k in range(0, length):
                if k != j and trees[i][k] >= trees[i][j]:
                    if k < j:
                        is_visible_from_left = False
                    elif k > j:
                        is_visible_from_right = False

            is_visible_from_top = True
            is_visible_from_bottom = True
            for k in range(0, height):
                if k != i and trees[k][j] >= trees[i][j]:
                    if k < i:
                        is_visible_from_top = False
                    elif k > i:
                        is_visible_from_bottom = False

            if is_visible_from_left or is_visible_from_right or is_visible_from_top or is_visible_from_bottom:
                result += 1

    return result


def get_highest_scenic_score(trees: list[list[str]]):
    length = len(trees[0])
    height = len(trees)

    result = 0
    for i in range(length):
        for j in range(height):
            left_visibility = 0
            k = j - 1
            while k >= 0:
                if trees[i][k] <= trees[i][j]:
                    left_visibility += 1
                    if trees[i][k] == trees[i][j]:
                        break
                else:
                    left_visibility += 1
                    break
                k -= 1
            right_visibility = 0
            for k in range(j+1, length):
                if trees[i][k] <= trees[i][j]:
                    right_visibility += 1
                    if trees[i][k] == trees[i][j]:
                        break
                else:
                    right_visibility += 1
                    break

            top_visibility = 0
            k = i - 1
            while k >= 0:
                if trees[k][j] <= trees[i][j]:
                    top_visibility += 1
                    if trees[k][j] == trees[i][j]:
                        break
                else:
                    top_visibility += 1
                    break
                k -= 1
            bottom_visibility = 0
            for k in range(i+1, height):
                if trees[k][j] <= trees[i][j]:
                    bottom_visibility += 1
                    if trees[k][j] == trees[i][j]:
                        break
                else:
                    bottom_visibility += 1
                    break

            print(i, j, left_visibility, right_visibility,
                  top_visibility, bottom_visibility)
            current_scenic_score = left_visibility * \
                right_visibility * top_visibility * bottom_visibility
            if current_scenic_score > result:
                result = current_scenic_score

    return result


with open(os.path.join("input", "input.txt"), "r") as input_file:
    tree_lines = [line.strip() for line in input_file.readlines()]

trees = [[char for char in line] for line in tree_lines]

visible_trees = get_visible_trees(trees)
highest_scenic_score = get_highest_scenic_score(trees)
print("The number of visible trees is: " + str(visible_trees))
print("The highest scenic score possible is: " + str(highest_scenic_score))
