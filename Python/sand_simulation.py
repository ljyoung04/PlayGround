import pygame
import sys
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CELL_SIZE = 40
Running = True
FPS = 10
SAND_COLOR = (158,103,32)
BLACK = (0,0,0)
WHITE = (255,255,255)


class Grid:
    
    def __init__(self):
        self.cols = int(SCREEN_WIDTH/CELL_SIZE)
        self.rows = int(SCREEN_HEIGHT/CELL_SIZE)
        self.Current_arr = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.Previous_arr = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def drawArr(self, window):
        for i in range(self.cols):
            for j in range(self.rows):
                pygame.draw.rect(window,WHITE, pygame.Rect(i*CELL_SIZE,j*CELL_SIZE,CELL_SIZE,CELL_SIZE),1)
                if self.Current_arr[i][j] == 1:
                    pygame.draw.rect(window,WHITE,pygame.Rect(i*CELL_SIZE,j*CELL_SIZE,CELL_SIZE,CELL_SIZE))
    
    def update_arr(self):
        self.Previous_arr = self.Current_arr
        self.Current_arr = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(self.cols):
            for j in range(self.rows - 1, -1, -1):
                if self.Previous_arr[i][j] == 1:
                    if j == self.rows - 1 or self.Previous_arr[i][j + 1] == 1:
                        self.Current_arr[i][j] = 1
                    else:
                        self.Current_arr[i][j + 1] = 1
                   
                   
        


window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Falling Sand Simulation")
clock = pygame.time.Clock()


grid = Grid()

grid.Current_arr[5][0] = 1 #test

while Running:
    window.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    grid.drawArr(window)
    grid.update_arr()

    clock.tick(FPS)
    pygame.display.update()