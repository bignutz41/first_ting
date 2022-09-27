import pygame
import requests

width = 550
background_colour = (255, 255, 255)
bold_border_list = [0, 3, 6, 9]
difficulty = "easy"
pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 35)

response = requests.get(f"https://sugoku.herokuapp.com/board?difficulty={difficulty}")
grid = response.json()['board']

print(grid)

pygame.init()
window = pygame.display.set_mode((width, width))
pygame.display.set_caption("Sudoku")
window.fill(background_colour)

def main():
    for i in range(0,10):
        if i in bold_border_list:
            pygame.draw.line(window, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 2)
            pygame.draw.line(window, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2)
        else:
            pygame.draw.line(window, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 1)
            pygame.draw.line(window, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 1)
    pygame.display.update()

    populate_grid()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                return

class value:
    def __init__(self, row, col, group):
        self.row = row
        self.col = col
        self.group = group




def populate_grid():
    x = 0


    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0<grid[i][j]<10):
                num_surface = font.render(str(grid[i][j]), True, (163, 39, 98))
                window.blit(num_surface, ((j+1)*50 + 13, (i+1)*50))
                value = value(i+1, j+1)




main()
