# --- Day 5: Hydrothermal Venture ---
# You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

# An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

# So, the horizontal and vertical lines from the above list would produce the following diagram:

# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....
# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

data = [[tuple(map(int, first.split(','))),tuple(map(int, second.split(',')))] for line in open("test.txt","r") for [first, second] in [line.strip().rsplit(" -> ")]]

# Create 9x9 grid for storing overlapping point
grid = [[0 for x in range(990)] for y in range(990)]

# How to do this with list comprehesion? DONE
# data = [line.strip().rsplit(" -> ") for line in open("test.txt","r")]
# for vector in range(len(data)): 
#     for point in range(2):
#         data[vector][point] = tuple(map(int, data[vector][point].split(',')))

# Prints grid
def print_grid():
    for row in grid:
        view = ""
        for num in row:
            view += " ." if num==0 else " "+str(num)
        print(view)

# Adds points to grid from given vector/line, returns false if vector is diagonal, true otherwise
def add_points(vector):
    x1 = vector[0][0]
    y1 = vector[0][1]
    x2 = vector[1][0]
    y2 = vector[1][1]

    if not ((x1 == x2 or y1 == y2)):
        return True

    x_range = range(x1,x2+1) if x1<x2 else range(x2,x1+1)
    if (x1 == x2): x_range = range(0)

    y_range = range(y1,y2+1) if(y1<y2) else range(y2,y1+1)
    if(y1 == y2): y_range = range(0)

    for x in x_range:
        grid[y1][x] += 1
    for y in y_range:
        grid[y][x1] += 1
    return False
    
# Counts the "Dangerous parts"
def count_overlap():
    count = 0
    for row in grid:
        for col in row:
            if (col > 1): count +=1
    return count

# Part 1 answer:
def part_1():
    for vector in data:
        add_points(vector)
    print("Part 1 answer:",count_overlap())
part_1()


# --- Part Two ---
# Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

# Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

# An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# Considering all lines from the above example would now produce the following diagram:

# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....
# You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

# Consider all of the lines. At how many points do at least two lines overlap?

# Adds points to grid from given diagonal vector/line
def add_diagonal_points(vector):
    x1 = vector[0][0]
    y1 = vector[0][1]
    x2 = vector[1][0]
    y2 = vector[1][1]

    while(x1 != x2 and y1 != y2):
        grid[y1][x1] += 1
        x1 += 1 if x1<x2 else -1
        y1 += 1 if y1<y2 else -1
    grid[y2][x2] += 1

# Part 2 answer
def part_2():
    for vector in data:
        isDiagonal = add_points(vector) 
        if(isDiagonal): add_diagonal_points(vector)

    print("Part 2 answer:",count_overlap())
# part_2()