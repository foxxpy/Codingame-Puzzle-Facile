import sys
import math

def instanciate_multi_line_grid(height, width):
    """Instanciate a list of lists"""
    grid = list()
    for i in range(height):
        line_list = list()
        for j in range(width):
            line_list.append(0)
        grid.append(line_list)
        
    return grid

def define_cycle(side, direction_pika):
    """Define the cycle of directions Pikachu must look at"""
    directions = ["<", "^", ">", "v"] if side=="L" else ["v", ">", "^", "<"]
    index_direction = directions.index(direction_pika)
    if index_direction > 0:
        directions = directions[index_direction-1:len(directions)]+directions[0:index_direction-1]
    else:
        directions = directions[3:]+directions[0:3]
    return directions
    

def move(grid, start_point, side, height, width):
    """Handle the moves of Pikachu through the maze"""
    i = start_point[0]
    j = start_point[1]
    direction_pika = start_point[2]
    
    directions = define_cycle(side, direction_pika)

    #For each direction Pikachu must look at
    for k in directions:
        #Left
        if k == "<" and j > 0 and (grid[i][j-1] == "0" or grid[i][j-1] in directions):
            start_point=(i, j-1, "<", True)
            break
        #Right
        if k == ">" and j < width-1 and (grid[i][j+1] == "0" or grid[i][j+1] in directions):
            start_point=(i, j+1, ">", True)
            break
            
        #Top
        if k == "^" and i > 0 and (grid[i-1][j] == "0" or grid[i-1][j] in directions):
            start_point=(i-1, j, "^", True)
            break

        #Bottom
        if k == "v" and i < height-1 and (grid[i+1][j] == "0" or grid[i+1][j] in directions):
            start_point=(i+1, j, "v", True)
            break
    
    return start_point    
    
#Variables instanciation
width, height = [int(i) for i in input().split()]
grid = list()
final_grid = instanciate_multi_line_grid(height, width) 
start_point = tuple() #(num_line, num_column, direction)
end_maze = False

#Instanciation of grid and filling final_grid with walls ("#")
for i in range(height):
    line = input()
    
    #We are looking for the start point and the direction Pikachu is looking at
    for direction in ["<", "^", ">","v"]:
        for j in range(len(line)):
            if direction == line[j]:
                start_point = (i, j, direction, False)
    grid.append(line)

    #We look for the walls and insert them in final_grid
    for j in range(len(line)):
        if line[j] == "#":
            final_grid[i][j] = "#"

side = input()

#Walking through the maze
while(end_maze == False):

    start_point = move(grid, start_point, side, height, width)
    i = start_point[0]
    j = start_point[1]

    if start_point[3] == True:
        final_grid[i][j] += 1

    if grid[i][j] in ["<", "^", ">", "v"]:
        end_maze = True

#We print our result
for i in range(height):
    for j in range(width):
        print(str(final_grid[i][j]), end="")
    print()