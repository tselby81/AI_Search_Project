
import pygame
from tkinter import *
from DFS import *

"""
Create the main game window
"""

GRID_SIZE = 30

MAZE = []

with open('solvedSmallMaze.txt', 'r') as f:
    maze = [[char for char in line.strip()] for line in f]
MAZE = maze

MAZE_HEIGHT = (len(maze)*GRID_SIZE)
MAZE_WIDTH = (len(maze[0])*GRID_SIZE)
            
WIN = pygame.display.set_mode((MAZE_WIDTH + (GRID_SIZE*2), MAZE_HEIGHT + (GRID_SIZE*2)))
pygame.display.set_caption("DFS Search")

GREY = (174, 179, 189)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (95, 180, 245)
RED = (255, 0, 0)

# Create objects to use to represent different parts of the maze
# def WALL():
#     pygame.draw.rect(WIN, BLACK, pygame.Rect((WIDTH/2)-60, (HEIGHT/2)-15, 30, 30))
# def START():
#     pygame.draw.rect(WIN, GREEN, pygame.Rect((WIDTH/2)-30, (HEIGHT/2)-15, 30, 30))
# def PATH():
#     pygame.draw.rect(WIN, LIGHT_BLUE, pygame.Rect((WIDTH/2), (HEIGHT/2)-15, 30, 30))
# def GOAL():
#     pygame.draw.rect(WIN, RED, pygame.Rect((WIDTH/2)+30, (HEIGHT/2)-15, 30, 30))

FPS = 0.5


def draw_grid(surface):
    for y in range(0, int(MAZE_HEIGHT + GRID_SIZE)):
        for x in range(0, int(MAZE_WIDTH + GRID_SIZE)):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, pygame.Color("lightslategrey"), r)
            else:
                r = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, pygame.Color("slategrey"), r)


def draw_window():
    WIN.fill("lightslategrey")

    draw_grid(WIN)



    with open('solvedSmallMaze.txt', 'r') as f:
            #file = f.read()
            #maze = [list(line.strip()) for line in file.split('\n')]
            maze = [[char for char in line.strip()] for line in f]
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 'P':
                maze[row][col] = pygame.draw.rect(WIN, GREEN, pygame.Rect((col*GRID_SIZE)+GRID_SIZE, (row*GRID_SIZE)+GRID_SIZE, GRID_SIZE, GRID_SIZE))

            elif maze[row][col] == 'G':
                maze[row][col] = pygame.draw.rect(WIN, RED, pygame.Rect((col*GRID_SIZE)+GRID_SIZE, (row*GRID_SIZE)+GRID_SIZE, GRID_SIZE, GRID_SIZE))

            elif maze[row][col] == '%':
                maze[row][col] = pygame.draw.rect(WIN, BLACK, pygame.Rect((col*GRID_SIZE)+GRID_SIZE, (row*GRID_SIZE)+GRID_SIZE, GRID_SIZE, GRID_SIZE))

            elif maze[row][col] == '.':
                maze[row][col] = pygame.draw.rect(WIN, LIGHT_BLUE, pygame.Rect((col*GRID_SIZE)+GRID_SIZE, (row*GRID_SIZE)+GRID_SIZE, GRID_SIZE, GRID_SIZE))

#Need to update the window to display what has been drawn in the loop
        pygame.display.update()


def choose_maze():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((MAZE_WIDTH + (GRID_SIZE*2), MAZE_HEIGHT + (GRID_SIZE*2)))
    pygame.display.set_caption("FILE SELECT")

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    font = pygame.font.SysFont('times', 30)
    font2 = pygame.font.SysFont('maiandragd', 18)
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False

        clock.tick(FPS)

        screen.blit(surface, (0, 0))
        screen.fill(GREY)
        pygame.display.flip()

        title = font.render("Please enter maze file name below", True, (0, 0, 0), None)
        titleRect = title.get_rect()
        titleRect.center = (MAZE_WIDTH / 2, 50)
        screen.blit(title, titleRect)

        subtitle = font2.render("INSERT TEXT BOX HERE", True, (0, 0, 0), None)
        subtitleRect = subtitle.get_rect()
        subtitleRect.center = (MAZE_WIDTH / 2, 90)
        screen.blit(subtitle, subtitleRect)

        pygame.display.update()
"""
Main Game Loop.
This should hold things related to game logic.
Other specialized functions should be written outside and called in the game loop when needed
"""
def main():

    # maze = open('solvedBigMaze.txt')
    # print(maze.read())

    # Clock item to control how many times we loop per second
    clock = pygame.time.Clock()


    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    choose_maze()
    main()