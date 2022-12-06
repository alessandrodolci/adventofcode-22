import os

START_OF_PACKET_LENGTH = 4
START_OF_MESSAGE_LENGTH = 14


def get_count_to_first_marker(datastream, buffer_length):
    for i in range(len(datastream)):
        buffer = datastream[i:i+buffer_length]
        if len(set(buffer)) == buffer_length:
            return i + buffer_length

    raise ValueError("No start-of-packet found within the given datastream.")


with open(os.path.join("input", "input.txt"), "r") as input_file:
    datastream = input_file.readline().strip()

start_of_packet_position = get_count_to_first_marker(
    datastream, START_OF_PACKET_LENGTH)
start_of_message_position = get_count_to_first_marker(
    datastream, START_OF_MESSAGE_LENGTH)
print("The first start-of-packet marker occurs after {} characters.".format(start_of_packet_position))
print("The first start-of-message marker occurs after {} characters.".format(start_of_message_position))
