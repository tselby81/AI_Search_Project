
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

########################################################################################################
                    # Figure out MAZE_HEIGHT, MAZE_WIDTH
########################################################################################################

MAZE_HEIGHT = (len(maze)*GRID_SIZE)
MAZE_WIDTH = (len(maze[0])*GRID_SIZE)
# CENTER = (MAZE_HEIGHT/2, MAZE_WIDTH/2)
            
WIN = pygame.display.set_mode((MAZE_WIDTH + (GRID_SIZE*4), MAZE_HEIGHT + (GRID_SIZE*4)))
pygame.display.set_caption("DFS Search")


GREY = (174, 179, 189)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (95, 180, 245)
RED = (255, 0, 0)

LIGHT_PURPLE = (159, 121, 238)
DARK_PURPLE = (93, 71, 139)

FPS = 30


def draw_grid(surface):
    for y in range(0, int(MAZE_HEIGHT + GRID_SIZE*4)):
        for x in range(0, int(MAZE_WIDTH + GRID_SIZE*4)):
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
            maze = [[char for char in line.strip()] for line in f]
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == '%':
                maze[row][col] = pygame.draw.rect(WIN, BLACK, pygame.Rect((col*GRID_SIZE)+(GRID_SIZE*2), (row*GRID_SIZE)+(GRID_SIZE*2), GRID_SIZE, GRID_SIZE))

            elif maze[row][col] == 'P':
                maze[row][col] = pygame.draw.rect(WIN, GREEN, pygame.Rect((col*GRID_SIZE)+(GRID_SIZE*2), (row*GRID_SIZE)+(GRID_SIZE*2), GRID_SIZE, GRID_SIZE))

            elif maze[row][col] == '.':
                maze[row][col] = pygame.draw.rect(WIN, LIGHT_BLUE, pygame.Rect((col*GRID_SIZE)+(GRID_SIZE*2), (row*GRID_SIZE)+(GRID_SIZE*2), GRID_SIZE, GRID_SIZE))

            elif maze[row][col] == 'G':
                maze[row][col] = pygame.draw.rect(WIN, RED, pygame.Rect((col*GRID_SIZE)+(GRID_SIZE*2), (row*GRID_SIZE)+(GRID_SIZE*2), GRID_SIZE, GRID_SIZE))


#Need to update the window to display what has been drawn in the loop
        pygame.display.update()


def choose_maze():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((MAZE_WIDTH + (GRID_SIZE*4), MAZE_HEIGHT + (GRID_SIZE*4)))
    pygame.display.set_caption("FILE SELECT")

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    font = pygame.font.SysFont('times', 30)
    font2 = pygame.font.SysFont('maiandragd', 18)

    input = pygame.Rect(200, 100, 300, 30)
    input.center = ((MAZE_WIDTH + (GRID_SIZE*4)) / 2, 190)

    user_text = ""
    
    intro = True
    active = False

    while intro:
        if active:
            color = LIGHT_PURPLE
        else:
            color = DARK_PURPLE
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
                    return user_text
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            elif event.type == pygame.QUIT:
                intro = False

        clock.tick(FPS)

        screen.blit(surface, (0, 0))
        screen.fill("lightslategrey")
        pygame.display.flip()

        title = font.render("PLEASE ENTER MAZE FILE NAME BELOW.", True, (0, 0, 0), None)
        titleRect = title.get_rect()
        titleRect.center = ((MAZE_WIDTH + (GRID_SIZE*4)) / 2, 125)
        screen.blit(title, titleRect)

        example = font.render("(sampleFile.txt).", True, (0, 0, 0), None)
        exampleRect = example.get_rect()
        exampleRect.center = ((MAZE_WIDTH + (GRID_SIZE*4)) / 2, 155)
        screen.blit(example, exampleRect)


        pygame.draw.rect(screen, color, input)
        text_surface = font2.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input.x+5, input.y+5))
        pygame.draw.rect(screen, BLACK, (input), 2)

        subtitle = font.render("PRESS ENTER WHEN FINISHED.", True, (0, 0, 0), None)
        subtitleRect = subtitle.get_rect()
        subtitleRect.center = ((MAZE_WIDTH + (GRID_SIZE*4)) / 2, 230)
        screen.blit(subtitle, subtitleRect)

        pygame.display.update()
    return user_text
"""
Main Game Loop.
This should hold things related to game logic.
Other specialized functions should be written outside and called in the game loop when needed
"""
def main():

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
    print(choose_maze())
    main()