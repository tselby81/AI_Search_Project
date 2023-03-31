import sys
from enum import Enum
from collections import namedtuple
# Read in the .txt files containing the Mazes

# Find start location

# Create function to identify the characters: Empty space(empty string), wall(%), goal(G), start(P)
        # Identify spaces that we already visit with the character we use to mark them

# Create function to visit each empty space and mark the space as we go

# Create a function that make a tree - create a list for children(not explored) and a list for parent nodes(explored)
        # Each space we visit gets added as a node to the tree

# Print the solution path and its cost (each step = 1)
# Print number of nodes expanded
# Print maximum depth searched
# Print maximum size of fringe

maze_arr = []

# frontier = []
# explored = []

# start = 0

# Read a given maze .txt file and turn it into a 2d array
with open('smallMaze.txt', 'r') as f:
    maze = f.read()
maze_arr = [list(line.strip()) for line in maze.split('\n')]

class Cell(str, Enum):
    SPACE = " "
    WALL = "%"
    START = "P"
    GOAL = "G"
    PATH = "."


# class DFS_search:

    def search(self):
        self.print_maze()
        self.find_start()
        ###############      RETURN A VALUE TO USE AS THE NODE VALUE     ###############
        self.build_tree()

    # Function to print the maze in a way we can understand
    def print_maze(self):
        for row in maze_arr:
            print(''.join(row))

    # Find the starting location and set that as your first node
    def find_start(self):
        for row in maze_arr:
            for char in row:
                if char == 'P':
                    global start 
                    start= char
                    print()
                    print("The starting location for the search is position ", char)
                    return True
        return False
    
    # Use the starting node and frontier stacks to build a tree to be explored
    def build_tree(self):
        pass

    # Function to mark nodes we have already been to -- .append to explored[] and .pop from frontier[]
    def mark(self):
        pass

    # Check current node to see if we reached the goal -- if not continue looping
    def check_goal(self):
        if maze_arr.index('G'):
            return True
        return False
    
    # Work backwards from the goal to track our path -- replace with '.' to show path we took
    def path(self):
        pass

# print("print maze_arr")
# print()
# print(maze_arr)
# print()


############################################################################################################################



