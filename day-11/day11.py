grid = [[int(num) for num in row.strip()] for row in open("input.txt","r")]

flashes = 0
stack = []

def printGrid():
    for row in grid:
        print(row)
    print()

# Increases level of all octopi
def levelUp():
    global flashes
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1
            if (grid[i][j] > 9): 
                stack.append((i,j))
    # print("LEVEL UP:")
    # printGrid()

# Increases level of octopi adjacent given octopus
def levelAdj():
    global flashes
    while(len(stack) > 0):
        x,y = stack.pop()
        if(not grid[x][y] > 9): continue
        grid[x][y] = 0
        flashes += 1
        for i in range(-1,2):
            if(x+i < 0 or x+i >= len(grid)): continue
            for j in range(-1,2):
                if(y+j < 0 or y+j >= len(grid[0]) or (i==0 and j==0) or grid[x+i][y+j] == 0): continue
                grid[x+i][y+j] += 1
                if (grid[x+i][y+j] > 9): 
                    stack.append((x+i,y+j))
    # print("LEVEL ADJ:")
    # printGrid()

def checkSynchro():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] != 0): return False
    return True

steps = 0
while(not checkSynchro()):
    steps += 1
    levelUp()
    levelAdj()
print(flashes) # PART 1
print(steps) # PART 2