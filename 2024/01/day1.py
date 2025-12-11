def read_pairs(path):
    first = []
    second = []
    with open(path) as f:
        for line in f:
            n1, n2 = map(int, line.strip().split("   "))
            first.append(n1)
            second.append(n2)

    return first, second


def part1():
    first, second = read_pairs("data_1.1.csv")
    first.sort()
    second.sort()
    total = 0
    for i in range(len(first)):
        total += abs(first[i] - second[i])

    print(total)


def part2():
    first, second = read_pairs("data_1.csv")

    second_count = {}
    for num in second:
        second_count[num] = second_count.get(num, 0) + 1

    total = 0
    for num in first:
        total += second_count.get(num, 0) * num

    print(total)


part2()
