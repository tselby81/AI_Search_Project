from collections import deque


# Using deque to implement some stack functionality
class Stack:
    def __init__(self):
        self.container = []
    def stack(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)


class DFS_search:
    def __init__(self, maze_file):
        self.start, self.goal, self.walls, self.width, self.height = self.read_maze(maze_file)
# Function to read the .txt file and check for wall, spaces, Goal, etc.
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
        print(maze)
        return start, goal, walls, width, height
    
    #  Function to get the children of the current node
    def get_children(self, child):
        row, col = child
        children = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]
        for x, y in children:
            if 0 <= x < self.height and 0 <= y < self.width and (x, y) not in self.walls:
                return x, y
        #return [(x, y) for x, y in children if 0 <= x < self.height and 0 <= y < self.width and (x, y) not in self.walls]

    
    def search(self):
        # Create a stack to store the nodes, then use those nodes to backtrack and find our path

        frontier = [(0, self.start, [])]
        explored = set()

        explored.add(self.start)        

        while frontier.__sizeof__() != 0:  #len(frontier) > 0:
            cost, node, solution = frontier.pop()
            for child in self.get_children(node):
                frontier.append((cost+1, child, solution+[node]))
                print()
                print(frontier)
                print()
            if node in explored:
                continue
            explored.add(node)
            if node == self.goal:
                return cost+1, solution+[node], len(explored), len(frontier)
        return None
    
#    print('Explored que is: ', explored)
    

        #     explored.add(pos)
        #     if pos == self.goal:
        #         return path + [pos], cost+1, len(explored), len(frontier)
        #     for child in self.get_children(pos):          #######    CALL THE get_children() FUNCTION AND PASS pos VALUE    #######
        #         frontier.push(child)
        # return None

DFS_search('smallMaze.txt').search()

"""       
DFS_search('smallMaze.txt').solve()
DFS_search('mediumMaze.txt').solve()
DFS_search('bigMaze.txt').solve()
DFS_search('openMaze.txt').solve()
"""

