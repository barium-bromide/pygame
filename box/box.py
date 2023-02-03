import pygame
import random

pygame.init()
WIDTH,HEIGHT = 500,550
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Cube")

BG_COLOUR = (68, 85, 90)
GRID_COLOUR = (186, 216, 224)
WHITE = (255,255,255)
DARKER_WHITE = (155,155,155)
BRIGHTER_BLACK = (20,20,20)
BLACK = (0,0,0)
GREEN = (0,128,0)
DARKER_GREEN = (0,28,0)
RED = (255,0,0)
DARKER_RED = (155,0,0)

FONT = pygame.font.SysFont("ComicSans", 26)
LEFT_JUSTIFY = 75
UP_JUSTIFY = 100
CELLSIZE = 60
FPS = 60

LEVEL1 = [[1,0,0,0,0,],
         [0,9,9,9,0],
         [0,9,9,9,0],
         [0,9,9,9,0],
         [0,0,0,0,2],]
LEVEL2 = [[1,0,0,0,0],
         [0,0,3,0,0],
         [0,0,3,0,0],
         [0,0,3,0,0],
         [0,0,0,0,2]]
LEVEL3 = [[1,0,3,3,3],
         [3,0,0,3,3],
         [3,3,0,0,3],
         [3,3,3,0,0],
         [3,3,3,3,2]]
