
import pygame
# from DFS import DFS_search

"""
Create the main game window
"""
# Dimentions for the main window
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DFS Search")

LIGHT_PURPLE = (165, 134, 219)
BLACK = (0, 0, 0)
FPS = 30


def draw_window():
    WIN.fill(LIGHT_PURPLE)
    pygame.draw.rect(WIN, BLACK, pygame.Rect((WIDTH/2), (HEIGHT/2), 30, 30))

    #Need to update the window to display what has been drawn in the loop
    pygame.display.update()


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
    main()