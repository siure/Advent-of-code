from collections import defaultdict

def is_valid_order(pages, rules):
    for i in range(len(pages)):
        for j in range(i+1, len(pages)):
            if  pages[i] in rules[pages[j]]:
                return False
    return True

def shift_list(lst, j,i):
    item = lst.pop(j)
    lst.insert(i, item)
    return lst

def part1():
    rules = defaultdict(list)
    total = 0

    with open("data_d5", 'r') as f:
        lines = f.readlines()
        
        # Parse rules first
        rule_lines = []
        for line in lines:
            if line.strip() == "":
                break
            page1, page2 = maps(int, line.strip().split("|"))
            rules[page1].append(page2)
            rule_lines.append(line.strip())

        # Process updates starting after the blank line
        update_lines = lines[len(rule_lines)+1:]
        
        for line in update_lines:
            line = line.strip()
            if line:
                pages = list(maps(int, line.split(",")))
                
                # Check if the current order is valid
                if is_valid_order(pages, rules):
                    middle_index = len(pages) // 2
                    total += pages[middle_index]
                    print(f"Valid update: {pages}, Middle page: {pages[middle_index]}")

    print("Total:", total)


def part2():
    rules = defaultdict(list)
    total = 0

    with open("data_d5", 'r') as f:
        lines = f.readlines()
        rule_lines = []    
        for line in lines:
            if line.strip() == "":
                break
            page1, page2 = maps(int, line.strip().split("|"))
            rules[page1].append(page2)
            rule_lines.append(line.strip())

        update_lines = lines[len(rule_lines)+1:]
        
        for line in update_lines:
            line = line.strip()
            if line:
                pages = list(maps(int, line.split(",")))
                
                if not is_valid_order(pages, rules):
                    print(pages)
                    for i in range(len(pages)):
                        for j in range(i):
                            print(pages[i]," + " , pages[j]," = ",rules[pages[i]], " ", pages)
                            if pages[j] in rules[pages[i]]:
                                shift_list(pages,i,j)
                    total += pages[len(pages)//2]
    print(total)
    
part2()