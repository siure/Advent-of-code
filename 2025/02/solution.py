from pathlib import Path
here = Path(__file__).parent
data_path = here / "input.txt"

with open(data_path, "r") as f:
    data = f.read()


def part1():
    
    invalid_id = 0

    ranges = data.split(",")
    for Id in ranges:
        start, end = Id.split("-")
        for i in range(int(start),int(end)+1):
            current = str(i)
            length = len(current)
            if current[:(length+1)//2] == current[(length+1)//2:]:
                invalid_id += i


    print(invalid_id)
            

def getMultipleOfLength(length):
    multiples = []
    for i in range(1,(length+2)//2):
        if length % i ==0:
            multiples.append(i)
    return multiples

def part2():      
    #data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    
    invalid_id = 0
    ranges = data.split(",")
    for Id in ranges:
        start, end = Id.split("-")

        for i in range(int(start),int(end)+1):
            current = str(i)
            length = len(current)
            multiples = getMultipleOfLength(length)

            for multiple in multiples:
                firstPart = current[:multiple]
                valid = True

                for time in range(1,length//multiple):
                    if firstPart != current[multiple*time:multiple*(time+1)]:
                        valid = False
                        break
                if valid:
                    invalid_id += i
                    break

    print(invalid_id)

part2()


                






