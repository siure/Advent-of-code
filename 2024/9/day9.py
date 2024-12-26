def part1():
    builder = []
    total = 0

    position = 0

    remPos = 0
    count = 0
    with open("2024/data_d9", "r") as f:
        data = f.read()

    r = len(data) // 2 + 1

    for i in range(0, len(data) - 1, 2):
        builder.append(
            f"{','.join([str(i // 2)]* int(data[i]))+','}{ '.' * int(data[i + 1])}"
        )
    builder.append(",".join([str(len(data) // 2)] * int(data[-1])) + ",")

    for i in range(0, len(builder)):
        if i == len(builder) - remPos:
            while count != 0:
                total += r * position
                position += 1
                count -= 1
            break

        s = builder[i].split(",")
        for j in range(len(s) - 1):
            total += position * int(s[j])
            position += 1
        remaining = len(s[-1])

        while remaining > 0:
            if i == len(builder) - remPos:
                break
            if count == 0:
                remPos += 1
                r -= 1
                count = len(builder[-remPos].split(",")[:-1])

            total += position * (r)

            position += 1
            remaining -= 1
            count -= 1

    print(total)


def part2():
    def parse_input(disk_map):
        return [(int(x), i % 2 == 0) for i, x in enumerate(disk_map)]

    def get_initial_state(segments):
        blocks = []
        file_id = 0
        for length, is_file in segments:
            if is_file:
                blocks.extend([file_id] * length)
                file_id += 1
            else:
                blocks.extend(['.'] * length)
        return blocks

    def find_gaps(blocks):
        """Find all gaps and their sizes."""
        gaps = []
        current_gap = 0
        start_pos = None
        
        for pos, block in enumerate(blocks + ['X']):  # Add sentinel
            if block == '.':
                if start_pos is None:
                    start_pos = pos
                current_gap += 1
            else:
                if current_gap > 0:
                    gaps.append((start_pos, current_gap))
                current_gap = 0
                start_pos = None
                
        return gaps

    def find_file_data(blocks):
        """Get all file positions and lengths."""
        files = []
        current_length = 0
        start_pos = None
        current_id = None
        
        for pos, block in enumerate(blocks + ['X']):  # Add sentinel
            if isinstance(block, int):
                if current_id is None:
                    current_id = block
                    start_pos = pos
                if block == current_id:
                    current_length += 1
                else:
                    files.append((current_id, start_pos, current_length))
                    current_id = block
                    start_pos = pos
                    current_length = 1
            else:
                if current_id is not None:
                    files.append((current_id, start_pos, current_length))
                    current_id = None
                    current_length = 0
        
        return sorted(files, reverse=True)  # Sort by ID descending

    def move_file(blocks, file_id, old_pos, length, new_pos):
        # Clear old position
        for i in range(old_pos, old_pos + length):
            blocks[i] = '.'
        
        # Place at new position
        for i in range(new_pos, new_pos + length):
            blocks[i] = file_id

    def solve_part2(disk_map):
        # Parse input and create initial state
        segments = parse_input(disk_map)
        blocks = get_initial_state(segments)
        
        # Process each file from highest ID to lowest
        files = find_file_data(blocks)
        
        for file_id, current_pos, length in files:
            # Find all gaps
            gaps = find_gaps(blocks)
            
            # Find leftmost gap that can fit this file and is to the left
            best_move = None
            for gap_start, gap_length in gaps:
                if gap_length >= length and gap_start < current_pos:
                    best_move = gap_start
                    break
            
            # Move file if we found a valid position
            if best_move is not None:
                move_file(blocks, file_id, current_pos, length, best_move)
        
        # Calculate checksum
        return sum(pos * block for pos, block in enumerate(blocks) if block != '.')

    with open("2024/data_d9",'r') as f:
        data= f.read()
    result = solve_part2(data)
    print("Checksum:", result)




part2()

#9903235278092

