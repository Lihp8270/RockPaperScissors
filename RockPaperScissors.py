import random

numOfGames = None
gamesPlayed = 0
wins = 0 # From the computer perspective
ties = 0 # From the computer perspective
losses = 0 # From the computer perspective
winPercentage = None # From the computer perspective
userThrow = None
lastUserThrow = None
lastGameResult = None # From the computer perspective
comThrow = None
validThrow = 0 # Flag to validate user input
firstPlayedGame = 1 # Flag to tell function to make a random selection

moveNames = {
    'R': 'Rock',
    'P': 'Paper',
    'S': 'Scissors',
}

def CalculateThrow(lastPlayed, lastResult, firstGame):
    moveDict = {
        1: 'R',
        2: 'P',
        3: 'S',
    }

    if firstGame == 1:
        return moveDict[random.randint(1,3)]
    
    if lastResult == 'Win':
        if lastPlayed == 'R':
            myThrow = 'R'                
        elif lastPlayed == 'P':
            myThrow = 'P'            
        elif lastPlayed == 'S':
            myThrow = 'S'
    elif lastResult == 'Lost':
        if lastPlayed == 'R':
            myThrow = 'P'                
        elif lastPlayed == 'P':
            myThrow = 'S'            
        elif lastPlayed == 'S':
            myThrow = 'R'            
    elif lastResult == 'Tie':
        if lastPlayed == 'R':
            myThrow = 'S'                
        elif lastPlayed == 'P':
            myThrow = 'R'            
        elif lastPlayed == 'S':
            myThrow = 'P'            
    return myThrow

def inputTest(userInput):
    if userInput == 'R' or 'P' or 'S':
        return True
    else:
        return False
    Pass

def playGame(user, com):
    if userThrow == 'R':
        if comThrow == 'R':
            gameResult = 'Oof, tie!'
        elif comThrow == 'P':
            gameResult = 'BOOM! I won!'
        elif comThrow == 'S':
            gameResult = 'RIP, I lost!'
    elif userThrow == 'P':
        if comThrow == 'P':
            gameResult = 'Oof, tie!'
        elif comThrow == 'S':
            gameResult = 'BOOM! I won!'
        elif comThrow == 'R':
            gameResult = 'RIP, I lost!'
    elif userThrow == 'S':
        if comThrow == 'S':
            gameResult = 'Oof, tie!'
        elif comThrow == 'R':
            gameResult = 'BOOM! I won!'
        elif comThrow == 'P':
            gameResult = 'RIP, I lost!'
    return gameResult

numOfGames = int(input("How many games do you want to play?\n"))

while gamesPlayed < numOfGames:
    gamesPlayed += 1
    print("Game", gamesPlayed,":")
    userThrow = input("Throw your hand! (R for Rock, P for Paper, S for Scissors): ").upper()
    
    if inputTest(userThrow) == True:
        validThrow = 1
    else:
        validThrow = 0

    #Check input is valid
    while validThrow == 0:
        userThrow = input("Incorrect format is R P or S please try again: ").upper()
        if inputTest(userThrow) == True:
            validThrow = 1
        else:
            validThrow = 0

    comThrow = CalculateThrow(lastUserThrow,lastGameResult,firstPlayedGame)
    outcome = playGame(userThrow, comThrow)
    
    if outcome == 'Oof, tie!':
        ties += 1
    elif outcome == 'BOOM! I won!':
        wins += 1
    elif outcome == 'RIP, I lost!':
        losses += 1
    
    print('You played ',moveNames[userThrow],' - I play ',moveNames[comThrow])
    print(outcome)

print('\nComp Scores\n------------\nWins: ',wins,'\nLosses: ',losses,'\nTies: ',ties,'\n\nWin Percentage: ',int((wins/numOfGames*100)),'%')