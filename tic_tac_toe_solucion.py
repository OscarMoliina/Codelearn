board = [['.' for i in range(3)] for j in range(3)]
player = 'O'
contador = 0

def draw_board(board):
    print(f'{board[0][0]} | {board[0][1]} | {board[0][2]}')
    for i in range(1,len(board)):
        print('---------')
        print(f'{board[i][0]} | {board[i][1]} | {board[i][2]}')

def poner_pieza(board,player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    fila = int(input(f'Jugador {player} - Selecciona la fila: '))
    columna = int(input(f'Jugador {player} - Selecciona la columna: '))
    i = True
    while i:
        if board[fila][columna] == '.':
            board[fila][columna] = player
            i = False
        else:
            fila = int(input(f'Jugador {player} - Selecciona la fila: '))
            columna = int(input(f'Jugador {player} - Selecciona la columna: '))  

def win_check(board,player):
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    for j in range(len(board)):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True
    
    return False

draw_board(board)
while not win_check(board, player) or contador == 9:
    poner_pieza(board, player)
    draw_board(board)
    contador += 1
if contador != 9:
    print(f'FIN! Enhorabuena Jugador {player}!')
else:
    print(f'FIN! Empate!')