from collections import defaultdict


def part1():
    symobls = defaultdict(list)
    total = 0
    with open("data_d8", "r") as f:
        data = [list(line) for line in f.read().splitlines()]
    lenx = len(data)
    leny = len(data[0])

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != ".":
                symobls[data[i][j]].append((i, j))

    for key in symobls.keys():
        coords = symobls[key]
        for coord1 in coords:
            for coord2 in coords:
                if coord1 == coord2:
                    continue
                vec = (coord1[0] - coord2[0], coord1[1] - coord2[1])
                point = (vec[0] + coord1[0], vec[1] + coord1[1])
                if (
                    0 <= point[0] < leny
                    and 0 <= point[1] < lenx
                    and data[point[0]][point[1]] != "#"
                ):
                    data[point[0]][point[1]] = "#"
                    total += 1
    print(total)


def part2():
    symobls = defaultdict(list)
    total = 0
    with open("data_d8", "r") as f:
        data = [list(line) for line in f.read().splitlines()]
    lenx = len(data)
    leny = len(data[0])

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != ".":
                symobls[data[i][j]].append((i, j))

    for key in symobls.keys():
        coords = symobls[key]
        for coord1 in coords:
            for coord2 in coords:
                if coord1 == coord2  :
                    if data[coord1[0]][coord1[1]] != "#":
                        data[coord1[0]][coord1[1]] = "#"
                        total += 1
                    continue
                vec = (coord1[0] - coord2[0], coord1[1] - coord2[1])
                point = (vec[0] + coord1[0], vec[1] + coord1[1])
                while 0 <= point[0] < leny and 0 <= point[1] < lenx:
                    if data[point[0]][point[1]] != "#":
                        data[point[0]][point[1]] = "#"
                        total += 1
                    point = (vec[0] + point[0], vec[1] + point[1])

    print(total)


part2()
