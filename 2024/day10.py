def explore1(i, j, maps, visited):
    if (i, j) in visited:
        return 0
    visited.add((i, j))
    
    if maps[i][j] == 9:
        return 1

    score = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = i + dx, j + dy
        if 0 <= nx < len(maps) and 0 <=ny<  len(maps[i]) and maps[nx][ny] == maps[i][j] + 1:
            score += explore(nx,ny,maps,visited)

    return score


def part1():
    with open("2024/data_d10") as f:
        data = f.read()

    lines = data.split("\n")
    maps = [[int(char) for char in line] for line in lines]
    total = 0
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 0:
                visited = set()
                total += explore(i, j, maps, visited)

    print(total)


def explore2(i,j,last,maps):
    if  0 > i or i >= len(maps) or 0> j or j >= len(maps[i]) or maps[i][j] != last+1:
        return 0
    if maps[i][j] == 9:
        return 1
    return explore2(i-1,j,last+1,maps) + explore2(i+1,j,last+1,maps) + explore2(i,j-1,last+1,maps) + explore2(i,j+1,last+1,maps)

def part2():
    with open("2024/data_d10") as f:
        data = f.read()
        
    lines = data.split("\n")
    maps = [[int(char) for char in line] for line in lines]
    total = 0
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 0:
                print("Debut",i,j)
                total += explore2(i-1,j,0,maps) + explore2(i+1,j,0,maps) + explore2(i,j-1,0,maps) + explore2(i,j+1,0,maps)

    print(total)
    
part2()