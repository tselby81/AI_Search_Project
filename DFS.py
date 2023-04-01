import time

start_time = time.time()

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
                    start = (row, col)
                elif maze[row][col] == 'G':
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
                print()
                print('GOALLLL!!!')
                print()
                return cost+1, solution+[node], len(explored), len(frontier)
            for child in self.get_children(node):
                frontier.append((cost+1, child, solution+[node]))
    
    def report(self):
        dfs_solution = self.search()
        print("The cost for this solution's path was ", dfs_solution[0])
        print()
        print('The number of nodes expanded: ', dfs_solution[2])
        print()
        print('Maximum size of the frontier queue: ', (dfs_solution[3]-1))
        print()

DFS_search('smallMaze.txt').report()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
DFS_search('smallMaze.txt').report()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
DFS_search('mediumMaze.txt').report()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
DFS_search('bigMaze.txt').report()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
DFS_search('openMaze.txt').report()

