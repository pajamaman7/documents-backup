import pygame
import random

##Shapes and globals

pygame.font.init()

s_height = 700
s_width = 800
play_height = 600
play_width = 300

board_height = 20
board_width = 10

"""
Shapes are represented with their letters, in order:
    S,Z,I,O,J,L,T
    and colors, in order:
    green, red, light blue,yellow, blue, orange, purple
"""

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shape_list = [S,Z,I,O,J,L,T]
color_list = ["red","green,","light blue","yellow","blue","orange","purple"]

class Piece(object):
    rows = 20
    columns = 10
    def __init__(self,column,row,shape):
        self.column=column
        self.row=row
        self.shape=shape
        self.color=color_list[piece_list.index(shape)]
        self.rotation=0

def create_grid(locked_positions={}):
    grid=[[(0,0,0) for i in range(0,board_width)]for j in range(0,board_height)]
    for i in range(0,board_width):
        for j in range(0,board_height):
            if (i,j) in locked_positions:
                grid[i][j]=locked_positions[(i,j)]
    return grid

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    global shape_list, color_list
    return Piece(board_width/2,0,random.choice(shape_list))

def draw_text_middle(text, size, color, surface):  
    pass
   
def draw_grid(surface, row, col):
    surface.fill((0,0,0))
    # Tetris Title
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', 1, (255,255,255))
 
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)
 
    # draw grid and border
    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)
    pygame.display.update()

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface):

def main():
    pass

def main_menu():
    pass


main_menu()  # start game
