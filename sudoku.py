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
    def __init__(self, row, col, group, value, x, y, hover):
        self.row = row
        self.col = col
        self.group = group
        self.value = value
        self.x = x
        self.y = y
        self.hover = hover
    def create_rect(x, y):
        rect = pygame.Rect((x, y), (50, 50))
    def check_hover(rect, clicked):
        if pygame.mouse.get_pos() in rect:
            hover = True
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and hover == True:
                clicked = True
        if clicked == True:
            print("Clicked")






def check_neighbours():
    pass


def populate_grid():
    x = 0
    board_list = []


    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0<grid[i][j]<10):
                square_surface = pygame.Rect(((j+1)*50 - 12, (i+1)*50 - 25), (50, 50))
                num_surface = font.render(str(grid[i][j]), True, (163, 39, 98))
                window.blit(num_surface, ((j+1)*50 + 13, (i+1)*50))
                if i == 1 and j < 3:
                    board_list += value((i+1), (j+1), 1, grid[i][j], ((j+1)*50 - 12), ((i+1)*50 + 25), False)
                elif i == 1 and 2 < j < 6:
                    board_list += value((i+1), (j+1), 2, grid[i][j], ((j+1)*50 - 12), ((i+1)*50 + 25), False)
                elif i == 1 and 5 < j < 9:
                    board_list += value((i+1), (j+1), 3, grid[i][j], ((j+1)*50 - 12), ((i+1)*50 + 25), False)
                elif i == 2 and j < 3:
                    
                    board_list += value((i+1), (j+1), 4, grid[i][j], ((j+1)*50 - 12), ((i+1)*50 + 25), False)
                elif i == 2 and 2 < j < 6:
                    board_list += value((i+1), (j+1), 5, grid[i][j], ((j+1)*50 - 12), ((i+1)*50 + 25), False)
                elif i == 2 and 5 < j < 9:
                    board_list += value((i+1), (j+1), 6, grid[i][j], ((j+1)*50 - 12), ((i+1)*50 + 25), False)
                elif i == 3 and j < 3:
                    board_list += value((i+1), (j+1), 7, grid[i][j], ((j+1)*50 - 12), ((i+1)*50 + 25), False)
                elif i == 3 and 2 < j < 6:
                    board_list += value((i+1), (j+1), 8, grid[i][j], ((j+1)*50 - 12), ((i+1)*50 + 25), False)
                elif i == 3 and 5 < j < 9:
                    board_list += value((i+1), (j+1), 9, grid[i][j], ((j+1)*50 - 12), ((i+1)*50 + 25), False)



main()
