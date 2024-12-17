def part1():
    builder =[]
    with open("data_d9",'r') as f:
        data = f.read()
        
    for i in range(0,10,2):
        builder.append(format(str(i//2)*int(data[i])+'.'*int(data[i+1])))
        
    print(builder)
        
part1()