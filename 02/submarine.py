def calculate_position(commands):
    horizontal_position = 0
    depth = 0

    for command in commands:
        direction, value = command.split()
        value = int(value)

        if direction == "forward":
            horizontal_position += value
        elif direction == "down":
            depth += value
        elif direction == "up":
            depth -= value

    return horizontal_position, depth

# # Example input
# commands = [
#     "forward 5",
#     "down 5",
#     "forward 8",
#     "up 3",
#     "down 8",
#     "forward 2"
# ]

# Read commands from input.txt
with open('input.txt', "r") as file:
    commands = file.read().splitlines()

horizontal_position, depth = calculate_position(commands)
result = horizontal_position * depth

print(f"Horizontal Position: {horizontal_position}, Depth: {depth}, Result: {result}")