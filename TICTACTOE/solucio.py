b = [['.' for _ in range(3)] for _ in range(3)]

def drawBoard(board):
    for fila in board:
        print(' '.join(fila))

def askPosition(board):
    fila = int(input('Ingresa la fila: '))
    columna = int(input('Ingresa la columna: '))
    while board[fila][columna] != '.':
        print('Posició ocupada - Canvia de posició.')
        fila = int(input('Ingresa la fila: '))
        columna = int(input('Ingresa la columna: '))
    return fila, columna

def apply(fila, columna, board, jug):
    board[fila][columna] = jug
    return board

#Funció fullBoard fent-me el xulo
def fullBoard(board):
    return all([board[fila][col] != '.' for col in range(3) for fila in range(3)])

#Funció fullBoard normal
def fullBoardNormal(board):
    for fila in range(3):
        for columna in range(3):
            if board[fila][columna] == '.':
                return False
    return True

def isWinner(board, jug):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == jug:
            return True
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == jug:
            return True
    if board[0][0] == board[1][1] == board[2][2] == jug:
            return True
    if board[2][0] == board[1][1] == board[0][2] == jug:
            return True
    return False

def play(board):
    jug = 'X'
    board = board
    winner = False
    drawBoard(board=board)
    while not winner:
        fila, col = askPosition(board=board)
        apply(fila=fila, columna=col, board=board, jug=jug)
        if isWinner(board=board, jug=jug):
            winner = jug
            break
        if fullBoard(board):
            winner = 'Empate'
            break
        drawBoard(board=board)
        jug = 'X' if jug == 'O' else 'O'
    print('--- Tauler Final ---')
    drawBoard(board=board)
    print(f'Winner = {winner}')