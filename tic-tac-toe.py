boardState = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
isRunning = True
playerInput = ['','']
playerInputValid = False
playerTurn = 1
def validateInput(input):
    if(input[0] == "1" or input[0] == "2" or input[0] == "3" and input[1] == "1" or input[1] == "2" or input[1] == "3"):
        return True
    else:
        return False
def parseInput(input):
    playerPlay = [0,0]
    playerPlay[0] = int(input[0]) - 1
    playerPlay[1] = int(input[1]) - 1
    return playerPlay

def validateLocation(playlocation):
    if(boardState[playlocation[0]][playlocation[1]] == " "):
        return True;
    else:
        return False;

def play(location, letter):
    boardState [location[0]] [location[1]] = letter

def checkWin():
    for i in range(0, len(boardState)-1):
        if(boardState[i][0] != ' ' and boardState[i][0] == boardState[i][1] and boardState[i][0] == boardState[i][2]):
            return True
    for i in range(0, len(boardState[0])-1):
        if(boardState[0][i] != ' ' and boardState[0][i] == boardState[1][i] and boardState[0][i] == boardState[2][i]):
            return True
    if(boardState[0][0] != ' ' and boardState[0][0] == boardState[1][1] and boardState[0][0] == boardState[2][2] or boardState[0][2] != ' ' and boardState[0][2] == boardState[1][1] and boardState[2][0] == boardState[0][2]):
        return True
    return False

def printBoard():
    print(boardState[0][0] + '|' + boardState[1][0] + '|' + boardState[2][0])
    print('-+-+-')
    print(boardState[0][1] + '|' + boardState[1][1] + '|' + boardState[2][1])
    print('-+-+-')
    print(boardState[0][2] + '|' + boardState[1][2] + '|' + boardState[2][2])

def checkFull():
    for i in range(0, len(boardState)-1):
        for j in range(0, len(boardState[0])-1):
            if(boardState[i][j] == ' '):
                return False
    return True

while(isRunning):
    playerInputValid = False
    print("It is player " + str(playerTurn) + "'s turn")
    printBoard()
    while(playerInputValid == False):
        playerInput[0] = input("Which column would you like to play in? Please Type 1, 2, or 3: ")
        playerInput[1] = input("Which row would you like to play in? Please Type 1, 2, or 3: ")
        if(validateInput(playerInput) == True):
            if(validateLocation(parseInput(playerInput)) == True):
                playerInputValid = True;
            else:
                print("Your location is invalid, please try again")
        else: print("Your input is invalid, please try again")
    if (playerTurn == 1):
        play(parseInput(playerInput), 'X')
        if(checkWin() == True):
            printBoard()
            print("player " + str(playerTurn) + " wins!")
            isRunning = False
        if (checkFull() == True):
            printBoard()
            print("Draw!")
            isRunning = False
        playerTurn = 2
    else:
        play(parseInput(playerInput), 'O')
        if(checkWin() == True):
            printBoard()
            print("player " + str(playerTurn) + " wins!")
            isRunning = False
        if (checkFull() == True):
            printBoard()
            print("Draw!")
            isRunning = False
        playerTurn = 1
