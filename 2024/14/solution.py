def part1():
    with open("2024/14/data", "r") as f:
        data = f.read()

    robots = [
        (
            tuple(map(int, line.split()[0].split("=")[1].split(","))),
            tuple(map(int, line.split()[1].split("=")[1].split(","))),
        )
        for line in data.splitlines()
    ]
    wide = 101
    tall = 103
    finalPos = []
    for robot in robots:
        p = robot[0]
        v = robot[1]
        finalPos.append(((p[0] + v[0] * 100) % wide, (p[1] + v[1] * 100) % tall))
    quadrant = [0, 0, 0, 0]
    for pos in finalPos:
        if pos[0] < wide // 2:
            if pos[1] < tall // 2:
                print(pos)
                quadrant[0] += 1
            elif pos[1] > tall // 2:
                quadrant[1] += 1
        elif pos[0] > wide // 2:
            if pos[1] < tall // 2:
                quadrant[2] += 1
            elif pos[1] > tall // 2:
                quadrant[3] += 1

    print(quadrant[0] * quadrant[1] * quadrant[2] * quadrant[3])


def part2():
    import numpy

    with open("2024/14/data", "r") as f:
        data = f.read()

    robots = [
        [
            list(map(int, line.split()[0].split("=")[1].split(","))),
            tuple(map(int, line.split()[1].split("=")[1].split(","))),
        ]
        for line in data.splitlines()
    ]

    wide = 101
    tall = 103
    min_std = None
    min_i = 0
    for i in range(10_000):
        for robot in robots:
            robot[0][0] = (robot[0][0] + robot[1][0]) % wide
            robot[0][1] = (robot[0][1] + robot[1][1]) % tall

        std = numpy.std([robot[0][0] for robot in robots]) + numpy.std(
            [robot[0][1] for robot in robots]
        )
        if min_std is None or std < min_std:
            min_std = std
            min_i = i

    print(min_i + 1,min_std)


part2()
