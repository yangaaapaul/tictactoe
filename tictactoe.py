import pygame as pg
import sys
WIN_SIZE = 600
xPic = pg.image.load('C:/Users/Paul/Downloads/Tic-tac-toe/X.png')
oPic = pg.image.load('C:/Users/Paul/Downloads/Tic-tac-toe/O.png')
scaledX = pg.transform.scale(xPic, (190,190))
scaledO = pg.transform.scale(oPic, (190,190))

pg.init()
screen = pg.display.set_mode([WIN_SIZE] *2)
#draws grid
pg.draw.line(screen, (85,85,85),(200,0), (200,600), 5)
pg.draw.line(screen, (85,85,85),(400,0), (400,600), 5)
pg.draw.line(screen, (85,85,85),(0,200), (600,200), 5)
pg.draw.line(screen, (85,85,85),(0,400), (600,400), 5)
board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

def drawBoard():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                screen.blit(scaledX, (i*200+5,j*200+5))
            if board[i][j] == 'O':
                screen.blit(scaledO, (i*200+5,j*200+5))


def full():
    for i in range(3):
        for j in range(3):
            if(board[i][j]==-1):
                return False
    return True
    
def writeText(message):
    font = pg.font.Font('freesansbold.ttf', 32)
    text = font.render(message, True, (255,255,255),(0,255,0))
    text_rect = text.get_rect(center = (WIN_SIZE//2,WIN_SIZE//2))
    screen.blit(text, text_rect)

def run():
    ind,flag = 0,True
    while True:
        pos = pg.mouse.get_pos()
        x,y = (pos[0]//200, pos[1]//200)
        player =['X','O']
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if board[x][y] != 'X' and board[x][y] != 'O' and flag:
                    board[x][y] = player[ind]
                    drawBoard()
                    if isWinner(player[ind]):
                        writeText(f'{player[ind]} wins!')
                        flag = False
                        
                    elif full():
                        writeText('Draw!')
                        flag = False
                    ind = (ind+1)%2
        pg.display.update()    


def mini_max(board, player):
    if isWinner('O'):
        return 1
    elif isWinner('X'):
        return -1
    elif full():
        return 0
    if player:
        max_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == -1:
                    board[i][j] = 'O'
                    curr_score = mini_max(board[i][j], False)
                    max_score = max(max_score,curr_score)
                    board[i][j] = -1
                    return max_score
    else:
        max_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == -1:
                    board[i][j] = 'X'
                    curr_score = mini_max(board[i][j], True)
                    min_score = min(max_score,curr_score)
                    board[i][j] = -1
                    return min_score

def isWinner(currPlayer):
    return ((board[0][0] == currPlayer and board[0][1] == currPlayer and board[0][2] == currPlayer) or
            (board[1][0] == currPlayer and board[1][1] == currPlayer and board[1][2] == currPlayer) or
            (board[2][0] == currPlayer and board[2][1] == currPlayer and board[2][2] == currPlayer) or
            (board[0][0] == currPlayer and board[1][0] == currPlayer and board[2][0] == currPlayer) or
            (board[0][1] == currPlayer and board[1][1] == currPlayer and board[2][1] == currPlayer) or
            (board[0][2] == currPlayer and board[1][2] == currPlayer and board[2][2] == currPlayer) or
            (board[0][0] == currPlayer and board[1][1] == currPlayer and board[2][2] == currPlayer) or
            (board[0][2] == currPlayer and board[1][1] == currPlayer and board[2][0] == currPlayer))
if __name__ == '__main__':
    run()
    
