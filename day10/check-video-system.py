from enum import Enum
import os

X_RESOLUTION = 40
Y_RESOLUTION = 6


class Instruction(str, Enum):
    ADDX = "addx",
    NOOP = "noop"


def check_signal_strength(cycle: int, x: int, signal_strengths: list[int]):
    normalized_cycle = cycle - 20
    if normalized_cycle == 0 or (normalized_cycle % 40 == 0 and cycle <= 220):
        signal_strengths.append(cycle * x)


def get_signal_strength_sum(program: list[str]) -> int:
    signal_strengths: list[int] = []

    current_cycle = 0
    x = 1
    for instruction in program:
        tokens = instruction.split()

        if Instruction(tokens[0]) == Instruction.NOOP:
            current_cycle += 1
            check_signal_strength(current_cycle, x, signal_strengths)
        elif Instruction(tokens[0]) == Instruction.ADDX:
            current_cycle += 1
            check_signal_strength(current_cycle, x, signal_strengths)
            current_cycle += 1
            check_signal_strength(current_cycle, x, signal_strengths)
            x += int(tokens[1])

    return sum(signal_strengths)


def draw_pixel(pixel_position: int, sprite_position, pixels: list[str]):
    pixels[pixel_position] = '#' if pixel_position % X_RESOLUTION in [
        sprite_position-1, sprite_position, sprite_position+1] else '.'


def draw_on_screen(program: list[str], pixels: list[str]) -> None:
    current_cycle = 0
    sprite_position = 1
    for instruction in program:
        tokens = instruction.split()

        if Instruction(tokens[0]) == Instruction.NOOP:
            draw_pixel(current_cycle, sprite_position, pixels)
            current_cycle += 1
        elif Instruction(tokens[0]) == Instruction.ADDX:
            draw_pixel(current_cycle, sprite_position, pixels)
            current_cycle += 1
            draw_pixel(current_cycle, sprite_position, pixels)
            current_cycle += 1
            sprite_position += int(tokens[1])


with open(os.path.join("input", "input.txt"), "r") as input_file:
    program = [line.strip() for line in input_file.readlines()]

signal_strength_sum = get_signal_strength_sum(program)
pixels = ['.' for _ in range(X_RESOLUTION * Y_RESOLUTION)]
draw_on_screen(program, pixels)
print("The sum of the first six signal strengths is: " + str(signal_strength_sum))
print("The image rendered on the screen at the end of the program is:")
for i in range(Y_RESOLUTION):
    print(''.join(pixels[i*X_RESOLUTION:(i+1)*X_RESOLUTION]))
