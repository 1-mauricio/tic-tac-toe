import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH =  15
BOARD_ROWS = 3
BOARD_COLS = 3

RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23,145, 135)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

# board
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
#print(board)

#pygame.draw.line(screen, RED, (10, 10), (300, 300), 10)

def draw_lines():
    # horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0,200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0,400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200,0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400,0), (400, 600), LINE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True

#false
print(is_board_full())
#marking all squares
for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            mark_square(row, col, 1)
#board is full
print(is_board_full())


draw_lines()
# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()