global N
N = int(input("Enter number of queens :"))
Board = [['_' for x in range(N)] for y in range(N)]
print(Board)


def printBoard(Board):
    for i in Board:
        for j in i:
            print(j, end='')
        print(" ")


def isSafe(chessBoard, i, j):
    for row in range(len(chessBoard)):
        for element in range(len(chessBoard[row])):
            if chessBoard[row][element] == 'Q':
                jDist = abs(j - element)
                iDist = abs(i - row)
                if i == row or j == element or jDist == iDist:
                    return False
    return True


def SolveQueen(Board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(Board, i, col):
            Board[i][col] = 'Q'
            printBoard(Board)
            print(' ')
            if SolveQueen(Board, col + 1):
                return True
            Board[i][col] = '_'
            print('\nBacktraking here..')
    return False


if (SolveQueen(Board, 0)== False) :
    print('\nSolution not exist')
else:
    print('\nFinal solution')
    printBoard(Board)
