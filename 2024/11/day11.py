def part1():
    with open("2024/data_d11") as f:
        data = f.read()
    data = [int(num) for num in data.split()]
    for i in range(25):
        print(i)
        j = 0
        while j < len(data):
            if data[j] == 0:
                data[j] = 1
            elif len(str(data[j])) % 2 == 0:
                data.insert(j, int(str(data[j])[: len(str(data[j])) // 2]))
                data[j + 1] = int(str(data[j + 1])[len(str(data[j + 1])) // 2 :])
                j += 1
            else:
                data[j] *= 2024
            j += 1
    print(len(data))


def part2():
    with open("2024/data_d11") as f:
        data = f.read()

    stones = {int(num): 1 for num in data.split()}

    for i in range(75):
        temp = {}

        if stones.get(0, 0) > 0:
            temp[1] = stones[0]
            stones.pop(0)
        for stone_i, nb in stones.items():
            size = len(str(stone_i))

            if size % 2 == 0:
                left = int(str(stone_i)[: size // 2])
                right = int(str(stone_i)[size // 2 :])
                temp[left] = temp.get(left, 0) + nb
                temp[right] = temp.get(right, 0) + nb
            else:
                temp[stone_i * 2024] = temp.get(stone_i * 2024, 0) + nb

        stones = temp

    total = sum(stones.values())
    print(total)


part2()
