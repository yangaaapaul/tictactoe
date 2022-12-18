import pygame as pg
import sys
WIN_SIZE = 600
xPic = pg.image.load('C:/Users/Paul/Downloads/Tic-tac-toe/X.png')
oPic = pg.image.load('C:/Users/Paul/Downloads/Tic-tac-toe/O.png')
scaledX = pg.transform.scale(xPic, (200,200))
scaledO = pg.transform.scale(oPic, (200,200))
pg.init()
screen = pg.display.set_mode([WIN_SIZE] *2)
board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
def drawBoard():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                screen.blit(scaledX, (i*200,j*200))
            if board[i][j] == 'O':
                screen.blit(scaledO, (i*200,j*200))
    pg.draw.line(screen, (85,85,85),(200,0), (200,600), 10)
    pg.draw.line(screen, (85,85,85),(400,0), (400,600), 10)
    pg.draw.line(screen, (85,85,85),(0,200), (600,200), 10)
    pg.draw.line(screen, (85,85,85),(0,400), (600,400), 10)
    pg.display.update()

def full():
    for i in range(3):
        for j in range(3):
            if(board[i][j]==-1):
                return False
    return True
    

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
                    if isWinner(player[ind]):
                        print(f'{player[ind]} wins')
                        flag = False
                    ind = (ind+1)%2
                
        
        drawBoard()

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
