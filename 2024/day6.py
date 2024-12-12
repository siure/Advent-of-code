from collections import defaultdict


def part1():
    i, j = 0, 0
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    with open("data_d6") as f:
        for line in f:
            if "^" in line:
                for k in range(len(line)):
                    if line[k] == "^":
                        break
                    j += 1
                break
            i += 1
    file = open("data_d6", "r")
    content = file.read()
    lines = content.split("\n")

    maps = [list(line) for line in lines]

    coord = {}
    changeDir = 0
    while True:
        if not (0 <= i < len(maps)) or not (0 <= j < len(maps[0])):
            break
        while (
            maps[i + direction[changeDir % 4][0]][j + direction[changeDir % 4][1]]
            != "#"
        ):
            if not (0 <= i < len(maps)) or not (0 <= j < len(maps[0])):
                break
            coord[(i, j)] = True
            i += direction[changeDir % 4][0]
            j += direction[changeDir % 4][1]
        changeDir += 1
    print(len(coord))


def display_map(maps):
    for i in range(len(maps)):
        print(maps[i])
    print()


def is_in_loop(start_i, start_j, maps, direction):
    visited = set()
    i, j, d = start_i, start_j, 0

    while True:

        if (i, j, d) in visited:
            return True
        visited.add((i, j, d))

        next_i = i + direction[d][0]
        next_j = j + direction[d][1]
        if next_i < 0 or next_i >= len(maps) or next_j < 0 or next_j >= len(maps[0]):
            return False 

        if maps[next_i][next_j] == "#":
            d = (d + 1) % 4
        else:
            i, j = next_i, next_j


def part2():
    start_i, start_j = 0, 0
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    maps = []
    with open("data_d6") as f:
        for i, line in enumerate(f):
            line = line.strip() 
            maps.append(list(line)) 
            if "^" in line:
                start_i = i
                start_j = line.index("^") 

    changeDir = 0
    total = 0
    
    print(start_i,start_j)

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "." and (i, j) != (start_i, start_j):

                new_map = [row[:] for row in maps]

                new_map[i][j] = "#"
                if is_in_loop(start_i, start_j, new_map, direction):
                    total += 1 

    print(total)


part2()
