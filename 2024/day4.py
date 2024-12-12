def part1():
    
    def search_xmas(x,y,direction,charac):
        word = "XMAS"
        for i in range(4):
            if not (0 <= x < lenx and 0 <= y < leny):
                return False
            if not charac[x][y] == word[i]:
                return False
            x += direction[0]
            y += direction[1]
        return True
                
            
    
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    total =0
    

    file = open("data_d4",'r')
    content = file.read()
    lines = content.split("\n")
    
    charac = [list(line) for line in lines]
    lenx = len(charac)
    leny = len(charac[0])
    for i in range(lenx):
        for j in range(leny):
            for direction in directions:
                    if search_xmas(i,j,direction,charac):
                        total += 1
                            
    print(total)

def part2():
    def search_mas(x, y, charac):
        word = "MS"
        diag1 = [(1, 1), (-1, -1)]
        diag2 = [(1, -1), (-1, 1)]
        
        for i in range(2):
            if not (0 <= x + diag1[i][0] < lenx and 0 <= y + diag1[i][1] < leny):
                return False
            if not (0 <= x + diag2[i][0] < lenx and 0 <= y + diag2[i][1] < leny):
                return False
        
        str1 = charac[x + diag1[0][0]][y + diag1[0][1]] + charac[x][y] + charac[x + diag1[1][0]][y + diag1[1][1]]
        str2 = charac[x + diag2[0][0]][y + diag2[0][1]] + charac[x][y] + charac[x + diag2[1][0]][y + diag2[1][1]]
        
        valid_patterns = ["MAS", "SAM"]
        return (str1 in valid_patterns and str2 in valid_patterns)
    
    file = open("data_d4",'r')
    content = file.read()
    lines = content.split("\n")
    
    charac = [list(line) for line in lines]
    lenx = len(charac)
    leny = len(charac[0])
    total = 0
    for i in range(lenx):
        for j in range(leny):
            if charac[i][j] == "A":
                if search_mas(i,j,charac):
                    total += 1
    print(total)
    
part2()