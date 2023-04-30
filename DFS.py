
from input_maze_scrn import *

class DFS_search:
    def __init__(self, maze_file):
        self.start, self.goal, self.walls, self.width, self.height = self.read_maze(maze_file)


    """
    Function to read the .txt file and convert to 2D-list.
    Check for wall, start, spaces, and goal and assigns the index of the character accordingly
    """
    def read_maze(self, maze_file):
        with open(maze_file, 'r') as f:
            maze = [[char for char in line.strip()] for line in f]
        start = None
        goal = None
        walls = []
        for row in range(len(maze)):
            for col in range(len(maze[row])):
                # Create global values for the x and y values of start and goal to use as index in draw_solved_maze()
                if maze[row][col] == 'P':
                    global start_x
                    global start_y
                    start_x = row
                    start_y = col
                    start = (row, col)
                elif maze[row][col] == 'G':
                    global goal_x
                    global goal_y
                    goal_x = row
                    goal_y = col
                    goal = (row, col)
                elif maze[row][col] == '%':
                    walls.append((row, col))
        width = len(maze[0])
        height = len(maze)
        return start, goal, walls, width, height


    """
    Function to get the children of the current node
    Checks to make sure values are within the range of the 2D-list and not in walls[].
    """
    def get_children(self, child):
        row, col = child
        children = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]

        # LIST COMPREHENSION TO RETURN THE CHILD NODE VALUES
        return [(x, y) for x, y in children if 0 <= x < self.height and 0 <= y < self.width and (x, y) not in self.walls]

##########################      THE BELOW EXAMPLE IS A LONGER OPTION EQUIVILENT TO LIST COMPREHENSION       ##########################
        # new_child = []
        # for x, y in children:
        #   if 0 <= x < self.height and 0 <= y < self.width and (x, y) not in self.walls:
        #   newchild.append(x,y)
        # return new_child

    """
    Function which loops through the nodes in get_children().
    The frontier stack is for child nodes that are queued to be visited. Its initial value
        is set to the start value we found in read_maze().
    The Explored set is for nodes that we have visited already.
    After we visit a node, that node gets added to the explored set so we know where we
        have been and don't check it again.
    Then we check for child nodes and add those to frontier[], if there are none we go back
        to the previous node and check forchildren until we find unexplored nodes.
    """
    def search(self):
        # Create a stack to store the nodes, then use those nodes to backtrack and find our path
        # With python, we can use lists and sets as a sort of stack for this purpose

        frontier = [(0, self.start, [])]
        explored = set()

        while frontier.__sizeof__() != 0:
            cost, node, solution = frontier.pop()
            if node in explored:
                continue
            explored.add(node)
            if node == self.goal:
                return cost+1, solution+[node], len(explored), len(frontier)
            for child in self.get_children(node):
                frontier.append((cost+1, child, solution+[node]))
        return None


    """
    Funtion to report data for the solution path, cost of the solution, nodes expanded, and size of frontier queue.
    """
    def report(self):
        dfs_solution = self.search()

        print('The path taken to solve the maze was:')
        print('.'.join([str(pos) for pos in dfs_solution[1]]))
        print("The cost for this solution's path was: ")
        print(dfs_solution[0])
        print('The number of nodes expanded: ')
        print(dfs_solution[2])
        print('Maximum size of the frontier queue: ')
        print(dfs_solution[3]-1)


"""
Function to take the solved maze and make a new .txt file.
Nodes that make up the solution path are converted to the "." char in the 2D-list.
The function will loop over this new list and create a new .txt file which will display the solved maze.
"""
def draw_solved_maze(filename, new_filename, solved_maze):
        with open(filename, 'r') as f:
            file = f.read()
            maze = [list(line.strip()) for line in file.split('\n')]
        for i, j in solved_maze:
            if maze[i][j] == maze[start_x][start_y]:
                maze[i][j] = 'P'
            elif maze[i][j] == maze[goal_x][goal_y]:
                maze[i][j] = 'G'
            else:
                maze[i][j] ='.'
        new = open(new_filename, "x")
        for row in maze:
            new.write(''.join(row) + '\n')
        new.close()


# path[1] is the list of nodes we travel to get to the goal.
# This value is passed into the draw_solved_maze() as an argument and referenced within the function as the list variable maze[].

# path = DFS_search('smallMaze.txt').search()
# DFS_search('smallMaze.txt').report()
# draw_solved_maze('smallMaze.txt', 'solvedSmallMaze.txt', path[1])


# path = DFS_search('mediumMaze.txt').search()
# DFS_search('mediumMaze.txt').report()
# draw_solved_maze('mediumMaze.txt', 'solvedMediumMaze.txt', path[1])


# path = DFS_search('bigMaze.txt').search()
# DFS_search('bigMaze.txt').report()
# draw_solved_maze('bigMaze.txt', 'solvedBigMaze.txt', path[1])


# path = DFS_search('openMaze.txt').search()
# DFS_search('openMaze.txt').report()
# draw_solved_maze('openMaze.txt', 'solvedOpenMaze.txt', path[1])

