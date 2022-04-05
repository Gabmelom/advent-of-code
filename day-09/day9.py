# --- Day 9: Smoke Basin ---
# These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

# If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

# Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

# In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

# The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

# Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

from collections import deque
import functools

grid = [[int(num) for num in row.strip()] for row in open("input.txt","r")]

# Iterates over grid to find lowpoints
def findLowPoints(grid):
    points = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            value = grid[x][y]
            if(x-1 >= 0): 
                up = grid[x-1][y]
                if (up <= value): continue
            if(x+1 < len(grid)):
                down = grid[x+1][y]
                if (down <= value): continue
            if(y-1 >= 0): 
                left = grid[x][y-1]
                if (left <= value): continue
            if(y+1 < len(grid[x])): 
                right = grid[x][y+1]
                if (right <= value): continue
            points.append((x,y))
    return points        

# Returns the risk level of an array of points
def totalRisk(points,grid):
    total = 0
    for point in points:
        x,y = point
        total += 1 + grid[x][y]
    return total

# Returns array of adjacent coordinates
def adjacentPoints(point, maxHeight,maxWidth):
    adjacentPoints = []
    x,y = point
    if(x-1 >= 0): adjacentPoints.append((x-1,y))
    if(x+1 < maxHeight):adjacentPoints.append((x+1,y))
    if(y-1 >= 0): adjacentPoints.append((x,y-1))
    if(y+1 < maxWidth): adjacentPoints.append((x,y+1))
    return adjacentPoints

low_points = findLowPoints(grid)
# print(totalRisk(low_points,grid)) # PART 1

basins = []
queued = [[None for x in range(len(grid[0]))] for y in range(len(grid))]

# Breadth-first search from low points to find basins
for point in low_points:
    basin = set()
    q = deque()

    q.append(point)
    queued[point[0]][point[1]] = True

    while(len(q) != 0):
        nextPoint = q.popleft()
        basin.add(nextPoint)
        neighbours = adjacentPoints(nextPoint,len(grid),len(grid[0]))
        for p in neighbours:
            if (grid[p[0]][p[1]] != 9 and not queued[p[0]][p[1]]):
                basin.add(p)
                q.append(p)
                queued[p[0]][p[1]] = True
    basins.append(len(basin))

basins.sort(reverse=True)
while(len(basins)!=3): basins.pop()
print(functools.reduce(lambda a,b: a*b, basins))