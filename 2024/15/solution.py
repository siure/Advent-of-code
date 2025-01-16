def part1():
    with open("2024/15/data", "r") as f:
        data = f.read()

    map = []
    movesList = []
    isMap = True
    pos = [0, 0]
    for line in data.splitlines():
        if line == "":
            isMap = False

        if not isMap:
            movesList.append(line)
        else:
            map.append(list(line))

    pos = next(
        (
            (i, j)
            for i, sublist in enumerate(map)
            for j, c in enumerate(sublist)
            if c == "@"
        )
    )

    direction = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    for moves in movesList:
        for move in moves:
            dir = direction[move]
            next_pos = (pos[0] + dir[0], pos[1] + dir[1])
            if map[next_pos[0]][next_pos[1]] == ".":
                map[pos[0]][pos[1]] = "."
                map[pos[0] + dir[0]][pos[1] + dir[1]] = "@"
                pos = (pos[0] + dir[0], pos[1] + dir[1])
            elif map[next_pos[0]][next_pos[1]] == "O":
                while map[next_pos[0]][next_pos[1]] == "O":
                    next_pos = (next_pos[0] + dir[0], next_pos[1] + dir[1])
                if map[next_pos[0]][next_pos[1]] == ".":
                    map[pos[0]][pos[1]] = "."
                    map[pos[0] + dir[0]][pos[1] + dir[1]] = "@"
                    map[next_pos[0]][next_pos[1]] = "O"
                    pos = (pos[0] + dir[0], pos[1] + dir[1])

    total = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "O":
                total += (i) * 100 + j
    print(total)


def part2():
    with open("2024/15/data", "r") as f:
        data = f.read()

    map = []
    movesList = []
    isMap = True
    pos = [0, 0]
    for line in data.splitlines():
        if line == "":
            isMap = False

        if not isMap:
            movesList.append(line)
        else:
            map.append([])
            for char in line:
                if char == "#":
                    map[-1].append("#")
                    map[-1].append("#")
                elif char == "O":
                    map[-1].append("[")
                    map[-1].append("]")
                elif char == ".":
                    map[-1].append(".")
                    map[-1].append(".")
                elif char == "@":
                    map[-1].append("@")
                    map[-1].append(".")

    pos = next(
        (
            (i, j)
            for i, sublist in enumerate(map)
            for j, c in enumerate(sublist)
            if c == "@"
        )
    )

    direction = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    for moves in movesList:
        for move in moves:
            dir = direction[move]
            next_pos = (pos[0] + dir[0], pos[1] + dir[1])
            if map[next_pos[0]][next_pos[1]] == ".":
                map[pos[0]][pos[1]] = "."
                map[pos[0] + dir[0]][pos[1] + dir[1]] = "@"
                pos = (pos[0] + dir[0], pos[1] + dir[1])
            elif (
                map[next_pos[0]][next_pos[1]] == "["
                or map[next_pos[0]][next_pos[1]] == "]"
            ):
                boxes = []
                if move == ">" or move == "<":
                    while (
                        map[next_pos[0]][next_pos[1]] == "["
                        or map[next_pos[0]][next_pos[1]] == "]"
                    ):
                        boxes.append((next_pos,map[next_pos[0]][next_pos[1]]))
                        next_pos = (next_pos[0] + dir[0], next_pos[1] + dir[1])
                    if map[next_pos[0]][next_pos[1]] == ".":
                        
                        for box in boxes:
                            map[box[0][0] + dir[0]][box[0][1] + dir[1]] = box[1]
                        map[pos[0]][pos[1]] = "."
                        map[pos[0] + dir[0]][pos[1] + dir[1]] = "@"
                        pos = (pos[0] + dir[0], pos[1] + dir[1])
                    
                else:
                    pile = {
                        next_pos,
                        (next_pos[0], next_pos[1] + 1) if map[next_pos[0]][next_pos[1]] == "[" else (next_pos[0], next_pos[1] - 1)
                    }

                    isMovable = True
                    while pile:
                        box_pos = pile.pop()  
                        next_box_pos = (box_pos[0] + dir[0], box_pos[1] + dir[1])
                        
                        if map[next_box_pos[0]][next_box_pos[1]] == "[":
                            pile.update(
                                {next_box_pos, (next_box_pos[0], next_box_pos[1] + 1)}
                            )
                        elif map[next_box_pos[0]][next_box_pos[1]] == "]":
                            pile.update(
                                {next_box_pos, (next_box_pos[0], next_box_pos[1] - 1)}
                            )
                        elif map[next_box_pos[0]][next_box_pos[1]] == "#":
                            isMovable = False
                            break
                        
                        boxes.append((box_pos, map[box_pos[0]][box_pos[1]]))

                    if isMovable:
                        for box in boxes:
                            map[box[0][0] ][box[0][1] ] = '.'
                        for box in boxes:
                            map[box[0][0] + dir[0]][box[0][1] + dir[1]] = box[1]
                        map[pos[0]][pos[1]] = "."
                        map[pos[0] + dir[0]][pos[1] + dir[1]] = "@"
                        pos = (pos[0] + dir[0], pos[1] + dir[1])
                        

    total = 0
    
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "[":
                total += (i) * 100 + j
    print(total)


part2()
