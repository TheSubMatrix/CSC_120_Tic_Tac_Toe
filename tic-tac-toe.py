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

while(isRunning):
    playerInputValid = False
    print("It is player " + str(playerTurn) + "'s turn")
    print(boardState[0][0] + '|' + boardState[1][0] + '|' + boardState[2][0])
    print('-+-+-')
    print(boardState[0][1] + '|' + boardState[1][1] + '|' + boardState[2][1])
    print('-+-+-')
    print(boardState[0][2] + '|' + boardState[1][2] + '|' + boardState[2][2])
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
        playerTurn = 2
    else:
        play(parseInput(playerInput), 'O')
        playerTurn = 1
