import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
TILE_SIZE = WIDTH // 4
FONT = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
num_tiles = 16


# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"{num_tiles-1} Puzzle")

# Function to create a shuffled board
def create_board():
    tiles=[]
    board = [list(range(num_tiles)),tiles_row_col(num_tiles,tiles)]
     
    random.shuffle(board[0])
    return board




# Function to draw the board
def draw_board(board):
    screen.fill(WHITE)
    for i in range(num_tiles):
        if board[0][i] != 0:
            tile = board[1][i]
            pygame.draw.rect(screen, BLACK, tile)
            text = FONT.render(str(board[0][i]), True, WHITE)
            text_rect = text.get_rect(center=tile.center)
            screen.blit(text, text_rect)
    '''
    for i in range(4):
        for j in range(4):
            tile = board[i * 4 + j]
            if tile != 0:
                pygame.draw.rect(screen, BLACK, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                text = FONT.render(str(tile), True, WHITE)
                text_rect = text.get_rect(center=(j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)
    '''
    pygame.display.flip()#update the display

# Function to find the empty tile
def find_empty(board):
    return board.index(0)

# Function to swap tiles
def swap_tiles(board, i, j):
    board[i], board[j] = board[j], board[i]

def tiles_row_col(tile_num,tiles):
    for i in range(tile_num):
        y=(i//4)*TILE_SIZE#row
        x=(i%4)*TILE_SIZE#column
        tile=pygame.Rect(x,y,TILE_SIZE,TILE_SIZE)
        tiles.append(tile)
    return tiles

def click_move(board,click_id):
    row_click=click_id//4
    col_click=click_id%4
    empty=find_empty(board)
    row0=empty//4
    col0=empty%4
    if row_click - 1 == row0 and col_click == col0:
        swap_tiles(board, click_id, empty)
    elif row_click + 1 == row0 and col_click == col0:
        swap_tiles(board, click_id, empty)
    elif col_click - 1 == col0 and row_click == row0:
        swap_tiles(board, click_id, empty)
    elif col_click + 1 == col0 and row_click == row0:
        swap_tiles(board, click_id, empty)



def check_complete(board):
    return (all(board[i]<board[i+1] for i in range(len(board)-2))) and board[-1]==0


# Function to move the tile
def move_tile(board, direction):
    empty = find_empty(board)
    
    if direction == "down" and empty < 12:
        swap_tiles(board, empty, empty + 4)
    elif direction == "up" and empty > 3:
        swap_tiles(board, empty, empty - 4)
    elif direction == "right" and empty % 4 < 3:
        swap_tiles(board, empty, empty + 1)
    elif direction == "left" and empty % 4 > 0:
        swap_tiles(board, empty, empty - 1)

# Main game loop
def main():
    board = create_board()
    print(board)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_tile(board[0], "up")
                elif event.key == pygame.K_DOWN:
                    move_tile(board[0], "down")
                elif event.key == pygame.K_LEFT:
                    move_tile(board[0], "left")
                elif event.key == pygame.K_RIGHT:
                    move_tile(board[0], "right")
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                for i in range(num_tiles):
                    if board[1][i].collidepoint(event.pos):
                        value=board[0][i]
                        id=board[0].index(value)
                        
                        click_move(board[0],id)

        if check_complete(board[0]):
            running = False               

        draw_board(board)
    pygame.quit()

if __name__ == "__main__":
    main()