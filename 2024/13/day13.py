from math import sqrt
import re


def part1():
    with open("2024/13/data_d13", "r") as f:
        data = f.read()

    lines = data.splitlines()
    total = 0
    for i in range(len(lines) // 4 + 1):
        a = int(lines[i * 4][12:14]), int(lines[i * 4][18:20])
        b = int(lines[1 + i * 4][12:14]), int(lines[1 + i * 4][18:20])
        prize = int(lines[2 + i * 4].split("=")[1].split(",")[0]), int(
            lines[2 + i * 4].split("=")[2]
        )

        combinaison = []
        max_i = max(prize) // min(a)

        for i in range(max_i + 1):
            if (prize[0] - a[0] * i) % b[0] == 0:
                y1 = (prize[0] - a[0] * i) // b[0]
            else:
                continue

            if (prize[1] - a[1] * i) % b[1] == 0:
                y2 = (prize[1] - a[1] * i) // b[1]
            else:
                continue

            if y1 == y2:
                combinaison.append((i, y1))

        if combinaison != []:
            minCost = min(combinaison, key=lambda coord: 3 * coord[0] + coord[1])
            total += 3 * minCost[0] + minCost[1]
    print(total)


def part2():
    with open("2024/13/data_d13", "r") as f:
        data = f.read()

    lines = data.splitlines()
    total = 0
    for i in range(len(lines) // 4 + 1):
        a = int(lines[i * 4][12:14]), int(lines[i * 4][18:20])
        b = int(lines[1 + i * 4][12:14]), int(lines[1 + i * 4][18:20])
        prize = (
            int(lines[2 + i * 4].split("=")[1].split(",")[0]) + 10000000000000,
            int(lines[2 + i * 4].split("=")[2]) + 10000000000000,
        )

        x = (prize[0] * b[1] - prize[1] * b[0]) / (a[0] * b[1] - a[1] * b[0])
        y = (prize[1] - x * a[1]) / b[1]

        if x >= 0 and y >= 0 and x.is_integer() and y.is_integer():
            print(x, y, a, b)
            total += 3 * x + y

    print(total)


part2()
# 99423413811305
