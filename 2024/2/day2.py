def part1():

    total = 0
    with open("data_d2") as f:
        for line in f:
            total += 1
            
            unusual = list(maps(int, line.strip().split(" ")))
            change = -1 if (unusual[0] - unusual[1]) > 0 else 1
            for i in range(0, len(unusual) - 1):
                increment = unusual[i] - unusual[i + 1]
                if not (0 < abs(increment) <= 3) or ( increment * change > 0):
                    total -= 1
                    break

    print(total)

def part2():
    total = 0
    with open("data_d2") as f:
        for line in f:
            unusual = list(maps(int, line.strip().split(" ")))
            for i in range(len(unusual)):
                truncated = unusual[:i] + unusual[i + 1:]
                diffs = [truncated[i]- truncated[i+1] for i in range(len(truncated)-1)]
                
                if all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs): 
                    total+= 1
                    break
    print(total)
    
part2()
            
            

      