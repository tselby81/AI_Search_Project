
import pygame
from DFS_Animation import *

# def choose_maze():
#     pygame.init()

#     clock = pygame.time.Clock()
#     screen = pygame.display.set_mode((MAZE_WIDTH + (GRID_SIZE*4), MAZE_HEIGHT + (GRID_SIZE*4)))
#     pygame.display.set_caption("FILE SELECT")

#     surface = pygame.Surface(screen.get_size())
#     surface = surface.convert()

#     font = pygame.font.SysFont('times', 30)
#     font2 = pygame.font.SysFont('maiandragd', 18)

#     input = pygame.Rect(200, 100, 300, 30)
#     input.center = ((MAZE_WIDTH + (GRID_SIZE*4)) / 2, 190)

#     user_text = ""
    
#     intro = True
#     active = False

#     while intro:
#         if active:
#             color = LIGHT_PURPLE
#         else:
#             color = DARK_PURPLE
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if input.collidepoint(event.pos):
#                     active = True
#                 else:
#                     active = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     intro = False
#                     return user_text
#                 if event.key == pygame.K_BACKSPACE:
#                     # get text input from 0 to -1 i.e. end.
#                     user_text = user_text[:-1]
#                 else:
#                     user_text += event.unicode
#             elif event.type == pygame.QUIT:
#                 intro = False

#         clock.tick(FPS)

#         screen.blit(surface, (0, 0))
#         screen.fill("lightslategrey")
#         pygame.display.flip()

#         title = font.render("PLEASE ENTER MAZE FILE NAME BELOW.", True, (0, 0, 0), None)
#         titleRect = title.get_rect()
#         titleRect.center = ((MAZE_WIDTH + (GRID_SIZE*4)) / 2, 125)
#         screen.blit(title, titleRect)

#         example = font.render("(sampleFile.txt).", True, (0, 0, 0), None)
#         exampleRect = example.get_rect()
#         exampleRect.center = ((MAZE_WIDTH + (GRID_SIZE*4)) / 2, 155)
#         screen.blit(example, exampleRect)


#         pygame.draw.rect(screen, color, input)
#         text_surface = font2.render(user_text, True, (255, 255, 255))
#         screen.blit(text_surface, (input.x+5, input.y+5))
#         pygame.draw.rect(screen, BLACK, (input), 2)

#         subtitle = font.render("PRESS ENTER WHEN FINISHED.", True, (0, 0, 0), None)
#         subtitleRect = subtitle.get_rect()
#         subtitleRect.center = ((MAZE_WIDTH + (GRID_SIZE*4)) / 2, 230)
#         screen.blit(subtitle, subtitleRect)

#         pygame.display.update()
#     return user_text