def parse_input(input_lines):
    # Parses the input into a list of line segments as tuples of (x1, y1, x2, y2)
    lines = []
    for line in input_lines:
        # Split by ' -> ' to get the two endpoints
        start, end = line.split(' -> ')
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        lines.append((x1, y1, x2, y2))
    return lines

def count_overlaps(lines):
    # Dictionary to count the number of times each point is covered by a line
    covered_points = {}
    
    for x1, y1, x2, y2 in lines:
        # Only consider horizontal and vertical lines
        if x1 == x2:  # Vertical line
            for y in range(min(y1, y2), max(y1, y2) + 1):
                covered_points[(x1, y)] = covered_points.get((x1, y), 0) + 1
        elif y1 == y2:  # Horizontal line
            for x in range(min(x1, x2), max(x1, x2) + 1):
                covered_points[(x, y1)] = covered_points.get((x, y1), 0) + 1
    
    # Count points where at least two lines overlap
    overlap_count = sum(1 for count in covered_points.values() if count >= 2)
    
    return overlap_count

# # Example input from the problem statement
# input_lines = [
#     "0,9 -> 5,9",
#     "8,0 -> 0,8",
#     "9,4 -> 3,4",
#     "2,2 -> 2,1",
#     "7,0 -> 7,4",
#     "6,4 -> 2,0",
#     "0,9 -> 2,9",
#     "3,4 -> 1,4",
#     "0,0 -> 8,8",
#     "5,5 -> 8,2"
# ]

# Read the input from input.txt
with open('input.txt', 'r') as file:
    input_lines = file.read().strip().splitlines()

# Parse the input
lines = parse_input(input_lines)

# Count overlaps
result = count_overlaps(lines)

# Output the result
print(result)
