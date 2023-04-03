
class DFS_search:
    def __init__(self, maze_file):
        self.start, self.goal, self.walls, self.width, self.height = self.read_maze(maze_file)

    """
    Function to read the .txt file and check for wall, spaces, Goal, etc.
    """
    def read_maze(self, maze_file):
        with open(maze_file, 'r') as f:
            maze = [[char for char in line.strip()] for line in f]
        start = None
        goal = None
        walls = []
        for row in range(len(maze)):
            for col in range(len(maze[row])):
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
    """
    def get_children(self, child):
        row, col = child
        children = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]
        return [(x, y) for x, y in children if 0 <= x < self.height and 0 <= y < self.width and (x, y) not in self.walls]

##########################      \/THIS SYNTAXT\/  VS  /\ABOVE SYNTAX/\ ????       ##########################
        # for x, y in children:
        #   if 0 <= x < self.height and 0 <= y < self.width and (x, y) not in self.walls:
        # return x, y

    
    def search(self):
        # Create a stack to store the nodes, then use those nodes to backtrack and find our path

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
    
    def report(self):
        dfs_solution = self.search()
        report = [
        '\nThe path taken to solve the maze was:',
        '.'.join([str(pos) for pos in dfs_solution[1]]),
        "\nThe cost for this solution's path was: ", dfs_solution[0],
        '\nThe number of nodes expanded: ', dfs_solution[2],
        '\nMaximum size of the frontier queue: ', (dfs_solution[3]-1)
        ]
        return report


"""
Create a function to take the solved maze and make a new .txt file
Path taken to find the goal expressed as '.'
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
        new.write('\n'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'+'\n')
        for item in (DFS_search(filename).report()):
            new.write(str(item) + '\n')
        new.close()

"""
path[1] is the list of nodes we travel to get to the goal.
This value is passed into the draw_solved_maze() as an argument and referenced within the function as the list variable maze[].
"""

path = DFS_search('smallMaze.txt').search()
draw_solved_maze('smallMaze.txt', 'solvedSmallMaze.txt', path[1])


path = DFS_search('mediumMaze.txt').search()
draw_solved_maze('mediumMaze.txt', 'solvedMediumMaze.txt', path[1])


path = DFS_search('bigMaze.txt').search()
draw_solved_maze('bigMaze.txt', 'solvedBigMaze.txt', path[1])


path = DFS_search('openMaze.txt').search()
draw_solved_maze('openMaze.txt', 'solvedOpenMaze.txt', path[1])

