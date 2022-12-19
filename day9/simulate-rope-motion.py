from enum import Enum
import os


class Direction(str, Enum):
    U = 'U',
    D = 'D',
    L = 'L',
    R = 'R'


def move_one_step(current_position: tuple[int, int], direction: Direction) -> tuple[int, int]:
    if direction == Direction.U:
        return (current_position[0], current_position[1] + 1)
    elif direction == Direction.D:
        return (current_position[0], current_position[1] - 1)
    elif direction == Direction.L:
        return (current_position[0] - 1, current_position[1])
    elif direction == Direction.R:
        return (current_position[0] + 1, current_position[1])
    else:
        raise ValueError("Invalid direction value")


def move_tail(current_head_position: tuple[int, int], current_tail_position: tuple[int, int]) -> tuple[int, int]:
    x_delta = current_head_position[0] - current_tail_position[0]
    y_delta = current_head_position[1] - current_tail_position[1]

    if abs(x_delta) == 2 and abs(y_delta) == 2:
        next_tail_x = current_tail_position[0] + x_delta//2
        next_tail_y = current_tail_position[1] + y_delta//2
        return (next_tail_x, next_tail_y)
    if abs(x_delta) == 2 and (abs(y_delta) == 0 or abs(y_delta) == 1):
        next_tail_x = current_tail_position[0] + x_delta//2
        next_tail_y = current_head_position[1] if abs(
            y_delta) == 1 else current_tail_position[1]
        return (next_tail_x, next_tail_y)
    elif abs(y_delta) == 2 and (abs(x_delta) == 0 or abs(x_delta) == 1):
        next_tail_x = current_head_position[0] if abs(
            x_delta) == 1 else current_tail_position[0]
        next_tail_y = current_tail_position[1] + y_delta//2
        return (next_tail_x, next_tail_y)
    else:
        return (current_tail_position[0], current_tail_position[1])


def get_visited_positions_with_two_knots(motions: list[str]) -> int:
    head_position = (0, 0)
    tail_position = (0, 0)
    visited_positions: set[tuple[int, int]] = {(0, 0)}
    for motion in motions:
        direction, units = motion.split()[0], int(motion.split()[1])
        for _ in range(units):
            try:
                head_position = move_one_step(
                    head_position, Direction(direction))
            except ValueError:
                exit(1)
            tail_position = move_tail(head_position, tail_position)
            visited_positions.add(tail_position)

    return len(visited_positions)


def get_visited_positions_with_n_knots(motions: list[str], knots_count: int) -> int:
    knots_positions: list[tuple[int, int]] = [
        (0, 0) for _ in range(knots_count)]
    visited_positions: set[tuple[int, int]] = {(0, 0)}
    for motion in motions:
        direction, units = motion.split()[0], int(motion.split()[1])
        for _ in range(units):
            try:
                knots_positions[0] = move_one_step(
                    knots_positions[0], Direction(direction))
            except ValueError:
                exit(1)
            for i in range(1, len(knots_positions)):
                knots_positions[i] = move_tail(
                    knots_positions[i-1], knots_positions[i])
            visited_positions.add(knots_positions[len(knots_positions)-1])

    return len(visited_positions)


with open(os.path.join("input", "input.txt"), "r") as input_file:
    motions = [line.strip() for line in input_file.readlines()]

visited_positions_with_two_knots = get_visited_positions_with_two_knots(
    motions)
visited_positions_with_ten_knots = get_visited_positions_with_n_knots(
    motions, 10)
print("The number of positions visited at least once by the tail of a two-knots rope is: " +
      str(visited_positions_with_two_knots))
print("The number of positions visited at least once by the tail of a ten-knots rope is: " +
      str(visited_positions_with_ten_knots))
