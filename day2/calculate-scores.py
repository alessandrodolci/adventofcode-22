import os


def get_total_score_with_wrong_strategy_guide(strategies):
    result = 0

    for strategy in strategies:
        opponent_choice = ord(strategy[0]) - ord('A') + 1
        your_choice = ord(strategy[2]) - ord('X') + 1

        result += your_choice + \
            (((((your_choice - opponent_choice) % 3) + 1) % 3) * 3)

    return result


def get_total_score_with_correct_strategy_guide(strategies):
    result = 0

    for strategy in strategies:
        opponent_choice = ord(strategy[0]) - ord('A')
        round_result = ord(strategy[2]) - ord('X')

        figure_score = round_result * 3
        your_choice = ((opponent_choice + ((round_result - 1) % 3)) % 3) + 1
        result += your_choice + figure_score

    return result


with open(os.path.join("input", "input.txt"), "r") as input_file:
    strategies = [line.strip() for line in input_file.readlines()]

wrong_total_score = get_total_score_with_wrong_strategy_guide(strategies)
correct_total_score = get_total_score_with_correct_strategy_guide(strategies)

print("The total score obtained following the misinterpreted strategy guide is: " +
      str(wrong_total_score))
print("The total score obtained following the correct strategy guide is: " +
      str(correct_total_score))
