def part1():
    with open("2025/01/input.txt", "r") as f:
        data = f.read()
    password = 0
    dial = 50
    for line in data.splitlines():
        if line[0] == "L":
            dial = (dial - int(line[1:])) % 100
        elif line[0] == "R":
            dial = (dial + int(line[1:])) % 100

        if dial == 0:
            password += 1

    print(password)


def part2():
    with open("2025/01/input.txt", "r") as f:
        data = f.read()
    password = 0
    dial = 50
    for line in data.splitlines():
        clicks = int(line[1:])

        if line[0] == "L":
            password += ((dial - 1) // 100) - ((dial - clicks) // 100)
            dial = (dial - clicks) % 100

        elif line[0] == "R":
            password += (dial + clicks - 1) // 100
            dial = (dial + clicks) % 100

        if dial == 0:
            password += 1

    print(password)


part2()
