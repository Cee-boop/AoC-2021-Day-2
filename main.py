with open(file='data.txt') as file:
    data = [entry.split(" ") for entry in file.read().split("\n")]


def part_one(commands):
    h_pos, depth = 0, 0
    for command in commands:
        d, n = command[0][0], int(command[1])  # d = direction, n = number

        if d == "f":
            h_pos += n
        elif d == "d":
            depth += n
        else:
            depth -= n

    return print(h_pos * depth)


def part_two(commands):
    h_pos, depth, aim = 0, 0, 0
    for command in commands:
        d, n = command[0][0], int(command[1])  # d = direction, n = number

        if d == "f":
            h_pos += n
            depth += n * aim
        elif d == "d":
            aim += n
        else:
            aim -= n

    return print(h_pos * depth)


part_one(data)
part_two(data)
