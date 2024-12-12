def generate_operator_combinations(operators, length):
    if length == 0:
        yield [] 
    else:
        for operator in operators:
            for combination in generate_operator_combinations(operators, length - 1):
                yield [operator] + combination  

def eval_right_to_left(equation):
    total = equation[0]
    for i in range(1,len(equation),2):
        total = eval(f"{total} {equation[i]} {equation[i+1]}")
    return total

def part1():
    total = 0
    operator = ['+', '*']
    
    with open('data_d7') as f:
        for line in f:
            result, equation_str = line.strip(":").split(" ", 1)
            result = result[:-1]
            num = equation_str.split(" ")
            
            n = len(num) - 1 
            found = False
            
            for symbols in generate_operator_combinations(operator, n):
                equation = []
                for j in range(len(num) - 1):
                    equation.append(num[j])
                    equation.append(symbols[j])
                equation.append(num[-1])
                
                if eval_right_to_left(equation) == int(result): 
                    total += int(result)
                    found = True
                    break  
            
            if found:
                continue 
    print(total)

def eval_right_to_left_plus(equation):
    total = equation[0]
    for i in range(1,len(equation),2):
        if equation[i] == '||':
            total = int(f"{total}{equation[i+1]}")
        else:
            total = eval(f"{total} {equation[i]} {equation[i+1]}")
    return total

def part2():
    total = 0
    operator = ['+', '*','||']
    cpt = 0
    with open('data_d7') as f:
        for line in f:
            result, equation_str = line.strip(":").split(" ", 1)
            result = result[:-1]
            num = equation_str.split(" ")
            
            n = len(num) - 1 
            found = False
            cpt+=1 
            print(cpt)
            
            for symbols in generate_operator_combinations(operator, n):
                equation = []
                for j in range(len(num) - 1):
                    equation.append(num[j])
                    equation.append(symbols[j])
                equation.append(num[-1])
                
                if eval_right_to_left_plus(equation) == int(result): 
                    total += int(result)
                    found = True
                    break  
            
            if found:
                continue 
    print(total)
