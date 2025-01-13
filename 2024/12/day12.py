def exploreRegion(i, j, visited, maps):
    if (i, j) in visited:
        return (0, 0)
    visited.add((i, j))

    area = 1
    perimeter = 0

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        areaAdd, perimeterAdd = 0, 0
        nx, ny = i + dx, j + dy
        if (
            0 <= nx < len(maps)
            and 0 <= ny < len(maps[i])
            and maps[i][j] == maps[nx][ny]
        ):
            areaAdd, perimeterAdd = exploreRegion(nx, ny, visited, maps)
        else:
            perimeter += 1
        area += areaAdd
        perimeter += perimeterAdd
    return (area, perimeter)


def part1():
    with open("2024/12/data_d12", "r") as f:
        data = f.read()

    map = [[char for char in line] for line in data.split("\n")]
    visited = set()
    cost = 0

    for i in range(len(map)):
        for j in range(len(map[0])):
            if not (i, j) in visited:

                area, perimeter = exploreRegion(i, j, visited, map)
                cost += area * perimeter

    print(cost)





def part2():
    with open("2024/12/data_d12", "r") as f:
        data = f.read()

    map = [[char for char in line] for line in data.split("\n") if line]
    plants = {(x, y) for y in range(len(map[0])) for x in range(len(map))}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    total_cost = 0
    regions = []
    
    def exploreRegionSides(i, j, region=None):
        if region is None:
            region = {}

        region[(i,j)] = {direction: 1 for direction in directions}
        plants.discard((i,j))
        

        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if (
                0 <= nx < len(map)
                and 0 <= ny < len(map[i])
                and map[i][j] == map[nx][ny]
            ):
                region[(i,j)][(dx,dy)] = 0
                if (nx,ny) not in region:
                    exploreRegionSides(nx,ny,region)

        return region

    while len(plants) > 0:
        i,j = plants.pop()
        regions.append(exploreRegionSides(i,j))

    normals = {(0, 1): (1, 0), (1, 0): (0, 1), (0, -1): (1, 0), (-1, 0): (0, 1)}
    for region in regions:
        for (x,y), plant in region.items():
            for direction, side in plant.items():
                if side == 1 and region.get((x + normals[direction][0], y+ normals[direction][1]),{}).get(direction,0) != 0:
                    plant[direction] = -1
                
    for region in regions:
        nbSides = 0
        for plant in region.values():
            for direction in plant.values():
                nbSides += max(direction,0)
        total_cost += len(region) * nbSides
    
    print(total_cost)
    
part2()