LEVEL4 = [[1,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]

grid = [row.copy() for row in LEVEL1]
level = 1
content = ["Move with wasd and go on the green box","Avoid the red box","","This is the end"]

def draw_grid():
    for y,row in enumerate(grid):
        for x,cell in enumerate(row):
            if cell == 0:
                pygame.draw.rect(WIN,DARKER_WHITE,[LEFT_JUSTIFY + x * CELLSIZE * 1.125,(UP_JUSTIFY + y * CELLSIZE * 1.125) + 10,CELLSIZE,CELLSIZE],border_radius=5)
                pygame.draw.rect(WIN,WHITE,[LEFT_JUSTIFY + x * CELLSIZE * 1.125,UP_JUSTIFY + y * CELLSIZE * 1.125,CELLSIZE,CELLSIZE],border_radius=5)
            elif cell == 1:
                pygame.draw.rect(WIN,DARKER_WHITE,[LEFT_JUSTIFY + x * CELLSIZE * 1.125,(UP_JUSTIFY + y * CELLSIZE * 1.125) + 10,CELLSIZE,CELLSIZE],border_radius=5)
                pygame.draw.rect(WIN,WHITE,[LEFT_JUSTIFY + x * CELLSIZE * 1.125,UP_JUSTIFY + y * CELLSIZE * 1.125,CELLSIZE,CELLSIZE],border_radius=5)
                pygame.draw.rect(WIN,BLACK,[LEFT_JUSTIFY + x * CELLSIZE * 1.125 + 15,(UP_JUSTIFY + y * CELLSIZE * 1.125) + 20,CELLSIZE/2,CELLSIZE/2],border_radius=5)
                pygame.draw.rect(WIN,BRIGHTER_BLACK,[LEFT_JUSTIFY + x * CELLSIZE * 1.125 + 15,(UP_JUSTIFY + y * CELLSIZE * 1.125) + 10,CELLSIZE/2,CELLSIZE/2],border_radius=5)
            elif cell == 2:
                pygame.draw.rect(WIN,DARKER_GREEN,[LEFT_JUSTIFY + x * CELLSIZE * 1.125,(UP_JUSTIFY + y * CELLSIZE * 1.125) + 10,CELLSIZE,CELLSIZE],border_radius=5)
                pygame.draw.rect(WIN,GREEN,[LEFT_JUSTIFY + x * CELLSIZE * 1.125,UP_JUSTIFY + y * CELLSIZE * 1.125,CELLSIZE,CELLSIZE],border_radius=5)
            elif cell == 3:
                pygame.draw.rect(WIN,DARKER_RED,[LEFT_JUSTIFY + x * CELLSIZE * 1.125,(UP_JUSTIFY + y * CELLSIZE * 1.125) + 10,CELLSIZE,CELLSIZE],border_radius=5)
                pygame.draw.rect(WIN,RED,[LEFT_JUSTIFY + x * CELLSIZE * 1.125,UP_JUSTIFY + y * CELLSIZE * 1.125,CELLSIZE,CELLSIZE],border_radius=5)

def pass_goal():
    global grid,level
    grid = [row.copy() for row in [LEVEL2, LEVEL3, LEVEL4][level-1]]
    level += 1
    
def reset():
    global grid
    grid = [row.copy() for row in [LEVEL1, LEVEL2, LEVEL3, LEVEL4][level-1]]

def draw_text():
    text = FONT.render(content[level-1], True, BLACK)
    WIN.blit(text, [(500 - len(content[level-1]) * 13)/2,20])

def draw_window():
    WIN.fill(BG_COLOUR)
    draw_grid()
    draw_text()
    pygame.display.update()

def handle_keys(keys_pressed):
    if keys_pressed[pygame.K_d]:
        for y,row in enumerate(grid):
            for x,cell in enumerate(row):
                if cell == 1:
                    if x + 1 > (len(row) - 1):
                        break

                    elif grid[y][x] == 9 or grid[y][x + 1] == 9:
                        break

                    else:
                        if grid[y][x] == 2 or grid[y][x + 1] == 2:
                            print("Goal")
                            pass_goal()
                            break

                        elif grid[y][x] == 3 or grid[y][x + 1] == 3:
                            print("Restart")
                            reset()
                            break

                        grid[y][x],grid[y][x + 1] = grid[y][x + 1],grid[y][x]
                    break
        pygame.time.delay(150)
    if keys_pressed[pygame.K_a]:
        for y,row in enumerate(grid):
            for x,cell in enumerate(row):
                if cell == 1:
                    if x - 1 < 0:
                        break

                    elif grid[y][x] == 9 or grid[y][x - 1] == 9:
                        break

                    else:
                        if grid[y][x] == 2 or grid[y][x - 1] == 2:
                            print("Goal")
                            pass_goal()
                            break

                        elif grid[y][x] == 3 or grid[y][x - 1] == 3:
                            print("Restart")
                            reset()
                            break

                        grid[y][x],grid[y][x - 1] = grid[y][x - 1],grid[y][x]
                    break
        pygame.time.delay(150)
    if keys_pressed[pygame.K_s]:
        for y,row in enumerate(grid):
            for x,cell in enumerate(row):
                if cell == 1:
                    if y + 1 > (len(grid) - 1):
                        break

                    elif grid[y][x] == 9 or grid[y + 1][x] == 9:
                        break

                    else:
                        if grid[y][x] == 2 or grid[y + 1][x] == 2:
                            print("Goal")
                            pass_goal()
                            break

                        elif grid[y][x] == 3 or grid[y + 1][x] == 3:
                            print("Restart")
                            reset()
                            break

                        grid[y + 1][x],grid[y][x] = grid[y][x],grid[y + 1][x]
                    break
            else:
                continue
            break
        pygame.time.delay(150)
    if keys_pressed[pygame.K_w]:
        for y,row in enumerate(grid):
            for x,cell in enumerate(row):
                if cell == 1:
                    if y - 1 < 0:
                        break

                    elif grid[y][x] == 9 or grid[y - 1][x] == 9:
                        break

                    else:
                        if grid[y][x] == 2 or grid[y - 1][x] == 2:
                            print("Goal")
                            pass_goal()
                            break

                        elif grid[y][x] == 3 or grid[y - 1][x] == 3:
                            print("Restart")
                            reset()
                            break

                        grid[y - 1][x],grid[y][x] = grid[y][x],grid[y - 1][x]
                    break
        pygame.time.delay(150)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key_pressed = pygame.key.get_pressed()
        handle_keys(key_pressed)
        draw_window()
    pygame.quit

if __name__ == "__main__":
    main()