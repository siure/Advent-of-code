def part1():
    total = 0

    with open("data_d3") as f:
        for line in f:
            for i in range(len(line) - 8):
                if line[i : i + 4] == "mul(":
                    num1 = ""
                    num2 = ""
                    for j in range(4):
                        num1 += line[i + j + 4]
                        if line[i + j + 4] == ",":
                            break
                    if not num1[-1] == ",":
                        continue
                    num1 = num1[:-1]
                    if not num1.strip().isdigit():
                        continue
                    for j in range(4):
                        num2 += line[i + j + 5 + len(num1)]
                        if line[i + j + 5 + len(num1)] == ")":
                            break
                    if not num2[-1] == ")":
                        continue
                    num2 = num2[:-1]
                    if not num2.strip().isdigit():
                        continue
                    total += int(num1) * int(num2)
                    i += 8 + len(num1) + len(num2)
    print(total)
    
def part2():
    total = 0
    is_execute = True
    with open("data_d3") as f:
        for line in f:
            for i in range(len(line) - 8):
                if line[i : i + 4] == "mul(" and is_execute:
                    num1 = ""
                    num2 = ""
                    for j in range(4):
                        num1 += line[i + j + 4]
                        if line[i + j + 4] == ",":
                            break
                    if not num1[-1] == ",":
                        continue
                    num1 = num1[:-1]
                    if not num1.strip().isdigit():
                        continue
                    for j in range(4):
                        num2 += line[i + j + 5 + len(num1)]
                        if line[i + j + 5 + len(num1)] == ")":
                            break
                    if not num2[-1] == ")":
                        continue
                    num2 = num2[:-1]
                    if not num2.strip().isdigit():
                        continue
                    total += int(num1) * int(num2)
                    i += 8 + len(num1) + len(num2)
                if line[i : i + 7] == "don't()":
                    i += 7
                    is_execute = False
                if line[i : i + 2] == "do":
                    i += 2
                    is_execute = True
                
    print(total) 

#195980
part2()
